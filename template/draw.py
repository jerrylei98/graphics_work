from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
#   Plot call: plot(screen, color, c1, 250)
    if(x1 < x0): #flip if QII,QIII
        hold_x = x1
        hold_y = y1
        x1 = x0
        y1 = y0
        x0 = hold_x
        y0 = hold_y
    x = x0
    y = y0

    dy = y1 - y0
    dx = x0 - x1
            
    if y1 > y0: #Quadrant 1/2
        d = dy + dy + dx
        if dy <  -dx:
            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += dx * 2
                x += 1
                d += dy * 2
        else:
            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += dy * 2
                y += 1
                d += dx * 2
    else: #Quadrant 3/4
        d = dy + dy - dx
        if dy > dx:
            while x < x1:
                plot(screen,color,x,y)
                if d < 0:
                    y -= 1
                    d -= dx * 2
                x += 1
                d += dy * 2
        else:
            while y > y1:
                plot(screen,color,x,y)
                if d> 0:
                    x += 1
                    d += dy * 2
                y -= 1
                d -= dx * 2


