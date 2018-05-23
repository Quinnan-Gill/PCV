from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
from scipy.ndimage import measurements,morphology
import matplotlib.cm as cm

def label_and_hist(path='../../data/houses.png', threshold=128):

    print "Starting\n"

    colorlist = ['r','g','b','y','c','m']

    im = array(Image.open(path).convert('L'))

    im = 1*(im<threshold)


    labels, nbr_objects = measurements.label(im)
    print "Number of objects:", nbr_objects

    size = labels.shape

    bars = zeros(nbr_objects)
    groups = linspace(1, nbr_objects, num=nbr_objects)

    for x in range(size[0]):
        for y in range(size[1]):
            bars[labels[x][y]-1] += 1

    print "Finished calculating"

    plt.figure("Label Histogram", figsize=(13,5))
    barlist = plt.bar(groups,bars, align='center', alpha=0.5)
    for i in range(len(barlist)):
        barlist[i].set_color(colorlist[i%len(colorlist)])
    plt.ylabel('The Size of the Labels')
    plt.show()
    print "\nDone\n"

# def display_array(array, size=(512,512)):
#     for i in range(0,size[0]):
#         for j in range(0,size[1]):
#             print array[i][j],
#         print "\n",


label_and_hist('../../images/empire.jpg')
