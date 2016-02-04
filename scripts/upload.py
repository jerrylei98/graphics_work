#import os
from os import listdir
import imgur

fd = ""

for png_file in listdir("/home/jerry/github/image_files"):
    if ".png" in png_file:
        fd = png_file

imgur_id = imgur.upload_local("/home/jerry/github/image_files/" + fd)

imgur_fd = open("imgur_return.txt", 'w')
#print imgur_id
imgur_fd.write("https://imgur.com/")
imgur_fd.write(image_id)
imgur_fd.close()
