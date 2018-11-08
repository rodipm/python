from PIL import Image
import numpy as np

img = Image.open('cave.jpg')
pixels = img.load()
w, h = img.size

even = Image.new('RGB', (w//2, h//2)) 
odd = Image.new('RGB', (w//2, h//2)) 

for x in range(w):
    for y in range(h):
        if x % 2:
            odd.putpixel((x//2, y//2), pixels[x,y])
        else:
            even.putpixel((x//2, y//2), pixels[x,y])
#even.show()
odd.show()
