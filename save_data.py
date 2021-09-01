import csv
import os


def data_saving(data_dict_list):
    data_dict_list = data_dict_list
    category = data_dict_list[0]['category']
    csv_file = 'csv_files/' + category + '.csv'
    fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                  'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    # os.path.dirname = récupère le chemin vers csv_file = renvoie le répertoire
    # os.path.exits = voir si un fichier ou répertoire existe
    # mettre les résultats ailleurs que dans le dossier projet
    # mettre le chemin vers le projet
    # os.makedirs = crée des sous-répertories jusqu'au fichier
    # à partir d'un path généré, créer un nom de fichier valide - remplacer un caractère par un autre
    # méthode pour vérifier que nom de fichier valide
    # faire un ppt
    try:
        if not os.path.exists('csv_files'):
            os.makedirs('csv_files')
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_dict_list:
                writer.writerow(row)

    except IOError:
        print('I/O error')
