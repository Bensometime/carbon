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

@app.route('/restart')
def restart():
    os.execl('restart.sh','')
    print("Still running...?")

@app.route('/off')
def turnoff():
    print("turning lights off from /off")
    pixels.fill((0,0,0))
    return "turning off"

@app.route('/valtest/')
def valtest():
    print(request.args.get('red', default = 0, type = int))
    return 'yes'


#this and others may need error checking
@app.route('/single/off', methods=['GET','POST'])
def singleoff():
    num = request.args.get('n', default = -1, type = int)
    if num != -1:
        pixels[num] = (0,0,0)
        if request.method == 'GET':
            return "Turned off " + str(num)
        if request.method == 'POST':
            return "", 201
    else:
        print("received an invalid value in /single/off")
        if request.method == 'GET':
            return "Error parsing given value in /single/off"

@app.route('/single/name', methods=['GET','POST'])
def singlename():
    num = request.args.get('n', default = -1, type = int)
    name = request.args.get('c', default = "black", type = str)
    if num != -1:
        pixels[num] = parsecolorname(name)
        if request.method == 'GET':
            return "set " + str(num) + " to " + name
        if request.method == 'POST':
                return "", 201
    else:
        print("received an invalid value in /single/name")
        if request.method == 'GET':
            return "Error parsing given value in /single/name"

@app.route('/single/rgb', methods=['GET','POST'])
def singlergb():
    num = request.args.get('n', default = -1, type = int)
    red = request.args.get('r', default = 0, type = int)
    green = request.args.get('g', default = 0, type = int)
    blue = request.args.get('b', default = 0, type = int)
    if num != -1:
        pixels[num] = ((red, green, blue))
        if request.method == 'GET':
            return "set " + str(num) + " to given rgb values"
        if request.method == 'POST':
            return "", 201
    else:
        print("received an invalid value in /single/rgb")
        if request.method == 'GET':
            return "Error parsing given value in /single/rgb"

@app.route('/all/name', methods=['GET','POST'])
def allname():
    name = request.args.get('c', default = "black", type = str)
    pixels.fill(parsecolorname(name))
    if request.method == 'GET':
        return "set all pixels to " + name
    if request.method == 'POST':
        return "", 201

@app.route('/all/rgb', methods=['GET','POST'])
def allrgb():
    red = request.args.get('r', default = 0, type = int)
    green = request.args.get('g', default = 0, type = int)
    blue = request.args.get('b', default = 0, type = int)
    pixels.fill((red,green,blue))
    if request.method == 'GET':
        return "set all pixels to given values"
    if request.method == 'POST':
        return "", 201

#my impulse to make this a single mega function for every case should be
#supressed...
def parsecolorname(input):
    newcolor = webcolors.name_to_rgb(input)
    return (newcolor.red, newcolor.green, newcolor.blue)

def getcolor(num):
    newcolor = webcolors.rgb_to_name((pixels[num][0], pixels[num][1], pixels[num][2]))
    return newcolor

app.run('0.0.0.0')
