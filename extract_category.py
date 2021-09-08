import requests
from bs4 import BeautifulSoup


def extract_category(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        ul = soup.find('ul', class_='breadcrumb')
        lis = ul.findAll('li')
        # transform
        category_text = lis[2].text
        category = list(category_text)
        category[0] = ''
        category[-1] = ''
        category = ''.join(category)
        return category
