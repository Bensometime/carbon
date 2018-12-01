import os
import time
import board
import neopixel
import webcolors

pixels = neopixel.NeoPixel(board.D18, 30)

color = webcolors.name_to_rgb('blue')
pixels[0] = ((color.red, color.green, color.blue))

print(pixels[0][0], pixels[0][1], pixels[0][2])

print(webcolors.rgb_to_name((pixels[0][0], pixels[0][1], pixels[0][2])))
