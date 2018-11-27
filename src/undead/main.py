import os
import time
import board
import NeoPixel

pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((0,0,0))

from flask import Flask
from flask import request

app = Flask(__name__)

def testboi():
    print("yes")

@app.route('/')
def index():
    print("I was consulted")
    return "banana"

@app.route('/tertiary')
def tertiary():
    page = "<html><h1>hack</h1></html>"
    return page

@app.route('/restart')
def restart():
    os.execl('restart.sh','')
    print("Still running...?")

@app.route('/test')
def testguy():
    testboi()
    return "wat"

@app.route('/color/<color>')
def redtoggle(color):
    print("requested " + color)
    if(color == 'red')
        print("turning lights red")
        pixels[0] = (255,0,0)
        pixels[1] = (255,0,0)
        pixels[2] = (255,0,0)
    if(color != 'red')
        print("turning lights off from /red")
        pixels[0] = (0,0,0)
        pixels[1] = (0,0,0)
        pixels[2] = (0,0,0)
    return color

@app.route('/off')
def turnoff():
    print("turning lights off from /off")
    pixels[0] = (0,0,0)
    pixels[1] = (0,0,0)
    pixels[2] = (0,0,0)
    return "turning off";    
