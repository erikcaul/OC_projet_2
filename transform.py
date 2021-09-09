import urllib.parse

def transform_category_url_list(raw_category_url_list):
    category_url_list = []
    for category_url in raw_category_url_list:
        base_url = 'http://books.toscrape.com/index.html'
        path = base_url.rsplit('/', 1)[0]
        category_url= urllib.parse.urljoin(path, category_url)
        category_url_list.append(category_url)
    return category_url_list


def transform_books_url_list_per_category(raw_books_url_list_per_category):
    product_page_url_list = []
    base_url = 'https://books.toscrape.com/catalogue/'
    for raw_book_url in raw_books_url_list_per_category:
        url_split = raw_book_url.rsplit('/', 2)[1:3]
        url_split_2 = url_split[0] + '/'
        product_page_url = urllib.parse.urljoin(base_url, url_split_2, url_split)
        # product_page_url = 'https://books.toscrape.com/catalogue/' + url_split[0] + '/' + url_split[1]
        product_page_url_list.append(product_page_url)
    return(product_page_url_list)

def transform_image_url(raw_image_url):
    url_split = raw_image_url.rsplit('/', 5)[1:6]
    image_url = 'http://books.toscrape.com'
    for i in url_split:
        image_url += '/' + i
    return image_url
