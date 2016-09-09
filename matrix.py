#!/usr/bin/env python
import cffi

matrix_prototypes = \
"""
    struct RGBLedMatrix;
    struct LedCanvas;
    struct RGBLedMatrix *led_matrix_create(int rows, int chained, int parallel);
    void led_matrix_delete(struct RGBLedMatrix *matrix);
    struct LedCanvas *led_matrix_get_canvas(struct RGBLedMatrix *matrix);
    void led_canvas_get_size(const struct LedCanvas *canvas,
                             int *width, int *height);
    void led_canvas_set_pixel(struct LedCanvas *canvas, int x, int y,
                              uint8_t r, uint8_t g, uint8_t b);
    void led_canvas_clear(struct LedCanvas *canvas);
    void led_canvas_fill(struct LedCanvas *canvas, uint8_t r, uint8_t g, uint8_t b);
    struct LedCanvas *led_matrix_create_offscreen_canvas(struct RGBLedMatrix *matrix);
    struct LedCanvas *led_matrix_swap_on_vsync(struct RGBLedMatrix *matrix,
                                               struct LedCanvas *canvas);
"""

prototypes = ""
with open('matrix/include/led-matrix-c.h') as f:
    prototypes = [line.strip() for line in f.readlines()
                       if line.strip() and not
                       line.startswith('#') and not
                       line.startswith('//') and not
                       line.startswith('}') and not
                       line.startswith('extern "C"')]

prototypes = "\n".join(prototypes)

ffi = cffi.FFI()
lib = ffi.dlopen('matrix/lib/librgbmatrix.so.1')
ffi.cdef(prototypes)
print(dir(ffi))
print(dir(lib))