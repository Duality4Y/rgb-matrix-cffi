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
print("prototypes: \n%s" % prototypes)

ffi = cffi.FFI()
lib = ffi.dlopen('matrix/lib/librgbmatrix.so.1')
ffi.cdef(prototypes)

print(dir(ffi))
print(dir(lib))
