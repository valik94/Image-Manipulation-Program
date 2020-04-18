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
        key=input("please enter 'v' for vertical mirror, or 'h' for horizontal mirror: ")
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
    im=np.array(Image.open(image).convert("L"))
    
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

def FileSavings (im_array, filename):
    while True:
        save=str(input(f"please enter 'save' to save augmented image {filename} or 'nosave' to not save image: "))
        if save=='save':
            save_mir= Image.fromarray(im_array).save(filename)
            print(f"Augmented image was saved as '{filename}' in the directory.")
            return False
        elif save=='nosave':
            print("image was not saved. Press 'q' to exit")
        elif save=='q':
            exit()
        else:
            print("input unrecognized, try again")
            
if __name__ == "__main__":
    
    im=Image.open("testimage.jpg")
    im.show()
    print(im.size, im.mode)
    conv_im=im.convert("L")
    im_arr=np.array(conv_im)
    #reflective_im_arr = np.full_like(im_arr, 0)
    #threshold_im_arr = np.full_like(im_arr, 0)
    reflective_im_arr=[]
    threshold_im_arr=[] 
    
    userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
    while userinput!='q':
        if userinput=='R':
            R=mirror("testimage.jpg")
            reflective_im_arr=R
            show_image(R)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        if userinput=='T':
            T=threshold("testimage.jpg")
            threshold_im_arr=T
            show_image(T)
            userinput=input("Please type 'R' for Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        if userinput=='S':
            if (reflective_im_arr!=[]):
                FileSavings(reflective_im_arr,"reflection.jpg")
            if (threshold_im_arr!=[]):
                FileSavings(threshold_im_arr,"threshold.jpg")
            elif(reflective_im_arr==[]) and (threshold_im_arr==[]) :
                userinput=input("Nothing was saved, Please type  R for Reflection or T for Threshold or q to exit: ")
        if userinput=='q':
            exit()


