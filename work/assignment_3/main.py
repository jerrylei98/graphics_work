from sys import argv
from display import * 
from draw import *

#--Checks if argument is 'imgur'--

if len(argv) > 1:
    go = argv[1]
    FILE_NAME = "assignment_2"
    fname = "../../../image_files/" + FILE_NAME + ".ppm"
else:
    go = ""

screen = new_screen()
color = [255,0,0]

#-----------
#constant
x = 50#XRES/2
y = 50#YRES/2
z = 0
#m = [[],[],[],[]]
m = [[0,100,100,100,100,0,0,0],[0,0,0,100,100,100,100,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]]

final_m = m

c1 = 0
while(c1 < 180):
    j = matrix_mult(make_rotZ(degree2radian(c1)), m)
    final_m[0].extend(j[0])
    final_m[1].extend(j[1])
    final_m[2].extend(j[2])
    final_m[3].extend(j[3])
    c1+=18

final_m = matrix_mult(make_translate(250,250,0),final_m)
draw_lines(final_m,screen,color)



"""
draw_line(screen,XRES/2,0,XRES/2,YRES, [0,0,0])
draw_line(screen,0,YRES/2,XRES,YRES/2, [0,0,0])
"""







#---------------------------------------------------------------#

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
