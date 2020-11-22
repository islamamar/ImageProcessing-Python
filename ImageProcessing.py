from PIL import Image
import numpy as np
import glob, os
img = Image.open("C:/Users/islamAmar/Desktop/angular/lena.png")

 # function tha Converting an image into grey level
def gray_level_image(img):
    grey_img = img.convert("L")
    grey_img.show()
    return grey_img