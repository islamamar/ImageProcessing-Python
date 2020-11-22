import ImageProcessing as IP
from PIL import Image

img = Image.open("C:/Users/islamAmar/Desktop/angular/lena.png")
gray_im= IP.gray_level_image(img)
path="C:/Users/islamAmar/PycharmProjects/pythonProject/images"
IP.thumbnails_image(path)
histogram= IP.Histogram_Computation(gray_im)

print("Image 10-bin image histogram : as  horizontal list ")
print(histogram)
print("Image 10-bin image histogram : as vertical element")
for i in range(0,len(histogram)):
		print("Histogram[",i,"]: ", histogram[i])