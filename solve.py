from PIL import Image, ImageColor, ImageDraw, ImageFont
import twophase.solver as sv
import keyboard
from StringMove import moveString
from getRubiksColor import getColors, calibrate
from camera import captureCube

colors = {  
                "white" : (255,255,255),
                "red"    : (255, 0, 0),
                "blue" : (0, 0,255),
                "green"   : (0,255,0),
                #"orange"  : (255,134,0),
                "black"   : (0,0,0),
                "yellow"  : (139,168,63),
          }


p1=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

p1[0] = (190,455) #U1
p1[1] = (285,333) #U2
p1[2] = (395,83) #U3
p1[3] = (290,763) #U4
#U5 /p1[4] WHITE BY DEFAULT
p1[5] = (540,300) #U6
p1[6] = (430,1014) #U7
p1[7] = (550,822) #U8
p1[8] = (698,580) #U9
    
p1[9] = (914,415) #R1
p1[10] = (748,175) #R2
p1[11] = (650,20) #R3
p1[12] = (1163,424) #R4
#R5/p1[13] RED BY DEFAULT
p1[14] = (830,40) #R6
p1[15] = (1335,450) #R7
p1[16] = (1160,253) #R8
p1[17] = (980,90) #R9
    
p1[18] = (630,1108) #F1
p1[19] = (740,930) #F2
p1[20] = (917,706) #F3
p1[21] = (844,1059) #F4
#F5/22 Green by default
p1[23] = (1160,670) #F6
p1[24] = (970,1020) #F7
p1[25] = (1190,830) #F8
p1[26] = (1332,654) #F9


#ANgle 2
p2=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    
p2[0] = (310,1010) #D1
p2[1] = (207,770) #D2
p2[2] = (124,635) #D3
p2[3] = (445,829) #D4
#D5 /p2[4] YELLOW BY DEFAULT
p2[5] = (222,335) #D6
p2[6] = (597,553) #D7
p2[7] = (454,304) #D8
p2[8] = (330,100) #D9
    
p2[9] = (1233,652) #L1
p2[10] = (1130,827) #L2
p2[11] = (899, 1040) #L3
p2[12] = (1077,640) #L4
#L5/p2[13] Orange BY DEFAULT
p2[14] = (733,1072) #L6
p2[15] = (861,633) #L7
p2[16] = (648,938) #L8
p2[17] = (500,1110) #L9
    
p2[18] = (890,75) #B1
p2[19] = (1108,290) #B2
p2[20] = (1252,458) #B3
p2[21] = (760,20) #B4
#B5/22 Blue by default
p2[23] = (1073,454) #B6
p2[24] = (560,2) #B7
p2[25] = (660,173) #B8
p2[26] = (824,436) #B9



calibration_file = "calibrateAngle1.png"
im = Image.open(calibration_file)

    #calibrate the colors based on the solved cube image
colors["white"] = calibrate(im, "white",p1, 0,9)
colors["red"]   = calibrate(im, "red",p1, 9,18)
colors["green"] = calibrate(im, "green",p1, 18,27)

calibration_file = "calibrateAngle2.png"
im = Image.open(calibration_file)
colors["black"] = calibrate(im, "black",p2, 9,17)
colors["blue"]   = calibrate(im, "blue",p2, 18,27)
colors["yellow"] = calibrate(im, "yellow",p2, 0,9)

print("calibrated colors:", colors)

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
colorString = getColors(file1,file2, p1, p2, colors)

#convert the colors to the cubestring
#A cube is defined by its cube definition string.
#A solved cube has the string 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'.

solvedCubeString    = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
checkeredCubeString = 'UDUDUDUDURLRLRLRLRFBFBFBFBFDUDUDUDUDLRLRLRLRLBFBFBFBFB'
randomCubeString    = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'

svSolution = sv.solve(colorString,20,0)

print("Cube State:", colorString)
print("svSolution:", svSolution)

svSolution = svSolution.split(' ')
exSolution = ''

for i in svSolution:
    if i == 'U1':
        exSolution += 'U'
    elif i == 'U2':
        exSolution += "UU"
    elif i == 'U3':
        exSolution += 'u'#lowerCase
    elif i == 'R1':
        exSolution += 'R'
    elif i == 'R2':
        exSolution += "RR"
    elif i == 'R3':
        exSolution += 'r'#lowerCase
    elif i == 'F1':
        exSolution += 'F'
    elif i == 'F2':
        exSolution += "FF"
    elif i == 'F3':
        exSolution += 'f'#lowerCase
    elif i == 'D1':
        exSolution += 'D'
    elif i == 'D2':
        exSolution += "DD"
    elif i == 'D3':
        exSolution += 'd'#lowerCase
    elif i == 'L1':
        exSolution += 'L'
    elif i == 'L2':
        exSolution += "LL"
    elif i == 'L3':
        exSolution += 'l'#lowerCase
    elif i == 'B1':
        exSolution += 'B'
    elif i == 'B2':
        exSolution += "BB"
    elif i == 'B3':
        exSolution += 'b'#lowerCase
    
print("exSolution:", exSolution)
moveString(exSolution)
#make the robot do the stuff
