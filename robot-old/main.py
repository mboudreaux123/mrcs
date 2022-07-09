import pygame
import os, time
from colorama import *
import RPi.GPIO as GPIO, Adafruit_PCA9685
import ds4, motor, steer, head, fn, servo_manager

def border():

    print("#" * 90)

def intro():

    print("")
    border()
    print(" ________  ___  ________  ________  ________          ________  ________  ________     ")
    print("|\   __  \|\  \|\   ____\|\   __  \|\   __  \        |\   __  \|\   __  \|\   __  \    ")
    print("\ \  \|\  \ \  \ \  \___|\ \  \|\  \ \  \|\  \       \ \  \|\  \ \  \|\  \ \  \|\  \   ")
    print(" \ \   ____\ \  \ \  \    \ \   __  \ \   _  _\       \ \   ____\ \   _  _\ \  \\\\\  \  ")
    print("  \ \  \___|\ \  \ \  \____\ \  \ \  \ \  \\\\  \|       \ \  \___|\ \  \\\  \\\\ \  \\\\\  \ ")
    print("   \ \__\    \ \__\ \_______\ \__\ \__\ \__\\\\ _\        \ \__\    \ \__\\\ _\\\\ \_______\\\\")
    print("    \|__|     \|__|\|_______|\|__|\|__|\|__|\|__|        \|__|     \|__|\|__|\|_______|")
    print("")
    border()
    print("")

def terminated():

    print("")
    border()
    print("")
    print(Fore.RED + "Program terminated" + Style.RESET_ALL)
    print("")
    border()
    print("")

if __name__ == '__main__':

    try:

        fn.removeLastLine()
        fn.removeLastLine()
        intro()

        steer = steer.Steer()
        ds4 = ds4.DS4()

        while(True):
            number = fn.convertRange(-1.0, 1.0, steer.getMaxAngle(), steer.getMinAngle(), ds4.getAxisAt(0))
            print(number)
            steer.turn(fn.convertRange(number)
            
    except KeyboardInterrupt:
        terminated()

