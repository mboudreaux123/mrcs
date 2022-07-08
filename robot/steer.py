import Adafruit_PCA9685, fn
from colorama import *

PREFIX = "[" + Fore.GREEN + "steer" + Style.RESET_ALL + "] -"

class Steer():

    def __init__(self):

        self.__LOWER_LIMIT = 140 # Cant be lower than MIN_ANGLE
        self.__UPPER_LIMIT = 520 # Cant be higher than MAX_ANGLE
        self.__MIN_ANGLE = 100
        self.__MAX_ANGLE = 560
        self.__MID_ANGLE = ((self.__MAX_ANGLE - self.__MIN_ANGLE) / 2) + self.__MIN_ANGLE
        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(50)
        self.__currentAngle = self.__MID_ANGLE
        self.__prevAngle = 0
        self.turn(self.__currentAngle)

    def turn(self, angle):

        # Ensure angle is a integer
        self.__currentAngle = int(angle)

        ## Check boundaries of angle
        if self.__currentAngle < self.__MIN_ANGLE:
            if self.__currentAngle < self.__LOWER_LIMIT:
                self.__currentAngle = self.__LOWER_LIMIT
        elif self.__currentAngle > self.__MAX_ANGLE:
            if self.__currentAngle > self.__UPPER_LIMIT:
                self.__currentAngle = self.__UPPER_LIMIT

        ## Set servo to current angle
        self.__pwm.set_pwm(0, 0, self.__currentAngle)

        ## Set previous angle as 
        if not self.__currentAngle == self.__prevAngle:
            self.__prevAngle = self.__currentAngle

    def getLowerLimit(self):
        return self.__LOWER_LIMIT

    def getUpperLimit(self):
        return self.__UPPER_LIMIT

    def getMinAngle(self):
        return self.__MIN_ANGLE

    def getMidAngle(self):
        return self.__MID_ANGLE
    
    def getMaxAngle(self):
        return self.__MAX_ANGLE

    def getCurrentAngle(self):
        return self.__currentAngle

    def getPreviousAngle(self):
        return self.__prevAngle
