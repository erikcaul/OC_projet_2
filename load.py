import urllib.request
import csv
import os
from extract import *
from transform import transform_image_url

def load_data_book(product_page_url):
    # Load one product data
    # data_books_list = []
    # for product_page_url in product_url_list:
    title = extract_title(product_page_url)
    product_description = extract_product_description(product_page_url)
    universal_product_code = extract_upc_prices_available(product_page_url)['universal_product_code']
    price_including_tax = extract_upc_prices_available(product_page_url)['price_including_tax']
    price_excluding_tax = extract_upc_prices_available(product_page_url)['price_excluding_tax']
    number_available = extract_upc_prices_available(product_page_url)['number_available']
    category = extract_category(product_page_url)
    review_rating = extract_review_rating(product_page_url)
    image_url = transform_image_url(extract_raw_img_url(product_page_url))

    data_book = {'product_page_url': product_page_url, 'universal_product_code': universal_product_code,
                 'title': title,
                 'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
                 'number_available': number_available, 'product_description': product_description,
                 'category': category, 'review_rating': review_rating, 'image_url': image_url}
    # data_books_list.append(data_book)
    return data_book

def load_book_img(product_page_url):
    # load book image
    dict_book = load_data_book(product_page_url)
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
