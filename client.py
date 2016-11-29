import socket
import os
import base64
import subprocess
import numpy as np
import cv2
import cv2.cv as cv
import sys

HOST = socket.gethostname()    # The remote host # use your pc name if you use pc as server 
PORT = 4000      	  # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #client_socket created

s.connect((HOST, PORT))                             #connecting to the server
sys.stdout.flush()                      

while 1:

        size = s.recv(1)                                 #receiving size of the image size before the actual data size
        size_size =int(size)
        print ("The size of file size is - ",size_size," bytes")

        size_d=s.recv(size_size)                    # size of image data file
        size_data=int(size_d)
        print("The size of file is- ",size_data,"bytes")

        d = ""
        while 1:
                strng = s.recv(size_data)
                d += strng
                print "string ", strng
                if len(d)>=size_data:
                        break

        data=np.fromstring(d,dtype='uint8')
        frame=cv2.imdecode(data,1)                     #decode the data
        cv2.imshow("image",frame)               #call the media application to open the file
        k=cv2.waitKey(1)
        if k==27:
                break
    

cv2.destroyAllWindows()
s.close()
