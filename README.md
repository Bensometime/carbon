# Carbon
Carbon is, at it's most simple, a python script which allows a raspberry pi to
act as a network-mounted controller for a set of neopixel rgb lights

## Goals
Carbon was envisioned as a system for controlling wearable or otherwise mobile
LEDs in a self-contained manner suitable for easy use in a variety of projects
including clothing, props, masks, etc. The primary use case involves setting up
a raspberry pi to run as both a hotspot and a server(?) for controlling the
lights. The user could hide the raspberry pi and power source and simply use a
phone or other device to control the parameters of the lights.

## Structure
src/cserver.py (Carbon Server) is the core of this project. It accepts input
in a REST structure via http requests and applies that input to control the
lights.

notes.txt contains thoughts and musings I've found useful while developing the
project. While I don't usually recommend wading through my ravings, it's
possible someone might find value in looking through them.

fancy/ and examplewebapp/ are works in progress for refining a way to write
animations and a simple web app to interface with carbon respectively. They are
very much unfinished at present time.

[start.sh, restart.sh, rc.local coming soon]

## Status
[coming soon]

## Installation
[Coming soon]

## Usage
[Coming soon]
