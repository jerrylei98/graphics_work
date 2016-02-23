from sys import argv
from display import * 
from draw import *

#--Checks if argument is 'imgur'--

if len(argv) > 1:
    go = argv[1]
    FILE_NAME = "assignment_2.ppm"
    fname = "../../../image_files/" + FILE_NAME
else:
    go = ""

#-----------
#constant


screen = new_screen()
color = [ 0, 255, 0 ]

#octant I
draw_line( screen, 0, 0, XRES - 1, YRES - 75, color )
"""
#octant II
draw_line( screen, 0, 0, XRES - 75, YRES - 1, color )
#octant VIII
draw_line( screen, 0, YRES - 1, XRES - 1, 75, color )
#octant VII
draw_line( screen, 0, YRES - 1, XRES - 75, 0, color )


color[ GREEN ] = 0
color[ RED ] = MAX_COLOR
#octant V
draw_line( screen, XRES - 1, YRES - 1, 0, 75, color )
#octant VI
draw_line( screen, XRES - 1, YRES - 1, 75, 0, color )
#octant IV
draw_line( screen, XRES - 1, 0, 0, YRES - 75, color )
#octant III
draw_line( screen, XRES - 1, 0, 75, YRES - 1, color )


color[ BLUE ] = MAX_COLOR
color[ RED ] = 0
#y = x
draw_line( screen, 0, 0, XRES - 1, YRES - 1, color )
#y = -x
draw_line( screen, 0, YRES - 1, XRES - 1, 0, color )

color[ GREEN ] = MAX_COLOR
#horizontal
draw_line( screen, 0, YRES / 2, XRES - 1, YRES / 2, color )
#vertical
draw_line( screen, XRES / 2, 0, XRES / 2, YRES - 1, color )

"""

if go != "imgur":
    display(screen)

#--Executes upload to imgur--
if go == "imgur":
    from subprocess import Popen, PIPE
    save_ppm(screen, fname)
    cmd = "../../scripts/upload.sh " + FILE_NAME
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()

    #read the imgur link
    fd = open("../../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()  
      
#------ file end
