import urllib.request as req
import re
import zipfile

# lets first get the .zip file
res = req.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

# downloaded then write it in the channel folder
with open('./channel/channel.zip', 'wb+') as f:
    f.write(res.read())

# we have the file unzipped, now lets start performing the search
# the first number given in 'readme.txt' is 90052
n = '90052'
p = re.compile(r' [0-9]+')
i = 0

# it asks us to check the comments (zipFileComments)
zFile = zipfile.ZipFile('./channel/channel.zip')

result = list()

while True:
    with open('./channel/' + n + '.txt', 'r') as f:
        data = str(f.read())
        m = p.findall(data)

        if m: 
            n = str(m[0][1:]) 
            i = i + 1
            print(str(i) + ': ' + n)
            info = str(zFile.getinfo(n + '.txt').comment)
            result.append(info[2:len(info) - 1])
            
            if result[-1] == '\\n':
                result[-1] = '\n'

        else:
            print('Found someting:')
            print(data)
            break
print(''.join(result))

# wich yelds: HOCKEY

