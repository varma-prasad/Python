#Importing path and skimage i/o library
import os.path
from skimage.io import imread
from skimage import data_dir
import matplotlib.pyplot as plt
#reading the astronaut image
img = imread(os.path.join(data_dir,'astronaut.png'))

#slicing
img_slice=img.copy()
img_slice=img_slice[0:300,360:480]
print(plt.figure())
print(plt.imshow(img_slice))

#assigning values correspondingto sliced image
img[0:300,360:400,:]=0
print(plt.imshow(img))
#Using matplotlib.pyplot to visualize the image

