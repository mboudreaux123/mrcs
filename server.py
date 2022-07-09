import socket, sys, cv2, pickle, struct, time, os, pygame
import robot.ds4, robot.motor, robot.steer, robot.head, robot.servo_manager
from _thread import *



import threading
from colorama import *
from miscUtils import *

def initScreen():
    printBorder()
    print("----------------"  + Fore.MAGENTA + " PiCar Server " + Style.RESET_ALL + "----------------")
    print()
    
def terminateScreen():
    print()
    printBorder()
    print()
    print(Fore.RED + "Server terminated" + Style.RESET_ALL)
    print()
    printBorder()

class server():
    def __init__(self, port = 29532, remoteAllowed = True):
        self.remoteAllowed = remoteAllowed
        self.remoteEnabled = False

        ## Enable networking is remote is allowed
        if self.remoteAllowed:
            self.port = port
            self.sock = socket.socket()
            self.clientConn = None
            self.clientAddr = None

            ## Set server into listen mode
            self.sock.bind(('', self.port))    
            self.sock.listen(5)

            self.thread = threading.Thread(target=self.socketThread, args=())
            self.start()

            ## Print out network stats
            print("Host: TODO")
            print("IP: TODO")
            print("Port:", self.port)
            print()
    
    def kill(self):
        ## Close client connections
        self.clientConnect.close()
        self.clientConn = None
        self.clientAddr = None
        self.remoteEnabled = False


    ## Thread to check for when connection to server is made by client
    def socketThread(self):
        while True:
            if self.remoteAllowed:
                if not self.remoteEnabled:
                    self.clientConnect, self.clientAddress = self.sock.accept()
                    self.remoteEnabled = True
                    print("[REMOTE] - " + Fore.GREEN + "Accepted connection from" + Style.RESET_ALL, self.clientAddress[0])

    ## Process inputs and perform action based on local server input
    def localControl(self):
        print("[LOCAL] - Enabled")
        # Take controller input from 
        # Process controller input

    ## Process inputs and perform action based on remote client input
    def remoteControl(self):
        ## Attempt to accept incoming connection
        ## If there is a remote connection, let client control bot
        if self.remoteEnabled and self.clientConnect:

            ## Send video stream to client
            self.clientConnect.send("sdijiopajdoiahohraopihefpahpvaoug".encode())
            
            ## Close client connections
            self.clientConnect.close()
            self.clientConn = None
            self.clientAddr = None
            self.remoteEnabled = False
            time.sleep(5)
            print("[REMOTE] - " + Fore.RED + "Connection closed" + Style.RESET_ALL)
            
        ## Otherwise, control robot locally
        else:
            self.localControl()

    def run(self):
        if self.remoteAllowed:
            while True:
                self.remoteControl()
        else:
            while True:
                self.localControl()

def main():
    init()
    carserver = server()
    carserver.run()

if __name__ == '__main__':
    try:
        initScreen()
        main()
        terminateScreen()
    except KeyboardInterrupt:
        terminateScreen()
        sys.exit(0)





















































