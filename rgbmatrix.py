#!/usr/bin/env python
import cffi

prototypes = ""
with open('matrix/include/led-matrix-c.h') as f:
    prototypes = [line.strip() for line in f.readlines()
                       if line.strip() and not
                       line.startswith('#') and not
                       line.startswith('//') and not
                       line.startswith('}') and not
                       line.startswith('extern "C"')]

prototypes = "\n".join(prototypes)
# print("prototypes: \n%s" % prototypes)

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
    def create_offscreen_canvas(self):
        return lib.led_matrix_create_offscreen_canvas(self.matrix)
    def swap_on_vsync(offscreen_canvas):
        return lib.led_matrix_swap_on_vsync(self.matrix, offscreen_canvas)
    def close(self):
        lib.led_matrix_delete(self.matrix)
