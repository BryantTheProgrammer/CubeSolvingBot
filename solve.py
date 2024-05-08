import twophase.solver as sv
import keyboard
from getRubiksColor import getColors

#steveTest()

# make a menu to allow the user to start
input("please press enter to start")

# enter filename 1    
file1 = "Angle1.png"

# enter filename 2
file2 = "Angle2.png"

#use the getRubicsColor.py to get the colors
colorstring = getColors(file1,file2)

#convert the colors to the cubestring
#A cube is defined by its cube definition string.
#A solved cube has the string 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'.

solvedCubeString    = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
checkeredCubeString = 'UDUDUDUDURLRLRLRLRFBFBFBFBFDUDUDUDUDLRLRLRLRLBFBFBFBFB'
randomCubeString    = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'

solution = sv.solve(checkeredCubeString,20,0)

print("solution:", solution)

#make the robot do the stuff
