#Importing path and skimage i/o library
import os.path
from skimage.io import imread
from skimage import data_dir
#reading the astronaut image
img = imread(os.path.join(data_dir,'astronaut.png'))
#Using matplotlib.pyplot to visualize the image
import matplotlib.pyplot as plt
print(plt.imshow(img))
print(img)
print('Type of image: ', type(img))
print('Dimensions of image: ', img.ndim)
print('Shape of image:', img.shape)
