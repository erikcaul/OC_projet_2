import requests
from bs4 import BeautifulSoup
import csv


# Extraire les données
def extraire_donnees(elements):
	resultat = []
	for element in elements:
		resultat.append(element.string)
	return resultat


# charger la donnée dans un fichier csv
def charger_donnees(nom_fichier, en_tete, titres, descriptions):
	with open(nom_fichier, 'w') as fichier_csv:
		writer = csv.writer(fichier_csv, delimiter=',')
		writer.writerow(en_tete)
		# zip permet d'itérer sur deux listes à la fois
		for titre, description in zip(titres, descriptions):
			writer.writerow([titre, description])

# extraire les product_page_url en itérant sur chaque page
def etl():
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
				product_page_url_list.append(product_page_url)

	en_tete = ["title", "description"]
	titres = extraire_donnees(titres)
	descriptions = extraire_donnees(descriptions)
	charger_donnees("data.csv", en_tete, titres, descriptions)


etl()
"""
	# récupération de tous les titres
	titres = soup.find_all("a", class_="gem-c-document-list__item-link")
	# récupération de toutes les descriptions
	descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
"""