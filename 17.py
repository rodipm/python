import numpy as np
import requests
from io import BytesIO
from PIL import Image


res = BytesIO(requests.get('http://www.pythonchallenge.com/pc/return/mozart.gif', auth=('huge', 'file')).content)
img  = Image.open(res)
data = np.array(img)

shifted = [bytes( np.roll(row, -row.tolist().index(195)).tolist()) for row in data]

shifted = Image.frombytes(img.mode, img.size, b''.join(shifted))
shifted.show()
