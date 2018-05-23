from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('images/empire.jpg').convert('L'))

# create a new figure
figure()
# don't use colors
gray()
# show countours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')

# histogram
figure()
hist(im.flatten(),128)
show()
