import urllib.request as req
from PIL import Image, ImageChops
import numpy as np

img = req.urlopen('http://pythonchallenge.com/pc/def/oxygen.png')

with open('oxygen.jpg', 'wb+') as f:
    f.write(img.read())

img = Image.open('oxygen.jpg')

#img = np.array(img)
#
#
#img[:,:,2] *= 0
#img[:,:,1] *= 0
#
#img = Image.fromarray(img)

#img = img.split()
#img[0].show()
#img[1].show()
#img[2].show()

pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

result = list()

pixels = pixels[:][47]

lp = pixels[0]
result.append(chr(lp[0]))

for p in pixels:
    if p != lp and p[0] == p[1] and p[0] == p[2]:
        result.append(chr(p[0]))

        lp = p

result = ''.join(result)
print(result)
