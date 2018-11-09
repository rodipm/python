import requests
from PIL import Image
from io import BytesIO

res = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=('huge', 'file'))

img = Image.open(BytesIO(res.content))

W, H = img.size

result = Image.new('RGB', (100, 100))

x, y = -1, 0
dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]

n = 0

for i in range(100, 1, -2):
    steps = [i, i-1, i-1, i-2]
    
    for j in range(4):
        k = 0
        while k < steps[j]:
            x += dirs[j][0]
            y += dirs[j][1]

            result.putpixel((x, y), img.getpixel((n, 0)))

            k += 1
            n += 1
result.show()
