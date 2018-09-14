from PIL import Image
from numpy import *
import os

def process_image(imagename,resultname,params="--edge-thresh 5 --peak-thresh 2"):
    """ Process an image and siave the results in a file. """

    if imagename[-3:] != 'pmg':
        # create a pgm file
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

    cmmd = str("./vlfeat-0.9.21/bin/maci64/sift "+imagename+" --output="+resultname+" "+params)

    print cmmd

    os.system(cmmd)

    print 'processed', imagename, 'to', resultname

def read_features_from_file(filename):
    """ Read feature properties and return in matrix form. """

    f = loadtxt(filename)
    return f[:,:4],f[:,4:] # freatures locations, descriptors

def write_features_to_file(filename,locs,desc):
    """ Save feature location and descriptor to file. """
    savetxt(filename,hstack((locs,desc)))

def plot_features(im,locs,circle=False):
    """ Show image features. input: im (image as array),
    locs (row, col, scale, orientation of each feature). """

    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x,y,'b',linewidth=2)

    imshow(im)
    if cirlce:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        plot(locs[:,0],locs[:,1],'ob')
    axis('off')
