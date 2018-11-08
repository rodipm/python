import re

a = ['1']
b = a[0]

for x in range(30):

    m = re.findall(r"(\d)(\1*)", b)
    b = '' 
    for i in range(len(m)):
        if ( m[i][1] == ''):
            n = '1'
        else:
            n = str(len(m[i][1]) + 1)
        b = b + n + m[i][0]
    a.append(b)
print(len(a[30]))
