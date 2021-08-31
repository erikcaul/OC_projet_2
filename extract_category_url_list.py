import requests
from bs4 import BeautifulSoup

category_url_list = []


def extract_category_url_list(url):
    url = url
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Récupérer toutes les url des categories de produit
        ul = soup.find('ul', class_='nav nav-list')
        ul_2 = ul.find('ul')
        lis = ul_2.findAll('li')
        for li in lis:
            a = li.find('a')
            category_url = a['href']
            oldurl = url
            path = oldurl.rsplit('/', 1)[0]
            category_url = path + '/' + category_url
            category_url_list.append(category_url)
        return category_url_list
