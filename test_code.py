import time
import random

from rgbmatrix import Matrix
from rgbmatrix import Canvas

rows = 32
chaines = 4
parallel = 2

matrix = Matrix(rows, chaines, parallel)
canvas = Canvas(matrix)
width, height = canvas.get_size()
print(width, height)
# canvas.fill(0x0, 0xFF, 0x00)
# time.sleep(2)

# canvas.clear()
# time.sleep(2)

for i in range(0, height):
    canvas.set_pixel(i, i, 0x00, 0x00, 0xff)
    time.sleep(0.01)

canvas.set_pixel(15, 15, 0x00, 0x00, 0xff)
canvas.set_pixel(15, 16, 0x00, 0x00, 0xff)

time.sleep(2)

x, y = random.randint(0, width - 1), random.randint(0, height - 1)
deltax, deltay = 1, 1

it = 0

while(1):
    it += 1
    if it == 10000:
        break
    canvas.fill(0x00, 0x00, 0x00)
    canvas.set_pixel(x, y, 0x00, 0x00, 0xFF)
    if x >= width or x < 0:
        deltax *= -1
    if y >= height or y < 0:
        deltay *= -1
    x += deltax
    y += deltay
    time.sleep(0.01)

matrix.close()
