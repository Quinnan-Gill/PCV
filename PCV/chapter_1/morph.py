from scipy.ndimage import measurements,morphology
from PIL import Image
from numpy import *

# load image and threshold to make sure it is binary
im = array(Image.open('data/empire.jpg').convert('L'))
im = 1*(im<128) #mult by 1 to turn bool to 0's and 1's

labels, nbr_objects = measurements.label(im)
print("Number of objects:", nbr_objects)

# morphology - opening to separate objects better
# binary_opening() specifies the sturcturing element
# sturcturing element: an array that indicates what neighbors to use when
#  centered around a pixel i.e. 9 = 4 above and 4 below && 5 = 2 in x direction
# iterations determines how many times to apply the operation
im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)

labels_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects: ", nbr_objects_open)
