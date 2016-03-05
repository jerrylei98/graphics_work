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

#-----------
#constant

m = [[], [], [], []]
x = XRES/2
y = YRES/2



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
