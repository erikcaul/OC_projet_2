import requests
from bs4 import BeautifulSoup
import os.path
from urllib.parse import urljoin

def extract_raw_category_url_list(url):
    url = url
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Récupérer toutes les url des categories de produit
        ul = soup.find('ul', class_='nav nav-list')
        ul_2 = ul.find('ul')
        lis = ul_2.findAll('li')
        raw_category_url_list = []
        for li in lis:
            a = li.find('a')
            category_url = a['href']
            raw_category_url_list.append(category_url)
        return raw_category_url_list

def extract_raw_books_url_list_per_category(category_url):
    i = 1
    response = requests.get(category_url)
    if not os.path.exists('img_folder'):
        os.makedirs('img_folder')
    while response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        h3s = soup.findAll('h3')
        raw_books_url_list_per_category = []
        for h3 in h3s:
            a = h3.find('a')
            raw_product_page_url = a['href']
            raw_books_url_list_per_category.append(raw_product_page_url)
        i += 1
        page_url = urljoin(category_url, 'page-' + str(i) + '.html')
        response = requests.get(page_url)
    return raw_books_url_list_per_category


def extract_title(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        return title

def extract_product_description(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_description = soup.find('meta', {'name': 'description'})
        product_description = product_description['content']
        return(product_description)

def extract_upc_prices_available(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_table_info = soup.find('table', class_="table table-striped")
        trs = product_table_info.findAll('tr')
        for tr in trs:
            th = tr.find('th')
            if th.text == 'UPC':
                universal_product_code = tr.find('td').text
            if th.text == 'Price (excl. tax)':
                price_excluding_tax = tr.find('td').text
            if th.text == 'Price (incl. tax)':
                price_including_tax = tr.find('td').text
            if th.text == 'Availability':
                number_available = tr.find('td').text
        product_info_data = {'universal_product_code': universal_product_code,
                             'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
                             'number_available': number_available}
        return product_info_data

def extract_category(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        ul = soup.find('ul', class_='breadcrumb')
        lis = ul.findAll('li')
        category_text = lis[2].text
        category = list(category_text)
        category[0] = ''
        category[-1] = ''
        category = ''.join(category)
        return(category)

def extract_review_rating(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        star_rating = soup.find(class_='star-rating')
        review_rating = star_rating['class'][1]
        return(review_rating)

def extract_raw_img_url(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        active_image = soup.find(class_='item')
        image = active_image.find('img')
        raw_image_url = image['src']
        return(raw_image_url)

# def extract_product_info(product_page_url):
#     # Extract one product data
#     response = requests.get(product_page_url)
#     if response.ok:
#         title = extract_title(product_page_url)
#         product_description = extract_product_description(product_page_url)
#         universal_product_code = extract_upc_prices_available(product_page_url)['universal_product_code']
#         price_including_tax = extract_upc_prices_available(product_page_url)['price_including_tax']
#         price_excluding_tax = extract_upc_prices_available(product_page_url)['price_excluding_tax']
#         number_available = extract_upc_prices_available(product_page_url)['number_available']
#         category = extract_category(product_page_url)
#         review_rating = extract_review_rating(product_page_url)
#         image_url = extract_raw_img_url(product_page_url)
#
#         data_book = {'product_page_url': product_page_url, 'universal_product_code': universal_product_code, 'title': title,
#                      'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
#                      'number_available': number_available, 'product_description': product_description,
#                      'category': category, 'review_rating': review_rating, 'image_url': image_url}
#         return data_book
