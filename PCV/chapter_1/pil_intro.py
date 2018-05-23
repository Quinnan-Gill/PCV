# Python Imaging Library (PIL) procides general image handling
# and lost of usefule basic image operations
from PIL import Image
import os


# Image module = most important module
# Returns the value pil_im as a PIL image object
pil_im = Image.open('empire.jpg')
# Have the images be displayed
pil_im.show()
#
# # color conversions are done using the convert() method
# # To read and convert to grayscale have .convert('L')
# pil_im = Image.open('empire.jpg').convert('L')
# pil_im.show()

# # Using save() PIL can save images in most image file formats
# for infile in filelist:
#     outfile = os.path.splitext(infile)[0] + ".jpg"
#     if infile != outfile:
#         try:
#             # open() creates a PIL image object
#             # save() saves the image to a file with the given filename
#             Image.open(infile).save(outfile)
#         except IOError:
#             print "cannot convert", infile

# # Turn into a thumbnail the size indicated as passed in tuple
# pil_im.thumbnail((128,128))

# Cropping
# crop uses a 4-tuple that goes left, upper, right, lower
# box = (180,180,2000,2000)
# region = pil_im.crop(box)
#
# region.show()

# 
# # Resize and Rotate
# # resize() with tuple
# out = pil_im.resize((128,128))
# out.show()
# out = pil_im.rotate(45)
# out.show()
