import numpy as np
from PIL import Image

def Reflection(im_arr,reflection_pct,reflection_dir):

    i=0
    while i==0:
        percent=reflection_pct
        if percent>50:
            print('ERROR \n please enter number <=50:')
        else:
            break

    gr_data = im_arr
    p=percent*0.01

    while i==0:
        key=reflection_dir
        if key=='v' or key=='h':
            break

    if key=='v':
        nn=gr_data.shape[0]
        n=int(round(nn*p,0))
        for i in range(1,n+1):
            x=n-i
            y=(n-1)+i
            gr_data[x]=gr_data[y]
    elif key=='h':
        nn=gr_data.shape[1]
        n=int(round(nn*p,0))
        gr_data=gr_data.T
        for i in range(1,n+1):
            x=n-i
            y=(n-1)+i
            gr_data[x]=gr_data[y]
        gr_data=gr_data.T
    else:
        return print('ERROR \nplease enter "v" for vertically, or "h" for horizontally')
    return gr_data

def Threshold(image_array, choice):
    """Input ins an image i.e. "image_array" and choice of threshold"""
    # opening  image
    im=image_array
    
    for i in range(im.shape[0]):
        for ii in range(im.shape[1]):
            if im[i][ii]<=choice:
                im[i][ii]=0
            else:
                im[i][ii]=255
    return im

def showImage(modified_array):
    return Image.fromarray(modified_array).show()

def FileSavings (im_array, filename):
    while True:
        save=str(input("please enter 'save' or 'nosave' the augmented images: "))
        if save=='save':
            filename=str(input("please enter file name: "))
            save_mir= Image.fromarray(im_array).save(f"{filename}.jpg")
            print(f"Augmented image was saved as '{filename}.jpg' in the directory.")
            exit()
        elif save=='nosave':
            print("Files were not saved.")
            exit()
        else:
            print("input unrecognized, try again")

if __name__ == "__main__":
    
    im=Image.open("testimage.jpg")
    im.show()
    print(im.size, im.mode)
    conv_im=im.convert("L")
    im_arr=np.array(conv_im)
    reflective_im_arr= []
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