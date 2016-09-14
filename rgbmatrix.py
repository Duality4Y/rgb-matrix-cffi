#!/usr/bin/env python
import cffi
import sys
import re

prototypes = ""
# remove the bulk of the comments and things we don't want.
with open('matrix/include/led-matrix-c.h') as f:
    prototypes = [line.strip() for line in f.readlines()
                       if line.strip() and not
                       line.startswith('#') and not
                       line.startswith('//') and not
                       line.startswith('}') and not
                       line.startswith('extern "C"')]

# http://stackoverflow.com/questions/241327/python-snippet-to-remove-c-and-c-comments
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

# removes rest of those pesky comments. :)
prototypes = comment_remover("\n".join(prototypes)).split('\n')
# make nice and presentable
prototypes = "\n".join([line.strip() for line in prototypes if line.strip()])
# print(prototypes)

"""
    notice that cdef removes moste comments by it's self.
    but # directives because it can't handle those yet.

    but clean the source anyway as to be sure it works.
"""

ffi = cffi.FFI()
lib = ffi.dlopen('matrix/lib/librgbmatrix.so.1')
ffi.cdef(prototypes)

class Canvas(object):
    def __init__(self, matrix=None):
        if matrix:
            self.canvas = lib.led_matrix_get_canvas(matrix.matrix)
        self.width_pointer = ffi.new("int *width")
        self.height_pointer = ffi.new("int *height")
    def get_size(self):
        lib.led_canvas_get_size(self.canvas, self.width_pointer, self.height_pointer)
        return (self.width_pointer[0], self.height_pointer[0])
    def clear(self):
        lib.led_canvas_clear(self.canvas)
    def fill(self, r, g, b):
        lib.led_canvas_fill(self.canvas, r, g, b)
    def set_pixel(self, x, y, r, g, b):
        lib.led_canvas_set_pixel(self.canvas, x, y, r, g, b)

class Matrix(object):
    def __init__(self, rows, chained, parallel):
        self.matrix = lib.led_matrix_create(rows, chained, parallel)
        if self.matrix == ffi.NULL:
            print("Exiting because couldn't initiate matrix.")
            sys.exit(1)
    def create_offscreen_canvas(self):
        return lib.led_matrix_create_offscreen_canvas(self.matrix)
    def swap_on_vsync(offscreen_canvas):
        return lib.led_matrix_swap_on_vsync(self.matrix, offscreen_canvas)
    def close(self):
        lib.led_matrix_delete(self.matrix)
