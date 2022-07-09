import pygame
import os
import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import imutils

os.environ["DISPLAY"] = ":0"

#############################################################
#### PiCarPro GPIO Variables
# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

Dir_forward   = 0
Dir_backward  = 1

left_forward  = 1
left_backward = 0

right_forward = 0
right_backward= 1

pwn_A = 0
pwm_B = 0

#############################################################
#### Pygame variables




#############################################################
#### DS4 Variables
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


#############################################################
#### PiCarPro move functions
def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)

def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

#############################################################
####

# https://stackoverflow.com/questions/929103
def convert_range(OldMin, OldMax, NewMin, NewMax, OldValue):
    OldRange = (OldMax - OldMin)
    if OldRange == 0:
        NewValue = NewMin
    else:
        NewRange = (NewMax - NewMin)  
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

    return NewValue


def accelerate(l2, r2):
    OldMax = 1.0
    OldMin = -1.0
    NewMax = 100
    NewMin = 0

    l2 = convert_range(OldMin, OldMax, NewMin, NewMax, l2)
    r2 = convert_range(OldMin, OldMax, NewMin, NewMax, r2)
    speed = r2 - l2

    # Forward
    if speed > 0:
        # Left motor
        GPIO.output(Motor_B_Pin1, GPIO.HIGH)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        pwm_B.start(0)
        pwm_B.ChangeDutyCycle(speed)
        # Right motor
        GPIO.output(Motor_A_Pin1, GPIO.HIGH)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)
    # Reverse
    elif speed < 0:
        # Left motor
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.HIGH)
        pwm_B.start(100)
        pwm_B.ChangeDutyCycle(speed * -1)
        # Right motor
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.HIGH)
        pwm_A.start(0)
        pwm_A.ChangeDutyCycle(speed * -1)
    else:
        # Accelerate to stop (speed of zero)
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor_A_EN, GPIO.LOW)
        GPIO.output(Motor_B_EN, GPIO.LOW)

def turn(axis_x):
    axis_x = convert_range(-1.0, 1.0, 500, 160, axis_x)
    pwm.set_pwm(0, 0, int(axis_x))
    
def turn_head(axis_x, axis_y):
    # Change axis_x range
    axis_x = convert_range(-1.0, 1.0, 560, 100, axis_x)
    
    # Change axis_y range
    axis_y = convert_range(-1.0, 1.0, 560, 100, axis_y)
    
    if axis_y < 260:
        axis_y = 260
    
    pwm.set_pwm(1, 0, int(axis_x))
    pwm.set_pwm(2, 0, int(axis_y))
    

#############################################################
#### Main

if __name__ == '__main__':
    try:
        setup()
        
        pygame.init()
        pygame.joystick.init()

        controller = pygame.joystick.Joystick(0)
        controller.init()

        # Three types of controls: axis, button, and hat
        axis = {}
        button = {}
        hat = {}

        # Assign initial data values
        # Axes are initialized to 0.0
        for i in range(controller.get_numaxes()):
            axis[i] = 0.0
        # Buttons are initialized to False
        for i in range(controller.get_numbuttons()):
            button[i] = False
        # Hats are initialized to 0
        for i in range(controller.get_numhats()):
            hat[i] = (0, 0)

        # Setup 180 turn servo
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(50)

        quit = False
        while quit == False:

            # Get events
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    axis[event.axis] = round(event.value,3)
                elif event.type == pygame.JOYBUTTONDOWN:
                    button[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    button[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    hat[event.hat] = event.value

            quit = button[BUTTON_PS]

            accelerate(axis[AXIS_L2], axis[AXIS_R2])
            turn(axis[AXIS_LEFT_STICK_X])
            turn_head(axis[AXIS_RIGHT_STICK_X], axis[AXIS_RIGHT_STICK_Y])

            # Limited to 30 frames per second to make the display not so flashy
            clock = pygame.time.Clock()
            clock.tick(60)
    except KeyboardInterrupt:
        destroy()
