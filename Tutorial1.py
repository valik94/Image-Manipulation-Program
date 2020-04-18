# #Tutorial1
# #import numpy and Pillow library
import numpy as np
from PIL import Image

def Threshold(image):
    """Input ins an image i.e. "lenna_colour.jpg" or similar"""
    #opening  image
    im=Image.open("lenna_colour.jpg").convert("L")
    # split the image into individual bands
    source = im.split()
    #set color parameter L to 
    L = 0
    #asking user input for number to change pixels to
    choice=int(input("please enter a number for pixels: "))
    if choice>255: #if input>255 change pixels array to 255
        imout = im.point(lambda i: 255)
    elif 0<=choice<=255:    #if input<=255 change pixels array to 0
        imout=im.point(lambda i: 0)
    else:   #input was wrong
        print("you chose the wrong number restart.")

    im_arr=np.array(imout)
    print(im_arr)
    print(im_arr.shape)
    imout.show()
    #returning modified array of image
    return im_arr

def FileSavings (image_arr):
    while True:
        save=str(input("please enter 'save' or 'nosave' the augmented image: "))
        if save=='save':
            save_im= Image.fromarray(image_arr).save('lenna_colourAugmented.jpg')
            print("file was saved as 'lenna_colourAugmented.jpg' in the directory")
            return False
        elif save=='nosave':
            print("File was not saved.")
            exit()
        else:
            print("input unrecognized, try again")
            

image_arr=Threshold("lenna_colour.jpg")
print(image_arr)
filesaved=FileSavings(image_arr)
print(filesaved)
