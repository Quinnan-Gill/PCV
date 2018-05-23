from PIL import Image
import numpy as np
import pylab as plt
from scipy.ndimage import filters
import matplotlib.cm as cm

# row = np.linspace(-2,2,20)
# X,Y = np.meshgrid(row,row)
# Z = np.exp(-((X-1.5)**2+(Y+1)**2))
# Z += np.exp(-((X)**2+(Y)**2))

def contour_gauss(path='../../data/empire.jpg',g_max=5):
    im = np.array(Image.open(path).convert('L'), dtype=np.uint8)


    print "RUNNING"
    plt.figure(figsize=(15,5))
    plt.subplot(1,g_max+1,1)
    plt.imshow(im, cmap=cm.Greys_r)
    plt.subplot(1,g_max+1,2)
    plt.contourf(im, origin="image")
    plt.xlabel("Gaussian=0")

    for i in range(1,g_max):
        temp_im = filters.gaussian_filter(im,i+1)
        axis_val = "Gaussian = " + str(i)
        print axis_val
        plt.subplot(1,g_max+1,i+2)
        plt.contourf(temp_im, origin="image")

        plt.xlabel(axis_val)

    print "FINISHED"
    plt.show()
    # print X,Y

contour_gauss()
