import glob,os
from PIL import Image
from numpy import *
from pylab import *
import pca

path = "../../data/a_thumbs/"
os.chdir(path)

imlist = []

for file in glob.glob("*.jpg"):
    imlist.append(path+file)

im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[0:2] # get the size of the image
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
              for im in imlist], 'f')

# perform PCA
V,S,immean = pca.pca(immatrix)

# show some images (mean and 7 first modes)
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()

