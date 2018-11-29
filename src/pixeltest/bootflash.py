
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.d18, 30)


time.sleep(8)

pixels[0] = (255,0,0)

time.sleep(3)

pixels.fill((0,0,0))