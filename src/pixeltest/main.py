import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)

while True:

    pixels[0] = (255,0,0)
    pixels[1] = (0,255,0)
    pixels[2] = (0,0,255)

    time.sleep(3)

    pixels[0] = (0,0,0)
    pixels[1] = (0,0,0)
    pixels[2] = (0,0,0)
    
    time.sleep(3)
