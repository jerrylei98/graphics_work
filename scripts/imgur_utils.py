import json
import requests
import base64

#client_id
fd = open("/home/jerry/api_keys/imgur_graphics.txt", 'r')
keys = fd.read().split('\n')
fd.close()

CLIENT_ID = keys[0]
CLIENT_SECRET = keys[1]


url_image = "https://api.imgur.com/3/image"
url_album = "https://api.imgur.com/3/album"


def upload_local(fpath):
    r = requests.post(url_image, data = {'image': open(fpath, 'rb').read(),
                                         'type': 'file'},
                                         headers = {'Authorization': 'Client-ID ' + CLIENT_ID})
    data = r.json()
    image_id = data.get('data').get('id')
    return "https://imgur.com/" + image_id
                      
#print upload_local("/home/jerry/github/image_files/assignment_1.png")

#print "www.imgur.com/" + d
