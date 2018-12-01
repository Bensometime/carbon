import os
import time
import board
import neopixel
import webcolors

pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((0,0,0))

from flask import Flask
from flask import request

app = Flask(__name__)

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
    return "wat"

@app.route('/off')
def turnoff():
    print("turning lights off from /off")
    pixels[0] = (0,0,0)
    pixels[1] = (0,0,0)
    pixels[2] = (0,0,0)
    return "turning off"

@app.route('/color/<input>', methods=['GET','POST'])
def color(input):
    if request.method == 'POST':
        parseinput(input)
    if request.method == 'GET':
        #todo: make this return the pixel states
        return getcolor()
        return input

#my impulse to make this a single mega function for every case should be
#supressed... so for now it will just parse the string and change lights 1-3
#to the parsed color
def parseinput(input):
    newcolor = webcolors.name_to_rgb(input)
    pixels[0] = newcolor
    #or when that is inevitably a type error
    pixels[0] = (newcolor.red, newcolor.green, newcolor.blue)
    pixels[1] = (newcolor.red, newcolor.green, newcolor.blue)
    pixels[2] = (newcolor.red, newcolor.green, newcolor.blue)

def getcolor():
    newcolor = webcolors.rgb_to_name(pixels[0][0], pixels[0][1], pixels[0][2])
