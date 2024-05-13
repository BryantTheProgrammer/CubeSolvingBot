from PIL import Image, ImageColor, ImageDraw, ImageFont
import numpy as np


def getPaletteColor(pal,code):
    return (pal[3*code],pal[3*code + 1],pal[3*code + 2])



'''
The classify() function below is taken from the following post, and modified to handle additional colors.
Post was by Jacob Ritchie on April 6, 2016
https://stackoverflow.com/questions/36439384/classifying-rgb-values-in-python

much code by Steve Sheehy, 2024
'''
def classify(rgb_tuple):
    # eg. rgb_tuple = (2,44,300)

    # add as many colors as appropriate here, but for
    # the stated use case you just want to see if your
    # pixel is 'more red' or 'more green'
    colors = {  
                "white" : (255,255,255),
                "red"    : (255, 0, 0),
                "blue" : (0, 0,255),
                "orange"  : (255,134,0),
                "green"   : (0,128,0),
                "yellow"  : (255,255,0),
              }

    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color

def steveTest():
    print("hello from steveTest")

def getColors(file1, file2):

    #file1 = "2024_02_12_14_15_48.jpg"
    #print("opening file:",file1)
    im = Image.open(file1)
    #print("Image mode   :",im.mode)
    #print("Image format :",im.format)
    #print("Image palette:",im.palette)
    #print("Image width  :",im.width)
    #print("Image height :",im.height)
    #print("Image info   :",im.info)
    #print("Image bands  :",im.getbands())
    #print("Colors used  :",im.getcolors())
    #print("palette      :",im.getpalette())
    #print("palette length:",len(im.getpalette()))
    #p = im.getpalette()
    #print("0: ",getPaletteColor(p,0))
    #print("1: ",getPaletteColor(p,1))
    #print("2: ",getPaletteColor(p,2))
    #print("3: ",getPaletteColor(p,3))
    #print("4: ",getPaletteColor(p,4))


    #im.show()

    '''
    You can open the image with Gimp or some other image editing program, then
    put your cursor at the location of the image, click, and then get the pixel
    coordinates from Gimp.

    This idea relies on the camera and the cube both being fixed and in the same location
    for every picture.  Then you can go to a single pixel, access the RGB values for that
    pixel, and then convert them to a discrete set of colors.

    Each of the 8 individual surfaces (excluding the middle one since it doesn't change)
    can be accessed using code like below.

    '''

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 16)
    #draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    halfCube = ' ' * 27
    firstCube = list(halfCube)
    secondCube = list(halfCube)
    wholeCube = ''
    
    p1=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    p1[0] = (203,455) #U1
    p1[1] = (285,333) #U2
    p1[2] = (395,83) #U3
    p1[3] = (290,763) #U4
    #U5 /p1[4] WHITE BY DEFAULT
    
    p1[5] = (540,300) #U6
    p1[6] = (430,1014) #U7
    p1[7] = (550,822) #U8
    p1[8] = (698,580) #U9
    
    p1[9] = (914,415) #R1
    p1[10] = (748,155) #R2
    p1[11] = (640,5) #R3
    p1[12] = (1163,424) #R4
    #R5/p1[13] RED BY DEFAULT

    p1[14] = (830,24) #R6
    p1[15] = (1335,434) #R7
    p1[16] = (1187,253) #R8
    p1[17] = (990,52) #R9
    
    p1[18] = (630,1108) #F1
    p1[19] = (760,930) #F2
    p1[20] = (917,706) #F3
    p1[21] = (844,1039) #F4
     #F5/22 Green by default

    p1[23] = (1160,670) #F6
    p1[24] = (986,998) #F7
    p1[25] = (1184,812) #F8
    p1[26] = (1332,654) #F9
    
    for idx, i in enumerate(p1):
        pix = im.getpixel(i)
        color = classify(pix)
        draw.text(i,classify(pix),(255,255,255),font=font)
        if(color == 'white'):
            firstCube[idx] = 'U'
        elif(color == 'blue'):
            firstCube[idx] = 'B'
        elif(color == 'red'):
            firstCube[idx] = 'R'
        elif(color == 'orange'):
            firstCube[idx] = 'L'
        elif(color == 'yellow'):
            firstCube[idx] = 'D'
        elif(color == 'green'):
            firstCube[idx] = 'F'

    firstCube[4] = 'U'
    firstCube[13] = 'R'
    firstCube[22] = 'F'

    im.save("angle1marked.jpg")
    
    im = Image.open(file2)
    draw = ImageDraw.Draw(im)

    #ANgle 2
    p2=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
       (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    
    p2[0] = (296,940) #D1
    p2[1] = (210,694) #D2
    p2[2] = (134,572) #D3
    p2[3] = (462,762) #D4
    #D5 /p2[4] YELLOW BY DEFAULT
    p2[5] = (218,301) #D6
    p2[6] = (627,498) #D7
    p2[7] = (463,236) #D8
    p2[8] = (330,54) #D9
    
    p2[9] = (1253,652) #L1
    p2[10] = (1093,827) #L2
    p2[11] = (899, 1015) #L3
    p2[12] = (1077,640) #L4
    #L5/p2[13] RED BY DEFAULT

    p2[14] = (733,1032) #L6
    p2[15] = (861,633) #L7
    p2[16] = (667,873) #L8
    p2[17] = (500,1070) #L9
    
    p2[18] = (919,34) #B1
    p2[19] = (1132,242) #B2
    p2[20] = (1263,409) #B3
    p2[21] = (783,1) #B4
     #B5/22 Green by default

    p2[23] = (1102,398) #B6
    p2[24] = (641,1) #B7
    p2[25] = (681,121) #B8
    p2[26] = (868,353) #B9
    for idx, i in enumerate(p2):
        pix = im.getpixel(i)
        color = classify(pix)
        draw.text(i,classify(pix),(255,255,255),font=font)
        if(color == 'white'):
            secondCube[idx] = 'U'
        elif(color == 'blue'):
            secondCube[idx] = 'B'
        elif(color == 'red'):
            secondCube[idx] = 'R'
        elif(color == 'orange'):
            secondCube[idx] = 'L'
        elif(color == 'yellow'):
            secondCube[idx] = 'D'
        elif(color == 'green'):
            secondCube[idx] = 'F'
            
    secondCube[4] = 'D'
    secondCube[13] = 'L'
    secondCube[22] = 'B'

    im.save("angle2marked.jpg")
    firstCube = "".join(firstCube)
    secondCube = "".join(secondCube)
    print('First Cube: ', firstCube)
    print('Second Cube: ', secondCube)
    
    wholeCube = firstCube + secondCube
    print('Whole Cube: ', wholeCube)
    
    return wholeCube


#test lines
#filename1 = "2024_02_12_14_15_48.jpg"
#filename2 = "2024_02_12_14_15_48.jpg"

#getColors(filename1,filename2)
'''
    The names of the facelet positions of the cube
                  |************|
                  |*U1**U2**U3*|
                  |************|
                  |*U4**U5**U6*|
                  |************|
                  |*U7**U8**U9*|
                  |************|
     |************|************|************|************|
     |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
     |************|************|************|************|
     |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
     |************|************|************|************|
     |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
     |************|************|************|************|
                  |************|
                  |*D1**D2**D3*|
                  |************|
                  |*D4**D5**D6*|
                  |************|
                  |*D7**D8**D9*|
                  |************|
    A cube definition string "UBL..." means for example: In position U1 we have the U-color, in position U2 we have the
    B-color, in position U3 we have the L color etc. according to the order U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2,
    R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4,
    L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9 of the enum constants.
'''