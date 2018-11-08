import requests
from PIL import Image
from io import BytesIO


data = open('evil2.gfx', 'rb').read()
print(data)

for i in range(5):
    open(f'evil{i}.jpg', 'wb+').write(data[i::5])
    Image.open(f'evil{i}.jpg').show()

# disproportional























#img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/return/evil2.jpg', auth=('huge', 'file')).content))
#img.show()

#(W, H) = img.size

#def process(color):
#    newimg = Image.new('RGB', (W, H)) 
#    for x in range(W):
#        for y in range(H):
#            if img.getpixel((x, y))  == color:
#                newimg.putpixel((x, y), color)
#            else:
#                newimg.putpixel((x, y), (0, 0, 0))
#    return newimg
#
#red = process((255, 0, 0))
#green = process((0, 255, 0))
#blue = process((0, 0, 255))
#
#red.show()
#green.show()
#blue.show()

#(img1, img2, img3) = img.split()
#img1.show()
#img2.show()
#img3.show()

