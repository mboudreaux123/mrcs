import socket
import robot.miscUtils

port = 29532
#server_ip = "192.168.7.109"
server_ip = "localhost"
 
## Create a socket instance
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                
 
# connect to the server on local computer
sock.connect((server_ip, port))
 
# receive data from the server and decoding to get the string.
print(sock.recv(1024).decode())

# close the connection
sock.close()
