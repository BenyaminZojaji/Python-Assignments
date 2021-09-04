from os import listdir
from imageio import imread, mimsave 
myPics=listdir('pictures')
images=[]
for name in myPics:
    images.append(imread('pictures/'+name))
mimsave('penSpinner.gif', images)
