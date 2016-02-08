#--Checks if argument is 'imgur'--
import sys
if len(sys.argv) > 1:
    go = sys.argv[1]
else:
    go = ""

#--Creates ppm file-- 

FILE_NAME = "full_black" #no need for .ppm
IMAGE_TYPE = "P3"
X_MAX = 1024
Y_MAX = 600
MAX_COLOR = 255

if go == "imgur": #if imgur is an argument
    fd = open("../../../image_files/" + FILE_NAME + ".ppm", "w")
else:
    fd = open(FILE_NAME + ".ppm", 'w')

fd.write(IMAGE_TYPE + " " + str(X_MAX) + " " + str(Y_MAX) + " " + str(MAX_COLOR))

#<--Drawing goes here-->#

cX = 0
cY = 0

c = raw_input("Color ex. '255 255 255': ")
color = ' ' + c + ' '

while cY < Y_MAX:
    while cX < X_MAX:
        fd.write(color)
        cX += 1
    cY += 1


fd.close()

#--Executes upload to imgur--
if go == "imgur":
    import subprocess
    
    cmd = "../../scripts/upload.sh " + FILE_NAME
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #found on stackoverflow
    p.wait()

    #read the imgur link
    fd = open("../../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()        
