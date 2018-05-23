from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
from scipy.ndimage import measurements,morphology
import matplotlib.cm as cm
from scipy import ndimage

def morph_test(img):

    print "\n RUNNING Morphological Tests\n"

    img_ero = morphology.binary_erosion(img)

    img_dil = morphology.binary_dilation(img)

    print "Morphological Tests Part 1"
    plt.figure("Morphological Operations Pt. 1", figsize=(13,5))

    print "\tOriginal Image"
    plt.subplot(1,3,1)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.xlabel("Original Image")

    print "\tBinary Erosion"
    plt.subplot(1,3,2)
    plt.imshow(img_ero, cmap=cm.Greys_r)
    plt.xlabel("Binary Erosion")

    print "\tBinary Dilation"
    plt.subplot(1,3,3)
    plt.imshow(img_dil, cmap=cm.Greys_r)
    plt.xlabel("Binary Dilation")

    plt.show()

    img_open = morphology.binary_opening(img)

    img_close = morphology.binary_opening(img)

    print "\nMorphlogical Tests Part 2"
    plt.figure("Morphological Operation Pt. 2", figsize=(13,5))

    print "\tOriginal Image"
    plt.subplot(1,3,1)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.xlabel("Original Image")

    print "\tBinary Opening"
    plt.subplot(1,3,2,)
    plt.imshow(img_open, cmap=cm.Greys_r)
    plt.xlabel("Binary Opening")

    print "\tBinary Closing"
    plt.subplot(1,3,3)
    plt.imshow(img_close, cmap=cm.Greys_r)
    plt.xlabel("Binary Closing")

    plt.show()

    print "\n FINNISHED with Morphological Tests"


def morph_oper(path='../../data/empire.jpg', threshold=128):

    print "\n Starting Morphoocal Operations"

    colorlist = ['g','b','y','c','m']

    im = array(Image.open(path).convert('L'))

    im = 1*(im<threshold)

    im = morphology.binary_opening(im)

    im = morphology.binary_erosion(im)

    im = morphology.binary_closing(im)

    im = morphology.binary_dilation(im)

    im = morphology.binary_opening(im)

    com = measurements.center_of_mass(im)

    plt.figure("Morpholocal Operations with Center of Masses", figsize=(13,5))
    plt.imshow(im, cmap=cm.Greys_r)

    print "Unlabeled center of mass:", com
    plt.plot(com[0],com[1],'ro')

    lbl = ndimage.label(im)[0]

    coms = measurements.center_of_mass(im,lbl,[1,2])

    print "\nLabeld center of mass:"

    for i, mass in enumerate(coms):
        print "\t Center of mass", i+1,":",mass
        plt.plot(mass[0],mass[1],'go')

    plt.show()

    print "\n DONE\n"

morph_oper()
