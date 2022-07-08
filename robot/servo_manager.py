import Adafruit_PCA9685
from colorama import *

WARN_PREFIX = "[" + Fore.YELLOW + "steer" + Style.RESET_ALL + "] -"
ERROR_PREFIX = "[" + Fore.RED + "steer" + Style.RESET_ALL + "] -"

class ServoManager():

    def __init__(self):

        self.__MIN_ANGLE = 100
        self.__MAX_ANGLE = 560
        self.__MID_ANGLE = ((self.__MAX_ANGLE - self.__MIN_ANGLE) / 2) + self.__MIN_ANGLE
        self.__servoList = []
        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(50)

    def registerServo(self, servoID, name, lowerLimit, upperLimit):

        # Check if servo with same ID already exists
        for servo in self.__servoList:
            if self.__servoList[servo]['id'] == servoID:
                print(ERROR_PREFIX, "Servo with ID:", servoID, "already exist!")
                return False

        # Check if lower and upper limits are within range
        if lowerLimit < self.__MIN_ANGLE:
            lowerLimit = self.__MIN_ANGLE
        elif lowerLimit > self.__MAX_ANGLE:
            lowerLimit = self.__MAX_ANGLE
        if upperLimit < self.__MIN_ANGLE:
            upperLimit = self.__MIN_ANGLE
        elif upperLimit > self.__MAX_ANGLE:
            upperLimit = self.__MAX_ANGLE

        # Append servo information to servo list
        self.__servoList.append(
            {
                'id': servoID,
                'name': name,
                'lowerLimit': 0,
                'upperLimit': 0,
                'currentAngle': self.__MID_ANGLE,
                'prevAngle': 0
            }
        )

        # Initial servo angle
        self.turn(servoID, self.__MID_ANGLE)

        return True

    # Get a servos index in the servo list by it's id
    def __getServoIndex(self, servoID):

        for servo in self.__servoList:
            if self.__servoList[servo]['id'] == servoID:
                return servo


    def turn(self, servoID, angle):

        index = self.__getServoIndex(servoID)

        # Ensure angle is a integer
        self.__servoList[index]['currentAngle'] = int(angle)

        ## Check boundaries of angle
        if self.__servoList[index]['currentAngle'] < self.__MIN_ANGLE:
            if self.__servoList[index]['currentAngle'] < self.__LOWER_LIMIT:
                self.__servoList[index]['currentAngle'] = self.__LOWER_LIMIT
        elif self.__servoList[index]['currentAngle'] > self.__MAX_ANGLE:
            if self.__servoList[index]['currentAngle'] > self.__UPPER_LIMIT:
                self.__servoList[index]['currentAngle'] = self.__UPPER_LIMIT

        ## Set servo to current angle
        self.__pwm.set_pwm(servoID, 0, self.__currentAngle)

        ## Set previous angle as 
        if not self.__servoList[index]['currentAngle'] == self.__servoList[index]['prevAngle']:
            self.__servoList[index]['prevAngle'] = self.__servoList[index]['currentAngle']




