from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    c1 = 0;
    while(c1 < XRES):
        plot(screen, DEFAULT_COLOR, c1, 250)
        c1+=1
"""    m = (y1 - y0) / (x1 - x0)
    #QUADRANT 1
    #OCTANT I
    if x0 > 0 & x1 > 0 & y0 > 0 & y1 > 0:
        if 0 < m < 1:
            print 'O1'
        elif m > 1:
            print 'O2'
        print 'Q1'"""



