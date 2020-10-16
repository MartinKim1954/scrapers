import re
import requests

url = "https://search.shopping.naver.com/search/category?catId=50000115"
res = requests.get(url)
res.raise_for_status()

content = res.text

splited = content.split(",")
for i in range(len(splited)):
    splited[i] = splited[i].replace("{", "")
    splited[i] = splited[i].replace("}", "")
    splited[i] = splited[i].replace("\"", "")
open_date = re.compile("^openDate")
ad_id = re.compile("^adId")

n = []
for i in range(len(splited)):
    if open_date.match(splited[i]):
        n.append(splited[i])
    if ad_id.match(splited[i]):
        n.append(splited[i])


for i in range(len(n)):
    n[i] = n[i].replace("openDate:", "")

how_many = 0
for i in range(len(n)):
    if n[i].startswith('adId'):
        how_many += 1
        # m.append(i)


def insert_point(string, index):
    return string[:index] + '.' + string[index:]


for i in range(len(n)):
    n[i] = insert_point(n[i], 4)
    n[i] = insert_point(n[i], 7)
    n[i] = n[i][:10]

print(n)
print(len(n))

for i in range(len(n)-how_many):
    if n[i].startswith('adId'):
        n.pop(i+1)

m = []
for i in range(len(n)):
    if not n[i].startswith('adId'):
        m.append(n[i])

print(m)
print(len(m))
txt_name = '50000115' + '.txt'


f = open(txt_name, 'w')
for i in range(len(m)):
    data = f'{m[i]}\n'
    f.write(data)
f.close()

f = open(txt_name, 'rw')
while True:
    lines = f.readlines()
    if not lines:
        break
    print(lines)
lines[0] + '1010101010'
f.close()
