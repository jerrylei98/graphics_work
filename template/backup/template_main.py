
#--Checks if argument is 'imgur'--
from sys import argv
if len(sys.argv) > 1:
    go = sys.argv[1]
else:
    go = ""

#--Creates ppm file-- 

FILE_NAME = "" #no need for .ppm
IMAGE_TYPE = "P3"
X_MAX = 500
Y_MAX = 500
MAX_COLOR = 255

if go == "imgur": #if imgur is an argument
    fd = open("../../../image_files/" + FILE_NAME + ".ppm", "w")
else:
    fd = open(FILE_NAME + ".ppm", 'w')

fd.write(IMAGE_TYPE + " " + str(X_MAX) + " " + str(Y_MAX) + " " + str(MAX_COLOR))

#<--Drawing goes here-->#


fd.close()

#--Executes upload to imgur--
if go == "imgur":
    from subprocess import Popen, PIPE
    
    cmd = "../../scripts/upload.sh " + FILE_NAME
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #found on stackoverflow
    p.wait()

    #read the imgur link
    fd = open("../../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()        
