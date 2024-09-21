#!/usr/bin/env python3
import time
import random
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import keyboard

# Three motor controller hats on the Raspberry Pi
kit1 = MotorKit(i2c=board.I2C())
kit2 = MotorKit(i2c=board.I2C(), address=0x61)
kit3 = MotorKit(i2c=board.I2C(), address=0x62)

# Function will iterate through a string of characters to move that face. 
def moveString(string):
    for char in string:
        move(char)
        time.sleep(0)
        
        releaseMotors()

'''
    There are 12 different ways in which to turn the cube, clockwise on 1 of 6 faces, 
    or counterclockwise on 1 of the same 6 faces.

    The letter corresponds to the face name, Up, Down, Right, Left, Front, Back.
    Capitilization refers to rotation direction. A captiol means clockwise, and a lowercase means counter clockwise.

'''
 # there is probably a more efficient way to write this if statement, area for improvment in later releases
def move(char):
    if char =='U':
        for i in range(51):
            kit1.stepper2.onestep(style=stepper.DOUBLE)
        kit1.stepper2.release()
    if char =='D':
        for i in range(51):
            kit1.stepper1.onestep(style=stepper.DOUBLE)
        kit1.stepper1.release() 
    if char =='R':
        for i in range(51):
            kit2.stepper1.onestep(style=stepper.DOUBLE)
        kit2.stepper1.release()
    if char =='L':
        for i in range(51):
            kit2.stepper2.onestep(style=stepper.DOUBLE)
        kit2.stepper2.release()                                                                                                                                                                                                                                                                                                                                                                                                                                         
    if char =='F':
        for i in range(51):
            kit3.stepper2.onestep(style=stepper.DOUBLE)
        kit3.stepper2.release()
    if char =='B':
        for i in range(51):
            kit3.stepper1.onestep(style=stepper.DOUBLE)
        kit3.stepper1.release()
    if char =='u':
        for i in range(51):
            kit1.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit1.stepper2.release()
    if char =='d':
        for i in range(51):
            kit1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit1.stepper1.release() 
    if char =='r':
        for i in range(51):
            kit2.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit2.stepper1.release()
    if char =='l':
        for i in range(51):
            kit2.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit2.stepper2.release()                                                                                                                                                                                                                                                                                                                                                                                                                                         
    if char =='f':
        for i in range(51):
            kit3.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit3.stepper2.release()
    if char =='b':
        for i in range(51):
            kit3.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        kit3.stepper1.release()
    time.sleep(0)

def generate_random_string(options, length):
    return ''.join(random.choice(options) for i in range(length))

def main():
    # Start a listener to monitor key presses
    options = ['R', 'L', 'B', 'D', 'U', 'F', 'u', 'd', 'l', 'r', 'b', 'f']  # Define the set of letters to choose from
    string_length = 20  # Specify the length of the random string

    # Generate a random set of moves to be executed on the cube. 
    random_string = generate_random_string(options, string_length)
    print("Random string:", random_string)

    # moveString(random_string)

    # moveString("ffrrllbbdduu")
    # moveString("LFLRD")#drlfl
    # moveString("drlfl")#drlfl
    moveString("UUDDBBFFLLRR")#drlfl

if __name__ == "__main__":
    main()

# Releasing all the motors is very important. 
# If you find that a motor is getting hot it is because you are not reaching this line of code.

def releaseMotors():
    kit1.stepper1.release()
    kit1.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()
    kit3.stepper1.release()
    kit3.stepper2.release()

# always good to gve this function a call.
releaseMotors()

