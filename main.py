import os.path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.parse
import urllib.request
import csv
import os

# Extract
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


def extract_title(soup):
    title = soup.find('h1').text
    return title

def extract_product_description(soup):
    product_description = soup.find('meta', {'name': 'description'})
    product_description = product_description['content']
    return(product_description)

def extract_upc_prices_available(soup):
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

def extract_category(soup):
    ul = soup.find('ul', class_='breadcrumb')
    lis = ul.findAll('li')
    category_text = lis[2].text
    category = list(category_text)
    category[0] = ''
    category[-1] = ''
    category = ''.join(category)
    return(category)

def extract_review_rating(soup):
    star_rating = soup.find(class_='star-rating')
    review_rating = star_rating['class'][1]
    return(review_rating)

def extract_raw_img_url(soup):
    active_image = soup.find(class_='item')
    image = active_image.find('img')
    raw_image_url = image['src']
    return(raw_image_url)

def extract_product_info(product_page_url):
    # Extract one product data
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = extract_title(soup)
        product_description = extract_product_description(soup)
        universal_product_code = extract_upc_prices_available(soup)['universal_product_code']
        price_including_tax = extract_upc_prices_available(soup)['price_including_tax']
        price_excluding_tax = extract_upc_prices_available(soup)['price_excluding_tax']
        number_available = extract_upc_prices_available(soup)['number_available']
        category = extract_category(soup)
        review_rating = extract_review_rating(soup)
        image_url = extract_raw_img_url(soup)

        data_book = {'product_page_url': product_page_url, 'universal_product_code': universal_product_code, 'title': title,
                     'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
                     'number_available': number_available, 'product_description': product_description,
                     'category': category, 'review_rating': review_rating, 'image_url': image_url}
        return data_book

# Transform

def transform_category_url_list(raw_category_url_list):
    category_url_list = []
    for category_url in raw_category_url_list:
        base_url = 'http://books.toscrape.com/index.html'
        path = base_url.rsplit('/', 1)[0]
        category_url= urllib.parse.urljoin(path, category_url)
        category_url_list.append(category_url)
    return category_url_list


def transform_books_url_list_per_category(raw_books_url_list_per_category):
    product_page_url_list = []
    base_url = 'https://books.toscrape.com/catalogue/'
    for raw_book_url in raw_books_url_list_per_category:
        url_split = raw_book_url.rsplit('/', 2)[1:3]
        url_split_2 = url_split[0] + '/'
        product_page_url = urllib.parse.urljoin(base_url, url_split_2, url_split)
        product_page_url_list.append(product_page_url)
    return(product_page_url_list)

def transform_image_url(raw_image_url):
    url_split = raw_image_url.rsplit('/', 5)[1:6]
    image_url = 'http://books.toscrape.com'
    for i in url_split:
        image_url += '/' + i
    return image_url

# Load
def load_book_img(dict_book):
    # load book image
    upc = dict_book['universal_product_code']
    image_url = dict_book['image_url']
    file_name = 'img_folder/' + upc + '.jpg'
    urllib.request.urlretrieve(image_url, file_name)

def load_data_books_in_csv_file(data_dict_list):
    category = data_dict_list[0]['category']
    csv_file = 'csv_files/' + category + '.csv'
    fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                  'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    try:
        if not os.path.exists('csv_files'):
            os.makedirs('csv_files')
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_dict_list:
                writer.writerow(row)

    except IOError:
        print('I/O error')


if __name__ == '__main__':
    if not os.path.exists('img_folder'):
        os.makedirs('img_folder')
    if not os.path.exists('img_folder'):
        os.makedirs('img_folder')
    raw_category_url_list = extract_raw_category_url_list('https://books.toscrape.com/index.html')
    category_url_list = transform_category_url_list(raw_category_url_list)
    for category_url in category_url_list:
        raw_product_url_list = extract_raw_books_url_list_per_category(category_url)
        product_page_url_list = transform_books_url_list_per_category(raw_product_url_list)
        data_dict_list = []
        for product_page_url in product_page_url_list:
            data_dict = extract_product_info(product_page_url)
            # transform image url et modif dans le dictionnaire
            image_url = transform_image_url(data_dict['image_url'])
            data_dict['image_url'] = image_url
            data_dict_list.append(data_dict)
            load_book_img(data_dict)
            print(data_dict)
        load_data_books_in_csv_file(data_dict_list)



# séparer dans mon code l'extract (une fonction); le transform (une fonction) et le load (une fonction)
# dans un seul fichier ou dans 3
# Extract : données brutes
# Transform : générer les url transformées, nom des img.
# load : save_data
# dowload img à part

# mettre dans une BdD, API, fair eune application Qu'est-ce qui peut être fait à partir de ça