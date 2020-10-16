import re
import requests
import time
import category_id as ci


def get_product_titles(content_splited):
    ad_id = re.compile("^adId")
    product_title = re.compile("^productTitle")
    product_title_and_org_with_ad = list()

    for i in range(len(content_splited)):
        if ad_id.match(content_splited[i]):
            product_title_and_org_with_ad.append(content_splited[i])
        if product_title.match(content_splited[i]):
            product_title_and_org_with_ad.append(content_splited[i])

    product_title_with_ad = []
    for i in range(len(product_title_and_org_with_ad)):
        if not product_title_and_org_with_ad[i].startswith('productTitleOrg'):
            product_title_with_ad.append(product_title_and_org_with_ad[i])

    for i in range(len(product_title_with_ad)):
        product_title_with_ad[i] = product_title_with_ad[i].replace(
            "productTitle:", "")

    how_many = 0
    for i in range(len(product_title_with_ad)):
        if product_title_with_ad[i].startswith('adId'):
            how_many += 1

    for i in range(len(product_title_with_ad)-how_many):
        if product_title_with_ad[i].startswith('adId'):
            product_title_with_ad.pop(i+1)

    product_title = []
    for i in range(len(product_title_with_ad)):
        if not product_title_with_ad[i].startswith('adId'):
            product_title.append(product_title_with_ad[i])

    return product_title


def get_review_counts(content_splited):
    ad_id = re.compile("^adId")
    review_count = re.compile("^reviewCountSum")
    review_counts_with_ad = list()

    for i in range(len(content_splited)):
        if ad_id.match(content_splited[i]):
            review_counts_with_ad.append(content_splited[i])
        if review_count.match(content_splited[i]):
            review_counts_with_ad.append(content_splited[i])

    for i in range(len(review_counts_with_ad)):
        review_counts_with_ad[i] = review_counts_with_ad[i].replace(
            "reviewCountSum:", "")

    how_many_ad = 0
    for i in range(len(review_counts_with_ad)):
        if review_counts_with_ad[i].startswith('adId'):
            how_many_ad += 1

    for i in range(len(review_counts_with_ad)-how_many_ad):
        if review_counts_with_ad[i].startswith('adId'):
            review_counts_with_ad.pop(i+1)

    review_counts = list()
    for i in range(len(review_counts_with_ad)):
        if not review_counts_with_ad[i].startswith('adId'):
            review_counts.append(review_counts_with_ad[i])

    return review_counts


def get_purchase_counts(content_splited):
    ad_id = re.compile("^adId")
    purchase_count = re.compile("^purchaseCnt")
    purchase_count_with_ad = list()

    for i in range(len(content_splited)):
        if ad_id.match(content_splited[i]):
            purchase_count_with_ad.append(content_splited[i])
        if purchase_count.match(content_splited[i]):
            purchase_count_with_ad.append(content_splited[i])

    for i in range(len(purchase_count_with_ad)):
        purchase_count_with_ad[i] = purchase_count_with_ad[i].replace(
            "purchaseCnt:", "")

    how_many_ad = 0
    for i in range(len(purchase_count_with_ad)):
        if purchase_count_with_ad[i].startswith('adId'):
            how_many_ad += 1

    for i in range(len(purchase_count_with_ad)-how_many_ad):
        if purchase_count_with_ad[i].startswith('adId'):
            purchase_count_with_ad.pop(i+1)

    purchase_counts = []
    for i in range(len(purchase_count_with_ad)):
        if not purchase_count_with_ad[i].startswith('adId'):
            purchase_counts.append(purchase_count_with_ad[i])

    return purchase_counts


def get_price(content_splited):
    ad_id = re.compile("^adId")
    price_count = re.compile("^mobilePrice")
    price_count_with_ad = list()

    for i in range(len(content_splited)):
        if ad_id.match(content_splited[i]):
            price_count_with_ad.append(content_splited[i])
        if price_count.match(content_splited[i]):
            price_count_with_ad.append(content_splited[i])

    for i in range(len(price_count_with_ad)):
        price_count_with_ad[i] = price_count_with_ad[i].replace(
            "mobilePrice:", "")

    how_many_ad = 0
    for i in range(len(price_count_with_ad)):
        if price_count_with_ad[i].startswith('adId'):
            how_many_ad += 1

    for i in range(len(price_count_with_ad)-how_many_ad):
        if price_count_with_ad[i].startswith('adId'):
            price_count_with_ad.pop(i+1)

    price = []
    for i in range(len(price_count_with_ad)):
        if not price_count_with_ad[i].startswith('adId'):
            price.append(price_count_with_ad[i])

    return price


def get_open_date(content_splited):
    ad_id = re.compile("^adId")
    open_date = re.compile("^openDate")
    open_dates_with_ad = list()

    for i in range(len(content_splited)):
        if ad_id.match(content_splited[i]):
            open_dates_with_ad.append(content_splited[i])
        if open_date.match(content_splited[i]):
            open_dates_with_ad.append(content_splited[i])

    for i in range(len(open_dates_with_ad)):
        open_dates_with_ad[i] = open_dates_with_ad[i].replace(
            "openDate:", "")

    how_many_ad = 0
    for i in range(len(open_dates_with_ad)):
        if open_dates_with_ad[i].startswith('adId'):
            how_many_ad += 1

    for i in range(len(open_dates_with_ad)-how_many_ad):
        if open_dates_with_ad[i].startswith('adId'):
            open_dates_with_ad.pop(i+1)

    open_dates = []
    for i in range(len(open_dates_with_ad)):
        if not open_dates_with_ad[i].startswith('adId'):
            open_dates.append(open_dates_with_ad[i])

    def insert_point(string, index):
        return string[:index] + '.' + string[index:]

    for i in range(len(open_dates)):
        open_dates[i] = insert_point(open_dates[i], 4)
        open_dates[i] = insert_point(open_dates[i], 7)
        open_dates[i] = open_dates[i][:10]

    return open_dates


for i in range(len(ci.category_id)):
    category_id = str(ci.category_id[i])
    url = "https://search.shopping.naver.com/search/category?catId=" + category_id
    res = requests.get(url)
    res.raise_for_status()

    content = res.text
    content_splited = content.split(",")

    for i in range(len(content_splited)):
        content_splited[i] = content_splited[i].replace("{", "")
        content_splited[i] = content_splited[i].replace("}", "")
        content_splited[i] = content_splited[i].replace("\"", "")

    product_title = get_product_titles(content_splited)
    review_count = get_review_counts(content_splited)
    purchase_count = get_purchase_counts(content_splited)
    price = get_price(content_splited)
    open_date = get_open_date(content_splited)

    product_number = 40
    product_info = list()
    for i in range(product_number):
        product_info.append((product_title[i] + ", " + review_count[i] + ", " +
                             purchase_count[i] + ", " + price[i] + ", " + open_date[i]))

    text_name = category_id + '.txt'
    f = open(text_name, 'w', encoding='utf-8')
    for i in range(len(product_info)):
        data = f'{product_info[i]}\n'
        f.write(data)
    f.close()

    time.sleep(0.01)
