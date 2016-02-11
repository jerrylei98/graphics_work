from sys import argv
if len(argv) > 1:
    go = argv[1]
else:
    go = ""

FILE_NAME = "assignment_1" #no need for .ppm
IMAGE_TYPE = "P3"
X_MAX = 640
Y_MAX = 640
MAX_COLOR = 255

if go == "imgur":
    fd = open("../../../image_files/" + FILE_NAME + ".ppm", "w")
else:
    fd = open(FILE_NAME + ".ppm", 'w')
fd.write(IMAGE_TYPE + " " + str(X_MAX) + " " + str(Y_MAX) + " " + str(MAX_COLOR))


white = " 0 0 0 "
black = " 255 255 255 " 


cX = 0
while(cX < X_MAX):
    cY = 0
    while(cY < Y_MAX):
          if (cY / 80) % 2 == 0:
              if (cX / 80) % 2 == 1:
                  fd.write(white)
              else:
                  fd.write(black)
          else:
              if (cX / 80) % 2 == 1:
                  fd.write(black)
              else:
                  fd.write(white)          
          cY+=1
    cX += 1


fd.close()

if go == "imgur":
    from subprocess import Popen,PIPE
    cmd = "../../scripts/upload.sh " + FILE_NAME
    p = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()

    #read the imgur link
    fd = open("../../scripts/imgur_return.txt", "r")
    print '\n' + fd.read() + '\n'
    fd.close()        

