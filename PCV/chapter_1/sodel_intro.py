from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('data/empire.jpg').convert('L'))

"""Sobel derivative filters"""
# Computes x and y dervative and gradient magnitudeusing Sobel filter

imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

pil_im = Image.fromarray(im)
pil_imx = Image.fromarray(imx)
pil_imy = Image.fromarray(imy)
pil_mag = Image.fromarray(magnitude)

pil_im.show()
pil_imx.show()
pil_imy.show()
pil_mag.show()

"""Gassian Filter"""
signma = 5 #standard deviation

imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma),(0,1), imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
