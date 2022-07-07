import socket, sys, cv2, pickle, struct
import miscUtils
from colorama import *

port = 29532

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
            print("[REMOTE] - " + Fore.GREEN + "Accepted connection from" + Style.RESET_ALL, addr[0])
  
            ## Send video stream to client
            #while True:
  
            ## Close connection
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



















































