#import os
from os import listdir
import imgur_utils
import sys

if len(sys.argv) > 1:

    fd = sys.argv[1]
    fd += '.png'


    imgur_id = imgur_utils.upload_local("/home/jerry/github/image_files/" + fd)
    
    imgur_fd = open("imgur_return.txt", 'w')

    imgur_fd.write(imgur_id)
    imgur_fd.close()
    
    print fd
