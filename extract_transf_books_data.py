import requests
from bs4 import BeautifulSoup
from extract_category import extract_category
from extract_img_url import extract_img_url
from extract_upc_prices_available import extract_upc_prices_available

# extract données brutes : E de ETL
def extract_transf_books_data(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        product_description = soup.find('meta', {'name': 'description'})
        product_description = product_description['content']
        universal_product_code = extract_upc_prices_available(url)['universal_product_code']
        price_including_tax = extract_upc_prices_available(url)['price_including_tax']
        price_excluding_tax = extract_upc_prices_available(url)['price_excluding_tax']
        number_available = extract_upc_prices_available(url)['number_available']
        category = extract_category(url)
        star_rating = soup.find(class_='star-rating')
        review_rating = star_rating['class'][1]
        image_url = extract_img_url(url)
        data_book = {'product_page_url': url, 'universal_product_code': universal_product_code, 'title': title,
                     'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
                     'number_available': number_available, 'product_description': product_description,
                     'category': category, 'review_rating': review_rating, 'image_url': image_url}
        return data_book
