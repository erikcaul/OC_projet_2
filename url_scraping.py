import requests
from bs4 import BeautifulSoup
import csv

product_page_url_list = []
product_page_short_url_list = []
universal_product_code_list = []
titles = []
price_including_tax_list = []
price_excluding_tax_list = []
number_available_list = []
product_description_list = []
category_list = []
review_rating_list = []
image_url_list = []

# faire une liste de livres
# pour chaque liste de livre, avoir une liste (ou tuple) de données
# utiliser des "named tuples" ou dict pour chacun des livres
# une méthode pour extraire les données d'un livre
# une méthode qui extrait tous les livres d'une category
# fonctions qui dépassent pas une page

# charger la donnée dans un fichier csv
def data_saving(file_name, fieldnames, product_page_url, universal_product_code_list, titles, price_including_tax_list, price_excluding_tax_list,
					number_available_list, product_description_list, category_list, review_rating_list, image_url_list):
	with open(file_name, 'w') as fichier_csv:
		writer = csv.writer(fichier_csv, delimiter=',')
		writer.writerow(fieldnames)
		# zip permet d'itérer sur deux listes à la fois
		for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, review_rating, category, image_url \
				in zip(product_page_url_list, universal_product_code_list, titles, price_including_tax_list, price_excluding_tax_list, number_available_list, product_description_list,
					   category_list, review_rating_list, image_url_list):
				writer.writerow([product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, review_rating, category, image_url])

"""# initialiser le fichier category.csv
def data_loading(file_name, product_page_url, universal_product_code_list, titles, price_including_tax_list, price_excluding_tax_list,
					number_available_list, product_description_list, category_list, review_rating_list, image_url_list):
	with open(file_name, 'w') as csv_file:
		fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
		writer.writeheader()
		for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, review_rating, category, image_url \
				in zip(product_page_url_list, universal_product_code_list, titles, price_including_tax_list,
					   price_excluding_tax_list, number_available_list, product_description_list,
					   category_list, review_rating_list, image_url_list):
		####	writer.writerow({'product_page_url': product_page_url, 'universal_product_code': universal_product_code, title, price_including_tax, price_excluding_tax,
							 number_available, product_description, review_rating, category, image_url})
# charger la donnée dans un fichier csv
def data_loading(file_name, champs, datas):
	with open(file_name, 'a') as csv_file:
		fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
					  'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
					  'image_url']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
		for data in datas:
			writer.writerow({champs: data})
"""
# data_init('fantasy.csv')
# Extraire les product_page_url en itérant sur chaque page
for i in range(4):
	# lien de la page à scrapper / transforme html (parse) en BeautiflSoup object
	url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-' + str(i) + '.html'
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.content, 'html.parser')
	# Récupérer toutes les url des pages de produit
		h3s = soup.findAll('h3')
		for h3 in h3s:
			a = h3.find('a')
			product_page_short_url = a['href']
			product_page_short_url_list.append(product_page_short_url)
			product_page_url_list.append('http://books.toscrape.com/catalogue/fantasy_19/page-' + str(i) + '.html' + product_page_short_url)
	# data_loading('fantasy.csv', 'product_page_url', product_page_url_list)

	for product_page_url in product_page_url_list:
		# print(product_page_url)
		url = product_page_url
		response = requests.get(url)
		if response.ok:
			soup = BeautifulSoup(response.content, 'html.parser')

			# Extract title
			title = soup.find('h1').text
			titles.append(title)
			# data_loading('fantasy.csv', 'title', titles)
			# print(title)

			# Extract product description
			product_description = soup.find('meta', {'name': 'description'})
			product_description_list.append(product_description['content'])
			# data_loading('fantasy.csv', 'product_description', product_description_list)
			# print(product_description['content'])

			# Extract universal_product_list (UPC) / tax (incl. & excl.) / number_available
			product_table_info = soup.find('table', class_="table table-striped")
			trs = product_table_info.findAll('tr')
			for tr in trs:
				th = tr.find('th')
				if th.text == 'UPC':
					universal_product_code = tr.find('td').text
					universal_product_code_list.append(universal_product_code)
					# data_loading('fantasy.csv', 'universal_product_code', universal_product_code_list)
				if th.text == 'Price (excl. tax)':
					price_excluding_tax = tr.find('td').text
					price_excluding_tax_list.append(price_excluding_tax)
					# data_loading('fantasy.csv', 'price_excluding_tax', price_excluding_tax_list)
				if th.text == 'Price (incl. tax)':
					price_including_tax = tr.find('td').text
					price_including_tax_list.append(price_including_tax)
					# data_loading('fantasy.csv', 'price_including_tax', price_including_tax_list)
				if th.text == 'Availability':
					number_available = tr.find('td').text
					number_available_list.append(number_available)
					# data_loading('fantasy.csv', 'number_available', number_available_list)
			"""print(universal_product_code)
			print(price_including_tax)
			print(price_excluding_tax)
			print(number_available)"""

			# Extract review_rating
			star_rating = soup.find(class_='star-rating')
			review_rating = star_rating['class'][1]
			review_rating_list.append(review_rating)
			# data_loading('fantasy.csv', 'review_rating', review_rating_list)
			# print(review_rating)

			# Extract image_url
			active_image = soup.find(class_='item')
			image = active_image.find('img')
			image_url = image['src']
			image_url_list.append(product_page_url + image_url)
			# data_loading('fantasy.csv', 'image_url', image_url_list)
			# print('http://books.toscrape.com/catalogue/unicorn-tracks_951/' + image_url)

category = 'fantasy'
category_list.append(category)
file_name = category + '.csv'
fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
data_saving(file_name, fieldnames, product_page_url_list, universal_product_code_list, titles, price_including_tax_list, price_excluding_tax_list,
					number_available_list, product_description_list, category_list, review_rating_list, image_url_list)

