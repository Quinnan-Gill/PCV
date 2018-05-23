from PIL import Image
import numpy as np

from skimage.transform import (hough_line, hough_line_peaks,
                              probabilistic_hough_line)
from skimage.feature import canny
from skimage import data

import matplotlib.pyplot as plt
from scipy.ndimage import filters
import matplotlib.cm as cm

def hough_line_detection(path='../../data/empire.jpg'):

    print "START"

    # image = array(Image.open(path).convert('L'))

    print "\n Cross Image"
    #Generating the cross image
    image = np.zeros((100, 100))
    idx = np.arange(25, 75)
    image[idx[::-1], idx] = 255
    image[idx, idx] = 255
    # image = np.array(Image.open(path).convert('L'))

    # Classic straight line Hough transform
    h, theta, d = hough_line(image)

    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    ax = axes.ravel()

    print "Original Image"
    ax[0].imshow(image, cmap=cm.gray)
    ax[0].set_title('Original Image')
    ax[0].set_axis_off()

    print "Hough Line Detection"
    ax[1].imshow(np.log(1 + h),
                 extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                 cmap=cm.gray, aspect=1/1.5)
    ax[1].set_title('Hough transform')
    ax[1].set_xlabel('Angles (degrees)')
    ax[1].set_ylabel('Distance (pixels)')
    ax[1].axis('image')

    print "Hough lines on the original image"
    ax[2].imshow(image, cmap=cm.gray)
    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
        ax[2].plot((0, image.shape[1]), (y0, y1), '-r')
    ax[2].set_xlim((0, image.shape[1]))
    ax[2].set_ylim((0, image.shape[1]))
    ax[2].set_axis_off()
    ax[2].set_title('Detected Lines')

    plt.tight_layout()
    plt.show()

    # Line finding using the Probabilistic Hough Transform
    image = data.camera() #This is just used as an example picture
    # image = np.array(Image.open(path).convert('L'))
    edges = canny(image, 2, 1, 25)
    lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                    line_gap=3)
    # Generating figure 2
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
    ax = axes.ravel()

    print "\n Actual Image"

    print "Original Image"
    ax[0].imshow(image, cmap=cm.gray)
    ax[0].set_title('Input image')

    print "Determining Canny Edges"
    ax[1].imshow(edges, cmap=cm.gray)
    ax[1].set_title('Canny edges')

    print "Determining the Probabilistic Hough"
    ax[2].imshow(edges * 0)
    for line in lines:
        p0, p1 = line
        ax[2].plot((p0[0], p1[0]), (p0[1], p1[1]))
    ax[2].set_xlim((0, image.shape[1]))
    ax[2].set_ylim((image.shape[0], 0))
    ax[2].set_title('Probabilistic Hough')

    for a in ax:
        a.set_axis_off()

    print "Deterining Tight Layout"
    plt.tight_layout()

    print "Showing image"
    plt.show()

    print "END"

hough_line_detection()
