#Assignment Tutorial
# from PIL import Image
# im=Image.open("lenna_colour.jpg")
# print(im.format, im.size, im.mode)


# import os, sys
# from PIL import Image

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert", infile)

# import os, sys
# from PIL import Image

# size = (128, 128)

# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#         except OSError:
#             print("cannot create thumbnail for", infile)

# import sys
# from PIL import Image

# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile, im.format, "%dx%d" % im.size, im.mode)
#     except OSError:
#         pass
# box = (0, 0, 500, 500)
# region = im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)


# def roll(image, delta):
#     """Roll an image sideways."""
#     xsize, ysize = image.size

#     delta = delta % xsize
#     if delta == 0: return image

#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     image.paste(part1, (xsize-delta, 0, xsize, ysize))
#     image.paste(part2, (0, 0, xsize-delta, ysize))

#     return image

# print(roll("lenna_colour.jpg",500))
# im.show(roll(im, 500))

# r, g, b = im.split()
# im = Image.merge("RGB", (b, g, r))

# out = im.resize((128, 128))
# out.show(im)
# out = im.rotate(45) # degrees counter-clockwise
# out.show(im)

# out = im.transpose(Image.FLIP_LEFT_RIGHT)
# #out.show(im)
# out = im.transpose(Image.FLIP_TOP_BOTTOM)
# #out.show(im)
# out = im.transpose(Image.ROTATE_90)
# # out.show(im)
# out = im.transpose(Image.ROTATE_180)
# # out.show(im)
# out = im.transpose(Image.ROTATE_270)
# #out.show(im)

# from PIL import Image
# from PIL import ImageFilter

# with Image.open("lenna_colour.jpg") as im:
    #  im = im.convert("L")
# out = im.filter(ImageFilter.DETAIL)
# out.show(im)
# out = im.point(lambda i: i * 2.5)
# out.show(im)



# from PIL import Image
# im=Image.open("lenna_colour.jpg")
# # split the image into individual bands
# source = im.split()

# R, G, B = 0, 1, 2

# # select regions where red is less than 100
# mask = source[R].point(lambda i: i < 100 and 255)
# # mask.show()
# # process the green band
# out = source[G].point(lambda i: i * 0.7)
# # out.show()
# # paste the processed band back, but only where red was < 100
# source[G].paste(out, None, mask)
# # mask.show()
# # build a new multiband image
# im = Image.merge(im.mode, source)
# # im.show()

# imout = im.point(lambda i: 254 and 255)
# # imout.show()


# from PIL import Image
# from numpy import asarray
# # load the image
# image = Image.open('lenna_colour.jpg')
# # convert image to numpy array
# data = asarray(image)
# print(type(data))
# # summarize shape
# print(data.shape)
# # image.show()

# # create Pillow image
# image2 = Image.fromarray(data)
# print(type(image2))
# # image2.show()
# # summarize image details
# print(image2.mode)
# print(image2.size)
# print(data)

# import numpy as np
# from PIL import Image

# #input is integer
# i=int(input("Please enter a pixel value for image:"))
# #im= convert PIL img into NumPy Array then open image (fileanme) and convert to 'L' color
# im = Image.open('lenna_colour.jpg').convert('L') #you can pass multiple arguments in single line
# source=im.split()
# L=0
# mask=source[L].point(lambda i: i*0)
# #mask.show()
# out=source[L].point(lambda i: 255)
# out.show()
# source[L].paste(out,None,mask)
# im=Image.merge(im.mode,source)
# im.show()
# #print(im.shape)
# #print(out)
# # array=np.array(im)
# # print(array.shape)
# #print(type(im))
# #print(im)
# im_arr=np.array(im)
# print(im_arr)
#saves image in .png format
#gr_im= Image.fromarray(im_arr).save('lenna_colourB&W.jpg')


from PIL import Image
from numpy import asarray
import numpy as np
image = Image.open("lenna_colour.jpg").convert('L')
print(image.size)
#flip an image x or y axis
data = asarray(image)
print(type(data))
print(data)
new_data=np.flip(data,1)
#choice=int(input("what percent u wanna flip %= "))
#size (958,960)

oldwidth=958
oldheight=960
maxp=oldwidth-1 #957
newImage=image.size
for row in range(oldheight-50):
    for col in range(oldwidth):
        new_data=data[1:800,row:]
        # oldpixel=data.getPixel(maxp-col,row)
        # newImage.setPixel(col,row,oldpixel)
        #new_data=data[1:, 100:i]

# summarize shape
print(new_data.shape)
#new_data.show()
# create Pillow image
image2 = Image.fromarray(new_data).save("gr_lenna.png")
print(type(image2))
print(type(new_data))
print(new_data)
# summarize image details
# print(image2.mode)
# print(image2.size)
#print(data)








# def roll(image, delta):
#     """Roll an image sideways."""
#     image = Image.open("lenna_colour.jpg")
#     xsize, ysize = image.size
#     print(image.dtype)
#     print(image.shape)
#     delta = delta % xsize
#     if delta == 0: return image

#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     image.paste(part1, (xsize-delta, 0, xsize, ysize))
#     image.paste(part2, (0, 0, xsize-delta, ysize))

#     return image

# x=roll("lenna_colour.jpg",500)
# x.show()



# from cImage import*
# def horizentalFlip(oldimage):
#     myimagewindow = ImageWin("lenna_colour.jpg",958,960)
#     oldimage = FileImage("lenna_colour.jpg")
#     oldimage.draw(myimagewindow)
#     oldw = oldimage.getWidth()
#     oldh = oldimage.getHeight()

#     newImage = EmptyImage(oldw,oldh)

#     maxp = oldw - 1
#     for row in range(oldh):
#         for col in range(oldw):
#             oldpixel = oldimage.getPixel(maxp-col,row)
#             newImage.setPixel(col,row,oldpixel)
#     newImage.setPosition(oldw+1,0)
#     newImage.draw(myimagewindow)
#     myimagewindow.exitOnClick()