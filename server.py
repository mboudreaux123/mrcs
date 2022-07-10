import socket, sys, cv2, pickle, struct, time, os, pygame, select
from robot.miscUtils import *
import robot.ds4, robot.steer
#robot.motor, robot.steer, robot.head, robot.servo_manager
from _thread import *



import threading
from robot.miscUtils import *

class server():
    def __init__(self, port = 29532, remoteAllowed = True):
        self.remoteAllowed = remoteAllowed
        self.remoteEnabled = False
        self.steer = robot.steer.Steer()
        self.controller = robot.ds4.DS4()

        ## Enable networking is remote is allowed
        if self.remoteAllowed:
            self.port = port
            self.sock = socket.socket()
            self.hostname = socket.gethostname()
            self.hostip = socket.gethostbyname(self.hostname)
            self.clientConnect = None
            self.clientAddress = None

            ## Set server into listen mode
            self.sock.bind(('', self.port))    
            self.sock.listen(5)

            ## Start thread to listen for remote connetion
            self.thread = threading.Thread(target=self.listenForConnection, args=())
            self.thread.start()

            ## Print out network stats
            print("Host: " + self.hostname)
            print("IP: " + self.hostip)
            print("Port:", self.port)
            print()
    
    def listenForConnection(self):
        if self.remoteAllowed:
            while True:
                if not self.remoteEnabled:
                    self.clientConnect, self.clientAddress = self.sock.accept()
                    self.remoteEnabled = True
                    print("[REMOTE] - " + Fore.GREEN + "Accepted connection from" + Style.RESET_ALL, self.clientAddress[0])
                time.sleep(1)

    def killConnection(self):
        ## Close client connections
        self.clientConnect.close()
        self.clientConnect = None
        self.clientAddress = None
        self.remoteEnabled = False
        print("[REMOTE] - " + Fore.RED + "Connection closed" + Style.RESET_ALL)

    # https://stackoverflow.com/a/21802953
    def connectionDisconnected(self):
        try:
            ready_to_read, ready_to_write, in_error = \
            select.select([self.clientConnect,], [self.clientConnect,], [], 5)
            return False
        except:
            self.killConnection()
            return True

    def streamVideo(self):
        ## Video streaming stuff here
        if self.remoteEnabled and self.clientConnect:
            print("Stream video")
            self.clientConnect.send("sdijiopajdoiahohraopihefpahpvaoug".encode())

    ## Process inputs and perform action based on remote client input
    def remoteControl(self):
        while self.remoteEnabled:
            try:
                print(self.clientConnect)
                print(self.clientAddress)

                self.streamVideo()

                ## Close client connections
                #self.killConnection()

            except:
                self.killConnection()
            
            time.sleep(0.05)

    ## Process inputs and perform action based on local server input
    def localControl(self):
        print("[LOCAL] - Enabled")
        while not self.remoteEnabled:

            # Load controller input
            self.controller.loadInputs() 

            # Process controller input
            print(self.controller.getAxisAt(robot.ds4.AXIS_LEFT_STICK_X))
            steerFactor = robot.miscUtils.convertRange(-1.0, 1.0, self.steer.getMaxAngle(), self.steer.getMinAngle(), self.controller.getAxisAt(robot.ds4.AXIS_LEFT_STICK_X))
            self.steer.turn(steerFactor)
            time.sleep(0.05)
        print("[LOCAL] - Disabled")
       
    def run(self):
        while True:
            if self.remoteAllowed:
                ## Attempt to accept incoming connection
                if self.remoteEnabled and self.clientConnect:
                    self.remoteControl()
                ## Otherwise, control robot locally
                else:
                    self.localControl()
            else:
                self.localControl()

def main():
    carserver = server()
    carserver.run()

if __name__ == '__main__':
    try:
        initServerScreen()
        main()
        terminateServerScreen()
        sys.exit(0)
    except KeyboardInterrupt:
        terminateServerScreen()
        sys.exit(0)





















































