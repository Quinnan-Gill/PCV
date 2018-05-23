from PIL import Image
from numpy import *

im = array(Image.open('empire.jpg').convert('L'))

im2 = 255 - im #invert image

im3 = (100.0/255) * im + 100 #clamp to interval 100...200

im4 = 255.0 * (im/255.0)**2 # squared

print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

# convert back from array
pil_im = Image.fromarray(im)
pil_im.show()
pil_im2 = Image.fromarray(im2)
pil_im2.show()
# for im3 and im4 need to convert to unit8
pil_im3 = Image.fromarray(uint8(im3))
pil_im3.show()
pil_im4 = Image.fromarray(uint8(im4))
pil_im4.show()
