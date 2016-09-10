import time
from rgbmatrix import Matrix
from rgbmatrix import Canvas

rows = 64
chaines = 4
parallel = 2

matrix = Matrix(rows, chaines, parallel)
canvas = Canvas(matrix)
width, height = canvas.get_size()

canvas.fill(0x0, 0xFF, 0x00)
time.sleep(2)

canvas.clear()
time.sleep(2)

for i in range(0, height):
    canvas.set_pixel(i, i, 0x00, 0x00, 0xff)
time.sleep(10)

matrix.close()
