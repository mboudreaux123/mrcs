# Lesson 6 How to Control DC Motor
# https://adeept.com/learn/tutorial-252.html

import RPi.GPIO as GPIO, sys, fn

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18100

MIN_SPEED = 0
MAX_SPEED = 100

prevSpeed = 0

PREFIX = "[motor] -"

def stop():
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)
    
def init():
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    stop()
    try:
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass

def disable():
    stop()
    GPIO.cleanup()

def forward(speed):
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

def reverse(speed):
    # Left motor
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)
    pwm_B.start(100)
    pwm_B.ChangeDutyCycle(speed)
    # Right motor
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    pwm_A.start(0)
    pwm_A.ChangeDutyCycle(speed)

def drive(speed):
    global prevSpeed
    speed = int(speed)
    if not speed == prevSpeed:
        print(PREFIX, "Speed:", speed)
        fn.removeLastLine()
    if speed > 0:
        if speed > MAX_SPEED:
            speed = MAX_SPEED
        forward(speed)
    elif speed < 0:
        speed = -speed
        if speed < MIN_SPEED:
            speed = MIN_SPEED
        reverse(speed)
    else:
        stop()
    prevSpeed = speed
