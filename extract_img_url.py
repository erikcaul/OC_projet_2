import requests
from bs4 import BeautifulSoup

# extract url img : E de ETL
def extract_img_url(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        active_image = soup.find(class_='item')
        image = active_image.find('img')
        image_url = image['src']
        # transform
        url_split = image_url.rsplit('/', 5)[1:6]
        image_url = 'http://books.toscrape.com'
        for i in url_split:
            image_url += '/' + i
        return image_url
