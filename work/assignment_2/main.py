from sys import argv
from display import * 
from draw import *

#--Checks if argument is 'imgur'--

if len(sys.argv) > 1:
    go = sys.argv[1]
    fname = "../../../assignment_n"
else:
    go = ""

#-----------
#constant

screen = new_screen()




if go not "imgur":
    display(screen)




#--Executes upload to imgur--
if go == "imgur":
    from subprocess import Popen, PIPE
    save_ppm(screen, fname)
    cmd = "../../scripts/upload.sh " + FILE_NAME
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #found on stackoverflow
    p.wait()

    #read the imgur link
    fd = open("../../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()  
      
#------ file end
