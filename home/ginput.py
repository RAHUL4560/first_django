import matplotlib

#Use the line below to set a backend for matplotib
matplotlib.use('TkAgg')

from PIL import Image
from pylab import *

im = array(Image.open('out.png'))
imshow(im)

print ('Please click 3 points')
x = ginput(3)

print ('you clicked:',x)
show()
