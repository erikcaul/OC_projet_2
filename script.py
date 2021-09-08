from extract_category_url_list import extract_category_url_list
from extract_books_url_list_per_category import extract_books_url_list_per_category
from save_data import data_saving

print(__name__)
if __name__ == '__main__':
    # function avec un chemin en paramètre facultatif
    # tester nombre de paramètre passé
    # si non : ./
    # si oui : passe le path en paramètre
    category_url_list = extract_category_url_list('http://books.toscrape.com/index.html')
    for category_url in category_url_list:
        url_list_per_category = extract_books_url_list_per_category(category_url)
        data_saving(url_list_per_category)

# séparer dans mon code l'extract (une fonction); le transform (une fonction) et le load (une fonction)
# dans un seul fichier ou dans 3
# Extract : données brutes
# Transform : générer les url transformées, nom des img.
# load : save_data
# dowload img à part

# mettre dans une BdD, API, fair eune application Qu'est-ce qui peut être fait à partir de ça