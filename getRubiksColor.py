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
                "orange" : (255,127,0),
                "red"    : (255, 0, 0),
                "yellow" : (229,255,0),
                "green"  : (0,255,0),
                "blue"   : (0,0,255),
                "white"  : (255,255,255),
              }

    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color

def steveTest():
    print("hello from steveTest")

def getColors(file1, file2):

    #file1 = "2024_02_12_14_15_48.jpg"
    print("opening file:",file1)
    im = Image.open(file1)
    print("Image mode   :",im.mode)
    print("Image format :",im.format)
    print("Image palette:",im.palette)
    print("Image width  :",im.width)
    print("Image height :",im.height)
    #print("Image info   :",im.info)
    print("Image bands  :",im.getbands())
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

    print("Pixel colors for the 8 colors of each side. Sides are Left, Right, and Top")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 16)
    #draw.text((0, 0),"Sample Text",(255,255,255),font=font)

    print("UP side colors.")
    p=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    p[0] = (176,395) #U1
    p[1] = (271,317) #U2
    p[2] = (392,106) #U3
    p[3] = (263,771) #U4
    #U5 WHITE BY DEFAULT
    p[4] = (549,315) #U6
    p[5] = (340,973) #U7
    p[6] = (480,807) #U8
    p[7] = (634,614) #U9

    for i in p:
        pix = im.getpixel(i)
        print("\tpixel at:",i, "rgb color:", pix, classify(pix))
        draw.text(i,classify(pix),(255,255,255),font=font)
        classify(pix):
            case 'white':
                print('U')


    print("RIGHT side colors.")
    p=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    p[0] = (236,257) #R1
    p[1] = (310,293) #R2
    p[2] = (404,342) #R3
    p[3] = (254,343) #R4
    #R5 RED BY DEFAULT
    p[4] = (417,431) #R6
    p[5] = (253,385) #R7
    p[6] = (354,471) #R8
    p[7] = (420,506) #R9

    for i in p:
        pix = im.getpixel(i)
        print("\tpixel at:",i, "rgb color:", pix, classify(pix))
        draw.text(i,classify(pix),(255,0,0),font=font)


    print("FRONT side colors.")
    p=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    p[0] = (260,190) #F1
    p[1] = (334,231) #F2
    p[2] = (436,263) #F3
    p[3] = (332,144) #F4
     #F5 Green by default
    p[4] = (516,203) #F6
    p[5] = (357,107) #F7
    p[6] = (503,133) #F8
    p[7] = (588,152) #F9

    for i in p:
        pix = im.getpixel(i)
        print("\tpixel at:",i, "rgb color:", pix, classify(pix))
        draw.text(i,classify(pix),(0,255,0),font=font)


    im.show()
    im.save("steve.jpg")
    
    cube = 'UDUDUDUDURLRLRLRLRFBFBFBFBFDUDUDUDUDLRLRLRLRLBFBFBFBFB'
    return cube


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