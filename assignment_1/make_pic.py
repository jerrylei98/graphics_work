FILE_NAME = "assignment_1.ppm"
IMAGE_TYPE = "P3"
X_MAX = 500
Y_MAX = 500
MAX_COLOR = 255


fd = open("../../image_files/" + FILE_NAME, "w")
#fd = open(FILE_NAME, 'w')
fd.write(IMAGE_TYPE + " " + str(X_MAX) + " " + str(Y_MAX) + " " + str(MAX_COLOR))

cX = 0
cY = 0

while(cY < Y_MAX):
    while(cX < X_MAX):
          r = X_MAX - cX - MAX_COLOR
          g = X_MAX - cX - MAX_COLOR
          b = X_MAX - cX - MAX_COLOR
          fd.write(" " + str(r) + " " + str(g) + " " + str(b))
          cX+=1
    cY += 1

fd.close()
          
        

