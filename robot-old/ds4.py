import pygame, os, time
from colorama import *

os.environ["DISPLAY"] = ":0"

AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1
AXIS_L2 = 2
AXIS_R2 = 5
AXIS_RIGHT_STICK_X = 3
AXIS_RIGHT_STICK_Y = 4

BUTTON_CROSS = 0
BUTTON_CIRCLE = 1
BUTTON_TRIANGLE = 2
BUTTON_SQUARE = 3

BUTTON_L1 = 4
BUTTON_R1 = 5
BUTTON_L2 = 6
BUTTON_R2 = 7

BUTTON_SHARE = 8
BUTTON_OPTIONS = 9

BUTTON_PS = 10
BUTTON_LEFT_STICK = 11

BUTTON_RIGHT_STICK = 12
BUTTON_PAD = 13

# Labels for DS4 controller hats (Only one hat control)
HAT_1 = 0

PREFIX = "[ds4] -"

TIMEOUT = 10

class DS4():

    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.__axis = {}
        self.__button = {}
        self.__hat = {}
        self.__axisPrev = {}
        self.__buttonPrev = {}
        self.__hatPrev = {}
        self.__lastMoveTime = 0
        self.__connect()

    def __connect(self):
        print(PREFIX,"Connecting controller...")
        if pygame.joystick.get_init():
            pygame.joystick.quit()
        pygame.joystick.init()
        while pygame.joystick.get_count() < 1:
            pygame.joystick.quit()
            pygame.joystick.init()
            print(PREFIX,"Please connect controller")
        print(PREFIX,"Controller connected")
        self.__controller = pygame.joystick.Joystick(0)
        self.__controller.init()
        for i in range(self.__controller.get_numaxes()):
            self.__axis[i] = 0.0
            self.__axisPrev[i] = self.__axis[i]
        # Buttons are initialized to False
        for i in range(self.__controller.get_numbuttons()):
            self.__button[i] = False
            self.__buttonPrev[i] = self.__button[i]
        # Hats are initialized to 0
        for i in range(self.__controller.get_numhats()):
            self.__hat[i] = (0, 0)
            self.__hatPrev[i] = self.__hat[i]
        self.__lastMoveTime = time.time()

    def __reconnect(self):
        print(PREFIX,"Reconnecting controller...")
        if pygame.joystick.get_init():
            pygame.joystick.quit()
        pygame.joystick.init()
        while pygame.joystick.get_count() < 1:
            pygame.joystick.quit()
            pygame.joystick.init()
            print(PREFIX,"Please reconnect controller")
        print(PREFIX,"Controller reconnected")
        self.__controller = pygame.joystick.Joystick(0)
        self.__controller.init()

    ## Check is the current input is the same the previous input
    def __isSameInput(self):
        if not self.__axis == self.__axisPrev:
            print(self.__axis, self.__axisPrev)
            return False
        if not self.__button == self.__buttonPrev:
            print(self.__button, self.__buttonPrev)
            return False
        if not self.__hat == self.__hatPrev:
            return False
        return True

    def __checkDisconnect(self):
        #if not self.__isSameInput():
        #    self.__lastMoveTime = time.time()
        #print(time.time() - self.__lastMoveTime)
        if time.time() - self.__lastMoveTime > TIMEOUT:
            self.__lastMoveTime = time.time()
            self.__reconnect()
    
    def loadInputs(self):
        if pygame.joystick.get_init():
            if pygame.joystick.get_count() > 0:
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        self.__axisPrev[event.axis] = self.__axis[event.axis]
                        self.__axis[event.axis] = round(event.value,3)
                    elif event.type == pygame.JOYBUTTONDOWN:
                        self.__buttonPrev[event.button] = self.__button[event.button]
                        self.__button[event.button] = True
                    elif event.type == pygame.JOYBUTTONUP:
                        self.__buttonPrev[event.button] = self.__button[event.button]
                        self.__button[event.button] = False
                    elif event.type == pygame.JOYHATMOTION:
                        self.__hatPrev[event.hat] = self.__hat[event.hat]
                        self.__hat[event.hat] = event.value
                self.__checkDisconnect()
            else:
                self.__reconnect()
        else:
            self.__reconnect()

    def getAxis(self):
        return self.__axis

    def getAxisAt(self, index):
        return self.__axis.get(index)

    def getButtons(self):
        return self.__buttons

    def getButton(self, index):
        return self.__buttons.get(index)

    def getHat(self):
        return self.__hat







