import numpy as np
from PIL import Image

def mirror(file_name):
    i=0
    while i==0:
        print("please enter flipping percentage <=50: ")
        percent=int(input())
        if percent>50:
            print('ERROR \n please enter number <=50:')
        else:
            break

    image1 = Image.open(file_name)
    image2 = image1.convert('L')
    gr_data = np.array(image2)
    p=percent*0.01

    while i==0:
        key=input("please enter v for vertical mirror, or h for horizontal mirror: ")
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
def threshold(image):
    """Input ins an image i.e. "testimage.jpg" or similar"""
    # opening  image
    im=np.array(Image.open(image).convert("L"))
    # split the image into individual bands
    # set color parameter L to
    # asking user input for number to change pixels to
    choice=int(input("please enter a number for threshold value: "))
    for i in range(im.shape[0]):
        for ii in range(im.shape[1]):
            if im[i][ii]<=choice:
                im[i][ii]=0
            else:
                im[i][ii]=255
    return im
def show_image(modified_array):
    return Image.fromarray(modified_array).show()

def FileSavings (im_mirror, im_threshold):
    while True:
        save=str(input("please enter 'save' or 'nosave' the augmented images: "))
        if save=='save':
            save_mir= Image.fromarray(im_mirror).save('reflection.jpg')
            save_thr= Image.fromarray(im_threshold).save('threshold.jpg')
            print("Augmented images were saved 'reflection.jpg' and 'threshold.jpg' in the directory")
            exit()
        elif save=='nosave':
            print("Files were not saved.")
            exit()
        else:
            print("input unrecognized, try again")
if __name__ == "__main__":
    userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
    while userinput!='q':
        if userinput=='R':
            R=mirror("testimage.jpg")
            show_image(R)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='T':
            T=threshold("testimage.jpg")
            show_image(T)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='S':
            S=FileSavings("testimage.jpg")
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='q':
            exit()
        else:
            userinput=input("Please type  R for Reflection or T for Threshold or S for Saving file: ")
    # im_mir=mirror('lenna_colour.jpg')
    # show_image(im_mir)
    # im_thr=threshold('lenna_colour.jpg')
    # save=FileSavings(im_mir,im_thr)
