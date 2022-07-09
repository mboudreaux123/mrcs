import Adafruit_PCA9685
from colorama import *
import fn

X_LOWER_LIMIT = 100 # Default 100
X_UPPER_LIMIT = 560 # Default 560
Y_LOWER_LIMIT = 100 # Default 100
Y_UPPER_LIMIT = 560 # Default 560

PREFIX = "[" + Fore.YELLOW + "head" + Style.RESET_ALL + "] -"

class Head():

    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)
        self.prevAngleX = 0
        self.prevAngleY = 0

    def turnX(self, angleX):
        angleX = int(angleX)
        if not angleX == self.prevAngleX:
            print(PREFIX, "AngleX:", angleX)
            fn.removeLastLine()

        ## Check boundaries of angleX
        if angleX < X_LOWER_LIMIT:
            angleX = X_LOWER_LIMIT
        elif angleX > X_UPPER_LIMIT:
            angleX = X_UPPER_LIMIT

        ## Set x angle
        self.pwm.set_pwm(1, 0, int(angleX))
        self.prevAngleX = angleX

    def turnY(self, angleY):
        angleY = int(angleY)
        if not angleY == self.prevAngleY:
            print(PREFIX, "AngleY:", angleY)
            fn.removeLastLine()
            
        ## Check boundaries of angleY
        if angleY < Y_LOWER_LIMIT:
            angleY = Y_LOWER_LIMIT
        elif angleY > Y_UPPER_LIMIT:
            angleY = Y_UPPER_LIMIT

        ## Set y angle
        self.pwm.set_pwm(2, 0, int(angleY))
        self.prevAngleY = angleY

    def getLowerLimit(self):
        return self.__LOWER_LIMIT

    def getUpperLimit(self):
        return self.__UPPER_LIMIT





    def getMinAngleX(self):
        return self.__MIN_ANGLE_X

    def getMidAngleX(self):
        return self.__MID_ANGLE_X
    
    def getMaxAngleX(self):
        return self.__MAX_ANGLE_X

    def getCurrentAngleX(self):
        return self.__currentAngleX

    def getPreviousAngleX(self):
        return self.__prevAngleX







    def getMinAngleY(self):
        return self.__MIN_ANGLE_Y

    def getMidAngleY(self):
        return self.__MID_ANGLE_Y
    
    def getMaxAngleY(self):
        return self.__MAX_ANGLE_Y

    def getCurrentAngleY(self):
        return self.__currentAngleY

    def getPreviousAngleY(self):
        return self.__prevAngleY
