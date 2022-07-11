from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from colorama import *

PREFIX = "[" + Fore.MAGENTA + "HEAD" + Style.RESET_ALL + "] -"

class Head():

    def __init__(self):
        self.__MIN_ANGLE_X = 0
        self.__MAX_ANGLE_X = 180
        self.__MIN_ANGLE_Y = 0
        self.__MAX_ANGLE_Y = 180
        self.__LOWER_LIMIT_X = self.__MIN_ANGLE_X + 0 # Cant be lower than MIN_ANGLE
        self.__UPPER_LIMIT_X = self.__MAX_ANGLE_X - 0 # Cant be higher than MAX_ANGLE
        self.__LOWER_LIMIT_Y = self.__MIN_ANGLE_Y + 0 # Cant be lower than MIN_ANGLE
        self.__UPPER_LIMIT_Y = self.__MAX_ANGLE_Y - 0 # Cant be higher than MAX_ANGLE
        self.__MID_ANGLE_X = ((self.__MAX_ANGLE_X - self.__MIN_ANGLE_X) / 2) + self.__MIN_ANGLE_X
        self.__MID_ANGLE_Y = ((self.__MAX_ANGLE_Y - self.__MIN_ANGLE_Y) / 2) + self.__MIN_ANGLE_Y

        self.__i2c_bus = busio.I2C(SCL, SDA)
        self.__pca = PCA9685(self.__i2c_bus)
        self.__pca.frequency = 50
        self.__headServoX = servo.Servo(self.__pca.channels[1])
        self.__headServoY = servo.Servo(self.__pca.channels[2])
        self.__currentAngleX = self.__MID_ANGLE_X
        self.__currentAngleY = self.__MID_ANGLE_Y
        self.__prevAngleX = 0
        self.__prevAngleY = 0
        self.turnX(self.__currentAngleX)
        self.turnY(self.__currentAngleY)

    def destroy(self):
        self.__pca.deinit()

    def turnX(self, angleX):

        ## Ensure angle is a integer
        self.__currentAngleX = int(angleX)

        ## Check boundaries of angleX
        if self.__currentAngleX < self.__LOWER_LIMIT_X:
            self.__currentAngleX = self.__LOWER_LIMIT_X
        elif self.__currentAngleX > self.__UPPER_LIMIT_X:
            self.__currentAngleX = self.__UPPER_LIMIT_X

        ## Set x angle
        self.__headServoX.angle = self.__currentAngleX
        self.__prevAngleX = self.__currentAngleX
    
    def turnY(self, angleY):

        ## Ensure angle is a integer
        self.__currentAngleY = int(angleY)

        ## Check boundaries of angleY
        if self.__currentAngleY < self.__LOWER_LIMIT_Y:
            self.__currentAngleY = self.__LOWER_LIMIT_Y
        elif self.__currentAngleY > self.__UPPER_LIMIT_Y:
            self.__currentAngleY = self.__UPPER_LIMIT_Y

        ## Set y angle
        self.__headServoY.angle = self.__currentAngleY
        self.__prevAngleY = self.__currentAngleY

    def getMinAngleX(self):
        return self.__MIN_ANGLE_X

    def getMidAngleX(self):
        return self.__MID_ANGLE_X
    
    def getMaxAngleX(self):
        return self.__MAX_ANGLE_X

    def getLowerLimitX(self):
        return self.__LOWER_LIMIT_X

    def getUpperLimitX(self):
        return self.__UPPER_LIMIT_X

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
    
    def getLowerLimitY(self):
        return self.__LOWER_LIMIT_Y

    def getUpperLimitY(self):
        return self.__UPPER_LIMIT_Y

    def getCurrentAngleY(self):
        return self.__currentAngleY

    def getPreviousAngleY(self):
        return self.__prevAngleY
