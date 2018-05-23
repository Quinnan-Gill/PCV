from PIL import Image
from pylab import *

# # Matlab
# im = array(Image.open('empire.jpg'))
# imshow(im)
# print('Please click 3 points')
# # ginput comes with PyLab
# x = ginput(3)
# print('you clicked:',x)
# show()


# Numpy Introduction
im = array(Image.open('empire.jpg'))
print(im.shape, im.dtype) # im.shape = rows, columns, color channels
                          # im.dtype = data type of the array elements(unit8)

im = array(Image.open('empire.jpg').convert('L'), 'f') #the f means floating point
print(im.shape, im.dtype) # im.shape = rows, columns but no color channels b/c grayscale

# The value at corrdinates i,j and color channel k are accessed like this
value = im[i,j,k]

im[i,:] = im[j,:]   # set the values of row i with values from row j
im[:,i] = 100       # set all the values in column i to 100
im[:100,:50].sum()  # the sum of the values of the first 100 rows and 50 columns
im[50:100,50:100]   # rows 50-100, columns 50-100 (100th not included)
im[i].mean()        # average of row i
im[:,-1]            # last column
im[-2,:] (or im[-2])# second to last row
