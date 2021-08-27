import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

category_books = []

def category_books_extract(url):
    page_url = url
    # changer page des livres de la catégorie
    i = 1
    response = requests.get(page_url)
    while response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Récupérer toutes les url des pages de produit
        h3s = soup.findAll('h3')
        for h3 in h3s:
            a = h3.find('a')
            product_page_url = a['href']
            oldurl = url
            path = oldurl.rsplit('/', 1)[0]
            category_books.append(path + '/' + product_page_url)
        i += 1
        page_url = urljoin(page_url, 'page-' + str(i) + '.html')
        response = requests.get(page_url)
    return(category_books)

# print(category_books_extract('http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'))