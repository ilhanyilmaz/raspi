import io
import socket
import struct
import cv2
import numpy as np

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')

cap = cv2.VideoCapture(0)

try:
    while True:
        f,frame = cap.read()
        cv2.imshow('frame', frame)
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        
        image = np.fromstring(connection.read(image_len), dtype=np.uint8).reshape((480,640,3))
        image2 = image.copy()
        cv2.imshow('image', image2)
        
        if cv2.waitKey(10) != -1:
            connection.close()
            server_socket.close()
            cap.release()
            cv2.destroyAllWindows()
            
finally:
    connection.close()
    server_socket.close()
    cv2.destroyAllWindows()
