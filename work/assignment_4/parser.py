from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f1 = open(fname, 'r')
    d = f1.read().split('\n')
    c1 = 0
    while c1 < len(d):
        if c1 == 'circle':
            d1 = d[c1+1].split(' ')
            circle(d1[0], d1[1], d1[2]) #use proper command
        elif c1 == 'hermite':
            d1 = d[c1+1].split(' ')
        elif c1 == 'hermite':
            d1 = d[c1+1].split(' ')
        elif c1 == 'hermite':
            d1 = d[c1+1].split(' ')
        c1 += 1
        

