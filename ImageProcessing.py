from PIL import Image
import numpy as np
import glob, os
img = Image.open("C:/Users/islamAmar/Desktop/angular/lena.png")

 # function tha Converting an image into grey level
def gray_level_image(img):
    grey_img = img.convert("L")
    grey_img.show()
    return grey_img
# Creating thumbnails of all files in a directory (current directory)
def thumbnails_image(path):

    # creating  thumbnail for (JPEG) image  in current directory
    for infile in glob.glob(path+"/*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail((128,128))
        # im.show()
        im.save(file + "_thumbnail"+ ".JPEG")
    # creating  thumbnail for (PNG) image  in current directory
    for infile in glob.glob(path+"/*.png"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail((128,128))
        # im.show()
        im.save(file + "_thumbnail"+ ".PNG")
