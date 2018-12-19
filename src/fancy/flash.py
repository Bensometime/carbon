<<<<<<< HEAD
import time
import board
import neopixel
import webcolors

pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((0,0,0))

pixels.fill((0,255,0))
time.sleep(3)
pixels.fill((0,0,0))

i = 0

while True:

    if pixels[i][1] != 0:
        pixels[i] = (0,0,0)
    else:
        pixels[i] = (0,255,0)

    if i<29:
        i = i + 1
    else:
        i = 0

    time.sleep(0.1)
=======
import time
import board
import neopixel
import webcolors

pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((0,0,0))

pixels.fill((0,255,0))
time.sleep(3)
pixels.fill((0,0,0))

i = 0

while True:
    i = i+1 if i < 3 else i = 0
    pixels[i] = (0,0,0) if pixels[i][1] != 0 else pixels[i] = (0,255,0)
    time.sleep(0.1)
>>>>>>> b9688cd70e8c2716226f5aabedcdea25308abb7b
