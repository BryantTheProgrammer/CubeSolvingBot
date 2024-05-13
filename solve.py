import twophase.solver as sv
import keyboard
from getRubiksColor import getColors
from camera import captureCube

#steveTest()

# make a menu to allow the user to start
#input("please press enter to start")
#123456789012345678901234567890123456789012345678901234567890

#UUUUUUUUULRLRRLLRRFFFFFFLFFFFFFDFFLLBBBBLBLLFURFLBLRFL
# enter filename 1    
file1 = "Angle1.png"

# enter filename 2
file2 = "Angle2.png"

captureCube(file1, file2)
#use the getRubicsColor.py to get the colors
colorstring = getColors(file1,file2)

#convert the colors to the cubestring
#A cube is defined by its cube definition string.
#A solved cube has the string 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'.

solvedCubeString    = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
checkeredCubeString = 'UDUDUDUDURLRLRLRLRFBFBFBFBFDUDUDUDUDLRLRLRLRLBFBFBFBFB'
randomCubeString    = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'

solution = sv.solve(colorstring,20,0)

print("Cube State:", colorstring)
print("solution:", solution)

#make the robot do the stuff
