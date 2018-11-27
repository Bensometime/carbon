import os
import time

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
def returnlist(color):
    return color
