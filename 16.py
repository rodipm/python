import datetime

def isLeap(y):
    return (y % 4 and y % 100 and y % 400) == 0
result = list()
for y in range(1006, 1997):
    if isLeap(y) and str(y)[-1] == '6':
        result.append(y)
#print(result)

matches = list()

for y in result:
    if datetime.date(y, 1, 1).weekday() == 3 and datetime.date(y-1, 12, 1).weekday() == 0:
        matches.append(y)
print(matches)

# so the second youngest is 1756. Searching google for the date 26/01/1756 we fid it is the birth date of Mozart. The answer is Mozart
