from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    m = (y1 - y0) / (x1 - x0)
    #QUADRANT 1
    #OCTANT I
    if x0 > 0 & x1 > 0 & y0 > 0 & y1 > 0:
        if 0 < m < 1:
            print 'O1'
        else if m > 1:
            print 'O2'
        print 'Q1'


