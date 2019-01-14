import requests
import threading


#i = 0
#r = requests.get('http://192.168.0.10:5000/single/name?n=0&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=1&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=2&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=3&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=4&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=5&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=6&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=7&c=red')
#r = requests.get('http://192.168.0.10:5000/single/name?n=8&c=red')

#while i < 29:
#    url = ('http://192.168.0.10:5000/single/name?n=%d&c=blue' % i)
#    r = requests.get(url)
#    i = i + 1

#okay, let's try it with threads to make fast(...?)

i = 0

def redify(num):
    r = requests.get('http://192.168.0.10:5000/single/name?n=%d&c=red' % num)
    return

threads = []
for x in range(29):
    t = threading.Thread(target=redify(x))
    threads.append(t)
    t.start()