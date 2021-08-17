import requests
from bs4 import BeautifulSoup

product_page_url_list = []
universal_product_code_list = []
titles = []
price_including_tax_list = []
price_excluding_tax_list = []
product_description_list = []
category_list = []
review_rating_list = []
image_url_list = []

for i in range(4):
    url ='http://books.toscrape.com/catalogue/category/books/fantasy_19/page-' + str(i) + '.html'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        h3s = soup.findAll('h3')
        lis = soup.findAll('li')
        for h3 in h3s:
            a = h3.find('a')
            product_page_url = a['href']
            product_page_url_list.append(product_page_url)
            title = a['title']
            titles.append(title)

        for li in lis:
            rating = soup.find_all("p", name)

        print(product_page_url_list)
        print(titles)

        """lis = soup.findAll('li')
        product_page_url = soup.find_all("a", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        print(product_page_url)
        for element in product_page_url:
            product_page_url_list.append(element)

        print(product_page_url_list)
        
        for li in lis:
            titres = soup.find_all("a", class_="gem-c-document-list__item-link")

            a = li.find('a')
            product_page_url = a['href']
            product_page_url_list.append(product_page_url)

"""
