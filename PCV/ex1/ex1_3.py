from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import matplotlib.cm as cm


def quotient_image(path='../../data/empire.jpg',pic_lab='Empire State Building'):

    print "RUNNING"

    im = array(Image.open(path).convert('L'))

    g_im = filters.gaussian_filter(im, 10)

    q_im = im / g_im

    plt.figure(figsize=(13,5))

    print "The Original Image"
    plt.subplot(1,3,1)
    plt.imshow(im, cmap=cm.Greys_r)
    plt.xlabel("Original Image")

    print "The Gaussian Blurred Image"
    plt.subplot(1,3,2)
    plt.imshow(g_im, cmap=cm.Greys_r)
    plt.xlabel("Gaussian Blurred Image")

    print "The Quotient Image"
    plt.subplot(1,3,3)
    plt.imshow(q_im, cmap=cm.Greys_r)
    plt.xlabel("Quotient Image")

    plt.show()

    print "DONE"

quotient_image()
quotient_image('../../images/empire.jpg')
