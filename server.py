import socket
import base64
import numpy
import cv2
import time

HOST = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #server_socket created

s.bind((HOST, 4000))                        #binding the socket to the address

s.listen(1)                                 #listening for the connection

conn, addr = s.accept()                     #accepting a connection and creating another socket for that client
print('Connected by', addr)

cap=cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,400)

while 1:

    ret,frame=cap.read()        #opening the file required in read mode
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    time.sleep(0.001)
    if ret == True:
        #cv2.imshow('frame',frame)
        #k=cv2.waitKey(1)
        #if (k==27):
            #cv2.destroyAllWindows()
            #conn.close()
        encode_p=[int(cv2.IMWRITE_JPEG_QUALITY),20]
        result,dstrng=cv2.imencode('.jpg',frame,encode_p)       #encoding the given file
        
        data=numpy.array(dstrng)
        strng=data.tostring()
        
        size=len(strng)
        size_data = str(size).encode('utf-8')       #size of image data
        
        #size of size
        a=len(size_data)
        print("The size of file is-",size,"bytes")
        size_of_size=str(a).encode('utf-8')  

        conn.send(size_of_size)                 
        conn.send(size_data)                   
        conn.sendall(strng)                      #sending the file
        
cv2.destroyAllWindows()    
conn.close()

