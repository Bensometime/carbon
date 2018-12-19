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
    pixels.fill((0,0,0))
    return "turning off"

@app.route('/green')
def green():
    print("turning the lights green")
    pixels[0] = (0,255,0)
    pixels[1] = (0,255,0)
    pixels[2] = (0,255,0)
    pixels[3] = (0,255,0)
    pixels[4] = (0,255,0)

@app.route('/color/<input>', methods=['GET','POST'])
def color(input):
    if request.method == 'POST':
        pixels.fill(parseinput(input))
        return input
    if request.method == 'GET':
        #this is a standin because I don't have an app to test the real
        #http request style with (yet)
<<<<<<< HEAD
        pixels.fill(parseinput(input))
=======
        parseinput(input)
>>>>>>> b9688cd70e8c2716226f5aabedcdea25308abb7b
        #done: make this return the pixel states
        return getcolor()
        #todo: make parseinput work over post request
        return input
    return input

#my impulse to make this a single mega function for every case should be
#supressed... so for now it will just parse the string and change lights 1-3
#to the parsed color
def parseinput(input):
    newcolor = webcolors.name_to_rgb(input)
    return (newcolor.red, newcolor.green, newcolor.blue)

def getcolor():
    newcolor = webcolors.rgb_to_name((pixels[0][0], pixels[0][1], pixels[0][2]))
    return newcolor

app.run('0.0.0.0')
