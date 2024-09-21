from PIL import Image, ImageColor, ImageDraw, ImageFont
import numpy as np

def getPaletteColor(pal,code):
    return (pal[3*code],pal[3*code + 1],pal[3*code + 2])

'''
The classify() function below is taken from the following post, and modified to handle additional colors.
Post was by Jacob Ritchie on April 6, 2016
https://stackoverflow.com/questions/36439384/classifying-rgb-values-in-python

Collaborators
Steve Sheehy, 2024
Bryant Hayden, 2024
'''

def calibrate(im, color, p, p_start, p_end):
    print("calibrating", color)
    avgR = 0
    avgG = 0
    avgB = 0
    for idx, i in enumerate(p[p_start:p_end]):
        if idx == 4: 
            continue
        pix = im.getpixel(i)
        print("idx:",idx, color, " sample:",pix)
        avgR += pix[0]
        avgG += pix[1]
        avgB += pix[2]
    avgR = avgR // 8
    avgG = avgG // 8
    avgB = avgB // 8
    avgRGB = (avgR, avgG, avgB)
    print(color, "average pixel:",avgRGB)
    return avgRGB

def classify(rgb_tuple, colors):
    # eg. rgb_tuple = (2,44,300)

    # add as many colors as appropriate here, but for
    # the stated use case you just want to see if your
    # pixel is 'more red' or 'more green'
    '''  the original colors before May 13
    colors = {  
                "white" : (255,255,255),
                "red"    : (255, 0, 0),
                "blue" : (0, 0,255),
                "green"   : (0,255,0),
                "orange"  : (255,134,0),
                "yellow"  : (255,255,0),
              }
    '''

    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color

def steveTest():
    print("hello from steveTest")

def getColors(file1, file2, p1, p2, colors):

    ### The following code is a series debugging tools that will prove useful during code modifications

    #file1 = "2024_02_12_14_15_48.jpg"
    #print("opening file:",file1)
    #im = Image.open(file1)
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

    # First and second cube refer to the first cube angle and second cube angle each of which should contain 27 Cubies
    firstCube = list(halfCube)
    secondCube = list(halfCube)

    # the whole cube will be a combination of the first and second cube angles
    wholeCube = ''
    
    for idx, i in enumerate(p1):
        pix = im.getpixel(i)
        color = classify(pix, colors)
        draw.text(i,classify(pix, colors),(255,255,255),font=font)
        if(color == 'white'):
            firstCube[idx] = 'U'
        elif(color == 'blue'):
            firstCube[idx] = 'B'
        elif(color == 'red'):
            firstCube[idx] = 'R'
        elif(color == 'black'):
            firstCube[idx] = 'L'
        elif(color == 'yellow'):
            firstCube[idx] = 'D'
        elif(color == 'green'):
            firstCube[idx] = 'F'

    #setting the default colors of the centers as they can't change
    firstCube[4] = 'U'
    firstCube[13] = 'R'
    firstCube[22] = 'F'

    im.save("angle1markedSteve.jpg")
    im.show()
    
    im = Image.open(file2)
    draw = ImageDraw.Draw(im)



    for idx, i in enumerate(p2):
        print("idx:",idx)
        pix1 = im.getpixel(i)
        #print("i  :",i,"pix  :",pix1)

        p5i = (i[0]+5,i[1]+5)
        pixp5 = im.getpixel(p5i)
        #print("p5i:",p5i,"pixp5:",pixp5)

        p9i = (i[0]+9,i[1]+9)
        pixp9 = im.getpixel(p9i)
        #print("p9i:",p9i,"pixp9:",pixp9)

        avgp = ((pix1[0] + pixp5[0] + pixp9[0]) // 3,
                (pix1[1] + pixp5[1] + pixp9[1]) // 3,
                (pix1[2] + pixp5[2] + pixp9[2]) // 3)

        color = classify(avgp, colors)
        print("avgp:",avgp, "color:",color)

        draw.text(i,classify(avgp, colors),(255,255,255),font=font)
        if(color == 'white'):
            secondCube[idx] = 'U'
        elif(color == 'blue'):
            secondCube[idx] = 'B'
        elif(color == 'red'):
            secondCube[idx] = 'R'
        elif(color == 'black'):
            secondCube[idx] = 'L'
        elif(color == 'yellow'):
            secondCube[idx] = 'D'
        elif(color == 'green'):
            secondCube[idx] = 'F'
        print("===")
            
    secondCube[4] = 'D'
    secondCube[13] = 'L'
    secondCube[22] = 'B'

    im.save("angle2markedSteve.jpg")
    im.show()

    firstCube = "".join(firstCube)
    secondCube = "".join(secondCube)
    print('First Cube: ', firstCube)
    print('Second Cube: ', secondCube)
    
    wholeCube = firstCube + secondCube
    print('Whole Cube: ', wholeCube)
    
    return wholeCube


#test lines
#filename1 = "Angle1.png"
#filename2 = "Angle2.png"

#getColors(filename1,filename2, p1, p2)

