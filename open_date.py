import re

item = '신생아욕조'
html = item + '.html'
first_ad_number = 4

f = open(html, 'r')
file_read = f.read()
f.close()
splited = file_read.split(",")
for i in range(len(splited)):
    splited[i] = splited[i].replace("{", "")
    splited[i] = splited[i].replace("}", "")
    splited[i] = splited[i].replace("\"", "")
price = re.compile("^openDate")
# price_unit = re.compile("^priceUnit")

n = []
j = 1
for i in range(len(splited)):
    if price.match(splited[i]):
        # if not price_unit.match(splited[i]):
        n.append(splited[i])
print(n)
print("길이는요!?", len(n))

for i in range(len(n)):
    n[i] = n[i].replace("openDate:", "")


def insert_point(string, index):
    return string[:index] + '.' + string[index:]


for i in range(len(n)):
    n[i] = insert_point(n[i], 4)
    n[i] = insert_point(n[i], 7)
    n[i] = n[i][:10]

txt_name = 'open_date_' + item + '.txt'

f = open(txt_name, 'w')
for i in range(first_ad_number, len(n)):
    data = f'{n[i]}\n'
    f.write(data)
f.close()

# 21~23번 데이터(광고데이터) 일일이 뺐음!
