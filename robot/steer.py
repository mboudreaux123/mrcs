
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

class Steer():

    def __init__(self):
        self.__MIN_ANGLE = 0
        self.__MAX_ANGLE = 180
        self.__LOWER_LIMIT = self.__MIN_ANGLE + 40 # Cant be lower than MIN_ANGLE
        self.__UPPER_LIMIT = self.__MAX_ANGLE - 40 # Cant be higher than MAX_ANGLE
        self.__MID_ANGLE = ((self.__MAX_ANGLE - self.__MIN_ANGLE) / 2) + self.__MIN_ANGLE
        self.__i2c_bus = busio.I2C(SCL, SDA)
        self.__pca = PCA9685(self.__i2c_bus)
        self.__pca.frequency = 50
        self.__steerServo = servo.Servo(self.__pca.channels[0])
        self.__currentAngle = self.__MID_ANGLE
        self.__prevAngle = 0
        self.turn(self.__currentAngle)

    def destroy(self):
        self.__pca.deinit()

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
        self.__steerServo.angle = self.__currentAngle

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
