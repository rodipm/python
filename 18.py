import requests as req
from PIL import Image
from io import BytesIO


#img = Image.open(BytesIO(req.get('http://www.pythonchallenge.com/pc/return/cookies.jpg', auth=('huge', 'file')).content))
#print(img.info)

res = req.get('http://www.pythonchallenge.com/pc/return/cookies.jpg', auth=('huge', 'file'))
print(res.cookies.get_dict())
