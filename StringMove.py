#!/usr/bin/env python3
import time
import random
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import keyboard

kit1 = MotorKit(i2c=board.I2C())
kit2 = MotorKit(i2c=board.I2C(), address=0x61)
kit3 = MotorKit(i2c=board.I2C(), address=0x62)

def moveString(string):
    for char in string:
        move(char)
        time.sleep(0)
        
        kit1.stepper1.release()
        kit1.stepper2.release()
        kit2.stepper1.release()
        kit2.stepper2.release()
        kit3.stepper1.release()
        kit3.stepper2.release()
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
    random_string = generate_random_string(options, string_length)
    print("Random string:", random_string)

#moveString("ffrrllbbdduu")
    #moveString("LFLRD")#drlfl
#     moveString("drlfl")#drlfl
    moveString("UUDDBBFFLLRR")#drlfl

if __name__ == "__main__":
    main()
    
kit1.stepper1.release()
kit1.stepper2.release()
kit2.stepper1.release()
kit2.stepper2.release()
kit3.stepper1.release()
kit3.stepper2.release()

