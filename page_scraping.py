import requests
from bs4 import BeautifulSoup

### product_page_url_list = []
universal_product_code_list = []
titles = []
price_including_tax_list = []
price_excluding_tax_list = []
product_description_list = []
### category_list = [] == Fantasy ??
review_rating_list = []
image_url_list = []

url = 'http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title = soup.find('h1').text
    print(title)

    # Extract product description
    product_description = soup.find('meta', {'name': 'description'})
    print(product_description['content'])

    # Extract universal_product_list (UPC) / tax (incl. & excl.)
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
    print(universal_product_code)
    print(price_including_tax)
    print(price_excluding_tax)

    # Extract review_rating
    ps = soup.findAll('p')

    for p in ps:
        rating = soup.find_all("p", class_="star-rating One")
        if rating:
            print(rating)
            break
        rating = soup.find_all("p", class_="star-rating Two")
        if rating:
            print(rating)
            break
        rating = soup.find_all("p", class_="star-rating Three")
        if rating:
            print(rating)
            break
        rating = soup.find_all("p", class_="star-rating Four")
        if rating:
            print(rating)
            break
        rating = soup.find_all("p", class_="star-rating Five")
        if rating:
            print(rating)
            break

    # print(review_rating)

    # Extract impage_url
