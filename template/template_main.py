#--Checks if argument is 'imgur'--
from sys import argv
if len(sys.argv) > 1:
    go = sys.argv[1]
else:
    go = ""









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
