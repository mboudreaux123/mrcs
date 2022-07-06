import socket, sys, cv2, pickle, struct
from colorama import *

port = 29532

def printBorder(length = 64):
    print("-" * length)

def initialScreen():
    printBorder()
    print("----------------"  + Fore.MAGENTA + " PiCar Server " + Style.RESET_ALL + "----------------")
    print()
    print("Host: TODO")
    print("IP: TODO")
    print("Port:", port)
    print()
    
def terminateScreen():
    print()
    printBorder()
    print()
    print(Fore.RED + "Server terminated" + Style.RESET_ALL)
    print()
    printBorder()
    
def main():
    init()
    initialScreen()

    ## Create a socket instance
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Listen on specified port
    sock.bind(('', port))  
    sock.listen(5)
    print("Server listening...")

    ## Establish connection
    while True:
        ## Attempt to accept incoming connection
        conn, addr = sock.accept()
        
        ## If there is a remote connection, let client control bot
        if conn:
            stream = cv2.VideoCapture(0)
            print("[REMOTE] - " + Fore.GREEN + "Accepted connection from" + Style.RESET_ALL, addr[0])
  
            ## Send video stream to client
            pos_frame = stream.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            while True:
                flag, frame = stream.read()
                if flag:
                    frame = cPickle.dumps(frame)
                    size = len(frame)
                    p = struct.pack('I', size)
                    frame = p + frame
                    client_socket.sendall(frame)
                else:
                    stream.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
      
                if stream.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == stream.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
                    size = 10
                    p = struct.pack("I", size)
                    client_socket.send(p)
                    client_socket.send('')
                    break
  
            ## Close connection
            conn.close()
            print("[REMOTE] - " + Fore.RED + "Connection closed" + Style.RESET_ALL)
            
        # Otherwise, control robot locally
        else:
            print("[LOCAL] - Enabled")
            # Take controller input from 

if __name__ == '__main__':
    try:
        main()
        terminateScreen()
    except KeyboardInterrupt:
        terminateScreen()
        sys.exit(0)



















































