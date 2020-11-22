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
# Computing a 10-bin histogram of an image (consider only grey level images)

def Histogram_Computation(img):
    ten_bins = np.zeros([10], np.int32)
    size = img.size
    Image_Height = size[0]
    Image_Width = size[1]
    sum = 0
    Histogram = np.zeros([256], np.int32)
    for x in range(0, Image_Height):
        for y in range(0, Image_Width):
            Histogram[img.getpixel((x, y))] += 1

    for i in range(0, 256):
        if (i % 25 != 0 or i == 0):
            sum = sum + Histogram[i]
        else:
            index = i // 25
            # print(index)
            ten_bins[index - 1] = sum
            sum = Histogram[i]

        if (i == 255):
            ten_bins[index - 1] = ten_bins[index - 1] + sum
    # print(ten_bins)
    # print(sum)
    # print(Histogram)
    return ten_bins