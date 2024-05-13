import twophase.solver as sv
import keyboard
from StringMove import moveString
from getRubiksColorAvg import getColors
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

svSolution = sv.solve(checkeredCubeString,20,0)

print("Cube State:", colorstring)
print("svSolution:", svSolution)

svSolution = svSolution.split(' ')
exSolution = ''

for i in svSolution:
    if i == 'U1':
        exSolution += 'U'
    elif i == 'U2':
        exSolution += "UU"
    elif i == 'U1':
        exSolution += 'u'#lowerCase
    
print("solution:", solution)
#executeSolution(solution)
#make the robot do the stuff
