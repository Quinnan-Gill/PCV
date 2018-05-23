from PIL import Image
from pylab import *
from numpy import *
import os

def get_imlist(path):
    """ Returns a list of filenames for all jpg images in a directory. """

    return [os.path.join(path, f) for f in os.listdir(path) if.endswitch('.jpg')]

def imresize(im,sz):
    """ Resize an image array using PIL. """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

# Hisogram equalization: transform flattens the graylevel histogram
# of an image so that all intensities are equally common as possible
#
# cumulative distribution function (cdf) the transfrom function which normalizes
# the pixels
def histeq(im,nbr_bins=256):
    """ Histogram equalization of a grayscale image. """

    # get image Histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape), cdf

# assuming that all the images have the same size
# we can sum up all the images and compute the average
def compute_average(imlist):
    """ Computer the average of a list of images. """

    # open first image and make into array of type floating
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skipped')
    averageim /= len(imlist)

    # return average as uint8
    return array(averageim, 'uint8')
