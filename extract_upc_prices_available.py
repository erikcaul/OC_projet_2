import requests
from bs4 import BeautifulSoup


def extract_upc_prices_available(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
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
        product_info_data = {'universal_product_code': universal_product_code,
                             'price_including_tax': price_including_tax, 'price_excluding_tax': price_excluding_tax,
                             'number_available': number_available}
        return product_info_data
