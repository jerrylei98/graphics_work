#import os
from os import listdir
import imgur_utils

fd = ""

for png_file in listdir("/home/jerry/github/image_files"):
    if ".png" in png_file:
        fd = png_file

imgur_id = imgur_utils.upload_local("/home/jerry/github/image_files/" + fd)

imgur_fd = open("imgur_return.txt", 'w')

imgur_fd.write(imgur_id)
imgur_fd.close()
