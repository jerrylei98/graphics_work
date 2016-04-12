from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

"""
poly = new_matrix(4,0)
add_box(poly, 0, 0, 0, 200, 100, 400)

draw_polygons(poly,screen,color)
display(screen)

"""
if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, transform, screen, color )
f.close()
