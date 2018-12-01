import board
import neopixel
import time
import sys

red =	int(sys.argv[1])
green =	int(sys.argv[2])
blue =	int(sys.argv[3])

pixels = neopixel.NeoPixel(board.D18, 32)

i = 0

while i != 31:
    pixels[i] = (red, green, blue)
    i = i+1

time.sleep(5)

pixels.fill((0,0,0))
