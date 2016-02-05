import sys
go = 'imgur'

FILE_NAME = "assignment_1" #no need for .ppm
IMAGE_TYPE = "P3"
X_MAX = 500
Y_MAX = 500
MAX_COLOR = 255

if go == "imgur":
    fd = open("../../image_files/" + FILE_NAME + ".ppm", "w")
else:
    fd = open(FILE_NAME + ".ppm", 'w')
fd.write(IMAGE_TYPE + " " + str(X_MAX) + " " + str(Y_MAX) + " " + str(MAX_COLOR))

cY = 0

while(cY < Y_MAX):
    cX = 0
    while(cX < X_MAX):
          r = X_MAX - cX - MAX_COLOR
#          g = (cX * (MAX_COLOR / X_MAX) % MAX_COLOR)
#          b = (cX * (MAX_COLOR / X_MAX) % MAX_COLOR)
          fd.write(" " + str(r) + " " + str(r) + " " + str(r))
          cX+=1
    cY += 1

fd.close()

if go == "imgur":
    import subprocess
    cmd = "../scripts/upload.sh " + FILE_NAME
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #found on stackoverflow
    p.wait()

    #read the imgur link
    fd = open("../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()        

