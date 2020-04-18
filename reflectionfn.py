import numpy as np
from PIL import Image 
# im_arr=np.array([[1,2,3,23,66],
#                  [4,5,6,56,78],
#                  [7,8,9,89,89],
#                  [10,11,12,13,90]])
im=Image.open("lenna_colour.jpg").convert("L")
im_arr=np.array(im)
print(im_arr)
print(im_arr.size)
print(im_arr.shape)
#print(len(im_arr))

# V - VERTICAL reflection across y-axis _rightside modified_
#arr(row,column) =a[i:,j:]

new_arr=im_arr[:,int(len(im_arr)*0.5):]
rev_new_arr=new_arr[::-1]
y=np.flip(rev_new_arr,None)
print(y.shape)
print(y)
resulty=np.concatenate((im_arr,y),1)

print(resulty)
save_im1= Image.fromarray(resulty).save('lenna_colourAugmented1.jpg')
print("file was saved as 'lenna_colourAugmented1.jpg' in the directory")

# H-HORIZONTAL reflection across x-axis _top modified_
x_arr=im_arr[:int(len(im_arr)*0.5), 0:]
x_new_arr=x_arr[::-1]
resultx=np.concatenate((x_new_arr,im_arr))
save_im2= Image.fromarray(resultx).save('lenna_colourAugmented2.jpg')
print("file was saved as 'lenna_colourAugmented2.jpg' in the directory")
print(resultx)        
perc=35.3
result=perc/100
print(f"result is {result}")