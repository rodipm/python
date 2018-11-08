import requests
from PIL import Image
from io import BytesIO

res = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=('huge', 'file'))

img = Image.open(BytesIO(res.content))

cImg = Image.new('RGB', (100, 100))

p = 0
for y in range(100):
    for x in range(100):
        cImg.putpixel((x, y), img.getpixel((p, 0)))
        p += 1

# lets walk around then: (99, 98) -> ((99-98) = 1, (99-97) = 2) -> (97, 96) -> ((99-96) = 3, (99-95) = 4)

fImg = Image.new('RGB', (100, 100))
px = 99
py = 99
for y in range(100):
    for x in range(100):
        px = py
        py = px - 1
        fImg.putpixel((x,y), cImg.getpixel((px, py)))
        #px = py
        #px = -1*px + (99)
        #if (x%2 == 0):
        #    py = px - 1
        #else:
        #    py = px + 1
        #print(f'{px}, {py}')
        #if (px >= 0 and py >= 0):
        #    fImg.putpixel((x,y), cImg.getpixel((px, py)))
fImg.show()
       # if n != 99:
       #     print(n)
       #     if px % 2 == 0:
       #         pixel = cImg.getpixel(((99-px), (99-py)))
       #         print(str(99 - px) + ' ' + str(99 - py))
       #     else:
       #         pixel = cImg.getpixel((px, py))
       #         print(str(px) + ' ' + str(py))
       #     
