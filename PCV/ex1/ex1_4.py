from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import matplotlib.cm as cm

def outline(path='../../images/squares.jpg'):

    print "RUNNING"

    im = array(Image.open(path).convert('L'))

    #Sodel derivative filters
    imx = zeros(im.shape)
    filters.sobel(im,1,imx)

    imy = zeros(im.shape)
    filters.sobel(im,0,imy)

    magnitude = sqrt(imx**2+imy**2)

    alpha = arctan2(imy,imx)

    g_im = concatenate([imx * cos(alpha), imy * sin(alpha)])

    print "\n SOBEL"
    plt.figure("Sobel",figsize=(13,5))
    print "The Original Image"
    plt.subplot(1,6,1)
    plt.imshow(im, cmap=cm.Greys_r)
    plt.xlabel("Original Image")

    print "The X-Derivative (Sobel)"
    plt.subplot(1,6,2)
    plt.imshow(imx, cmap=cm.Greys_r)
    plt.xlabel("X-Derivative")

    print "The Y-Derivative (Sobel)"
    plt.subplot(1,6,3)
    plt.imshow(imy, cmap=cm.Greys_r)
    plt.xlabel("Y-Derivative")

    print "The Magnitude"
    plt.subplot(1,6,4)
    plt.imshow(magnitude, cmap=cm.Greys_r)
    plt.xlabel("Gradient Magnitude")

    print "The Direction"
    plt.subplot(1,6,5)
    plt.imshow(alpha, cmap=cm.Greys_r)
    plt.xlabel("Gradient Direction")

    print "The Gradient Matrix"
    plt.subplot(1,6,6)
    plt.imshow(g_im, cmap=cm.Greys_r)

    plt.show()

    imx = zeros(im.shape)
    filters.prewitt(im,1,imx)

    imy = zeros(im.shape)
    filters.prewitt(im,0,imy)

    magnitude = sqrt(imx**2+imy**2)

    alpha = arctan2(imy,imx)

    g_im = concatenate([imx * cos(alpha), imy * sin(alpha)])

    print "\n PREWITT"

    plt.figure("Prewitt",figsize=(13,5))
    print "The Original Image"
    plt.subplot(1,6,1)
    plt.imshow(im, cmap=cm.Greys_r)
    plt.xlabel("Original Image")

    print "The X-Derivative (Sobel)"
    plt.subplot(1,6,2)
    plt.imshow(imx, cmap=cm.Greys_r)
    plt.xlabel("X-Derivative")

    print "The Y-Derivative (Sobel)"
    plt.subplot(1,6,3)
    plt.imshow(imy, cmap=cm.Greys_r)
    plt.xlabel("Y-Derivative")

    print "The Magnitude"
    plt.subplot(1,6,4)
    plt.imshow(magnitude, cmap=cm.Greys_r)
    plt.xlabel("Gradient Magnitude")

    print "The Direction"
    plt.subplot(1,6,5)
    plt.imshow(alpha, cmap=cm.Greys_r)
    plt.xlabel("Gradient Direction")

    print "The Gradient Matrix"
    plt.subplot(1,6,6)
    plt.imshow(g_im, cmap=cm.Greys_r)

    plt.show()

    print "Done"

outline()
