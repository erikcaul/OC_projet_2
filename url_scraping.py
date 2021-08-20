import requests
from bs4 import BeautifulSoup
import csv

# charger la donnée dans un fichier csv
def data_loading(file_name, champs, datas):
	with open(file_name, 'w') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(champs)
		# zip permet d'itérer sur deux listes à la fois
		for data in datas:
			writer.writerow(data)

# Extraire les product_page_url en itérant sur chaque page
product_page_url_list = []
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
			product_page_url = a['href']
			product_page_url_list.append('http://books.toscrape.com/catalogue/fantasy_19/page-1.html' + product_page_url)
	data_loading('data.csv', 'product_page_url', product_page_url_list)

	for product_page_url in product_page_url_list:
		print('http://books.toscrape.com/catalogue/fantasy_19/page-1.html' + product_page_url)



