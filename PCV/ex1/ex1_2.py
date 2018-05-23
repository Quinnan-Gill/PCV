from PIL import Image
from numpy import *
import pylab as plt
from scipy.ndimage import filters
import matplotlib.cm as cm


def unsharp_masking(path='../../data/empire.jpg'):

    # establish original images
    im_color = array(Image.open(path))
    im_gray = array(Image.open(path).convert('L'))

    # apply a gaussian filter to blur the image
    im_color_blur = filters.gaussian_filter(im_color, 5)
    im_gray_blur = filters.gaussian_filter(im_gray, 5)

    # substract the blurred image from the originial
    unsharp_im_color = im_color - im_color_blur
    unsharp_im_gray = im_gray - im_gray_blur

    print "RUNNING"

    plt.figure(figsize=(11,5))

    # Display the color unsharp

    print "\n COLOR"
    print "Original Image (Color)"
    plt.subplot(1,3,1)
    plt.imshow(im_color, cmap=cm.Greys_r)
    plt.xlabel("Original (Color)")

    print "Gaussian Blur Image (Color)"
    plt.subplot(1,3,2)
    plt.imshow(im_color_blur)
    plt.xlabel("Gaussian Image")

    print "Unsharpened Image (Color)"
    plt.subplot(1,3,3)
    plt.imshow(unsharp_im_color)
    plt.xlabel("Unsharpened Image")

    plt.show()

    plt.figure(figsize=(11,5))

    print "\n GREY"
    # Display the gray unsharp
    print "Original Image (Grey)"
    plt.subplot(1,3,1)
    plt.imshow(im_gray, cmap=cm.Greys_r)
    plt.xlabel("Original (Grey)")

    print "Gaussian Blur Image (Grey)"
    plt.subplot(132)
    plt.imshow(im_gray_blur, cmap=cm.Greys_r)
    plt.xlabel("Gaussian Image")

    print "Unsharpened Image (Grey)"
    plt.subplot(133)
    plt.imshow(unsharp_im_gray, cmap=cm.Greys_r)
    plt.xlabel("Unsharpened Image")

    plt.show()

unsharp_masking()
