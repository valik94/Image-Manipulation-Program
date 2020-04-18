# #Tutorial1
# #import numpy and Pillow library
import numpy as np
from PIL import Image

def UserInput():
    userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
    while userinput!='q':
        if userinput=='R':
            R=Reflection("lenna_colour.jpg")
            return R
        elif userinput=='T':
            T=Threshold("lenna_colour.jpg")
            return T
        elif userinput=='S':
            S=FileSavings("lenna_colour.jpg")
            return S
        elif userinput=='q':
            exit()
        else:
            userinput=input("Please type  R for Reflection or T for Threshold or S for Saving file: ")
            
def Reflection(image_array,R_pct,R_dir):
    """Input is an image array i.e. "testimage.jpg", R_pct=reflection% R_dir=reflection axis (vertical or horizontal) or similar
        Output is the modified numpy array of the image """
    
    if R_dir=='v' and 0<R_pct<50:
        new_arr=im_arr[:,int(len(im_arr)*(R_pct/100)):]
        rev_new_arr=new_arr[::-1]
        y=np.flip(rev_new_arr,None)
        resulty=np.concatenate((im_arr,y),1)
        print(resulty)
        return resulty
    elif R_dir=='h' and 0<R_pct<50:
        x_arr=im_arr[:int(len(im_arr)*(R_pct/100)), 0:]
        x_new_arr=x_arr[::-1]
        resultx=np.concatenate((x_new_arr,im_arr))       
        print(resultx)
        return resultx
    else:
        print("Wrong input, please restart and try again")
        
def Threshold(image_array, choice):
    """Input is an image array i.e. "lenna_colour.jpg" or similar and choice of the threshold"""
    #opening  image

    image_array[image_array<=choice]=0
    image_array[image_array>choice]=255
    print(image_array)
    #returning modified array of image
    return image_array

def showImage(array):
    image_from_array=Image.fromarray(array)
    image_from_array.show()

def FileSavings (image_arr,filename):
    while True:
        save=str(input("please enter 'save' or 'nosave' the augmented image: "))
        if save=='save':
            save_im= Image.fromarray(image_arr).save(filename)
            print(f"file was saved as '{filename}' in the directory")
            return False
        elif save=='nosave':
            print("File was not saved.")
            exit()
        else:
            print("input unrecognized, try again")
            
if __name__ == "__main__":  

    im=Image.open("testimage.jpg")
    im.show()
    print(im.size, im.mode)
    conv_im=im.convert("L")
    im_arr=np.array(conv_im)
    reflective_im_arr=[]
    threshold_im_arr=[]
    userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
    
    while (userinput!='q'):
        if userinput=='R':
            reflection_pct=int(input("Please enter reflection percentage: %"))
            reflection_dir=str(input("Please enter reflection direction 'v' or 'h': "))                   
            reflective_im_arr=Reflection(im_arr,reflection_pct,reflection_dir)
            showImage(reflective_im_arr)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        if userinput=='T':
            choice=int(input("please enter a threshold number for pixels between 0 and 255: "))
            threshold_im_arr=Threshold(im_arr,choice)
            showImage(threshold_im_arr)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        if userinput=='S':
            if (reflective_im_arr!=[]):
                FileSavings(reflective_im_arr,"reflection.jpg")
            if (threshold_im_arr!=[]):
                FileSavings(threshold_im_arr,"threshold.jpg")
    exit()
