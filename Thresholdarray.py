#Threshold
import numpy as np
from PIL import Image
def Threshold(image):
    """Input is an image i.e. "lenna_colour.jpg" or similar"""
    #opening  image
    im=Image.open("lenna_colour.jpg").convert("L")
    im_arr=np.array(im)
    #asking user input for number to change pixels to
    choice=int(input("please enter a threshold number for pixels between 0 and 255: "))

    im_arr[im_arr<=choice]=0
    im_arr[im_arr>choice]=255
    print(im_arr)
    #returning modified array of image
    return im_arr

res=Threshold("lenna_colour.jpg")
print(res)