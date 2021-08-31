import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from extract_transf_books_data import extract_transf_books_data
from extract_img_url import extract_img_url
from download_img import download_img
from extract_category import extract_category


def extract_books_url_list_per_category(url):
    page_url = url
    i = 1
    j = 0
    response = requests.get(page_url)
    while response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        h3s = soup.findAll('h3')
        data_books_category_list = []
        for h3 in h3s:
            a = h3.find('a')
            product_page_url = a['href']
            url_split = product_page_url.rsplit('/', 2)[1:3]
            product_page_url = 'https://books.toscrape.com/catalogue/' + url_split[0] + '/' + url_split[1]
            data_books_category_list.append(extract_transf_books_data(product_page_url))
            image_url = extract_img_url(product_page_url)
            category = extract_category(product_page_url)
            download_img(image_url, 'img_folder/' + category + '_' + str(j) + '.jpg')
            j += 1
        i += 1
        page_url = urljoin(page_url, 'page-' + str(i) + '.html')
        response = requests.get(page_url)
    return data_books_category_list
