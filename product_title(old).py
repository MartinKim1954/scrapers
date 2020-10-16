import re
import requests
import category_id as ci

url = "https://search.shopping.naver.com/search/category?catId=50000115"
res = requests.get(url)
res.raise_for_status()

content = res.text
content_splited = content.split(",")

for i in range(len(content_splited)):
    content_splited[i] = content_splited[i].replace("{", "")
    content_splited[i] = content_splited[i].replace("}", "")
    content_splited[i] = content_splited[i].replace("\"", "")
product_title = re.compile("^productTitle")
review_numbers = re.compile("^reviewCountSum")
purchase_count = re.compile("^purchaseCnt")
price = re.compile("^mobilePrice")
open_date = re.compile("^openDate")


def insert_point(string, index):
    return string[:index] + '.' + string[index:]


n = []
for i in range(len(content_splited)):
    if product_title.match(content_splited[i]):
        n.append(content_splited[i])
    if purchase_count.match(content_splited[i]):
        n.append(content_splited[i])
    if price.match(content_splited[i]):
        n.append(content_splited[i])
    if open_date.match(content_splited[i]):
        n.append(content_splited[i])
    if review_numbers.match(content_splited[i]):
        n.append(content_splited[i])

m = []
for i in range(len(n)):
    if not n[i].startswith('productTitleOrg'):
        m.append(n[i])
# print(n)
print("길이는요!?", len(m))

for i in range(len(m)):
    m[i] = m[i].replace("productTitle:", "")
    m[i] = m[i].replace("purchaseCnt:", "")
    m[i] = m[i].replace("openDate:", "")
    m[i] = m[i].replace("mobilePrice:", "")
    m[i] = m[i].replace("reviewCountSum:", "")

print(m)
txt_name = '50000115' + '.txt'

f = open(txt_name, 'w')
for i in range(len(m)):
    # if i % 4 == 0 and i != 0:
    data = f'{m[i]}\n'
    # else:
    # data = f'{m[i]},'

    f.write(data)
f.close()


# # 21~23번 데이터(광고데이터) 일일이 뺐음!
