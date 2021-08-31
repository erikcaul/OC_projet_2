import requests
from bs4 import BeautifulSoup


def extract_img_url(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        active_image = soup.find(class_='item')
        image = active_image.find('img')
        image_url = image['src']
        path = url.rsplit('/', 1)[0]
        image_url = path + '/' + image_url
        return image_url
