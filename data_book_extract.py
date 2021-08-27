import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def data_book_extract(url):
# url = 'http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.find('h1').text
        print(title)

        # Extract product description
        product_description = soup.find('meta', {'name': 'description'})
        print(product_description['content'])

        # Extract universal_product_list (UPC) / tax (incl. & excl.) / number_available
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
        print(universal_product_code)
        print(price_including_tax)
        print(price_excluding_tax)
        print(number_available)

        # extract category
        ul = soup.find('ul', class_='breadcrumb')
        lis = ul.findAll('li')
        category = lis[2].text
        print(category)

        # Extract review_rating
        star_rating = soup.find(class_='star-rating')
        review_rating = star_rating['class'][1]
        print(review_rating)

        # Extract image_url
        active_image = soup.find(class_='item')
        image = active_image.find('img')
        image_url = image['src']
        path = url.rsplit('/', 1)[0]
        image_url = path + '/' + image_url

        # return du dictionnaire
        data_book = {'product_page_url': url, 'universal_product_code': universal_product_code, 'title': title, 'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax, 'number_available': number_available, 'category': category, 'review_rating': review_rating, 'image_url': image_url}
        return data_book

print(data_book_extract('http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html'))
