from PIL import Image
from numpy import *
from scipy.ndimage import filters

"""
    Gaussian blurring or a Gassian filter is used to define an image
    to work in (for interpolation) for computing interest points
"""
# im = array(Image.open('data/empire.jpg').convert('L'))
# im2 = filters.gaussian_filter(im,10)


im = array(image.open('data/empire.jpg'))
im2 = zeros (im.shape)
for i in range(3):
    # to blur color images simply apply Gaussian blurring to each color channel
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2) #not needed
im2 = array(im2,'uint8')


pil_im = Image.fromarray(im)
pil_im2 = Image.fromarray(im2)

pil_im.show()
pil_im2.show()
