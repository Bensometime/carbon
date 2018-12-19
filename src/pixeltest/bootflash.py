
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)


time.sleep(3)

pixels[0] = (255,0,0)
pixels[1] = (255,0,0)
pixels[2] = (255,0,0)
pixels[3] = (255,0,0)

time.sleep(3)

pixels.fill((0,0,0))
