import os.path
from extract import extract_raw_category_url_list, extract_raw_books_url_list_per_category
from transform import transform_category_url_list, transform_books_url_list_per_category, transform_image_url
from load import load_data_book, load_book_img, load_data_books_in_csv_file

if __name__ == '__main__':
    if not os.path.exists('img_folder'):
        os.makedirs('img_folder')
    if not os.path.exists('img_folder'):
        os.makedirs('img_folder')
    category_url_list = transform_category_url_list(extract_raw_category_url_list("https://books.toscrape.com/index.html"))
    for category_url in category_url_list:
        product_page_url_list = transform_books_url_list_per_category(extract_raw_books_url_list_per_category(category_url))
        data_dict_list = []
        for product_page_url in product_page_url_list:
            data_dict = load_data_book(product_page_url)
            data_dict_list.append(data_dict)
            print(data_dict_list)
            load_book_img(product_page_url)

        load_data_books_in_csv_file(data_dict_list)



# séparer dans mon code l'extract (une fonction); le transform (une fonction) et le load (une fonction)
# dans un seul fichier ou dans 3
# Extract : données brutes
# Transform : générer les url transformées, nom des img.
# load : save_data
# dowload img à part

# mettre dans une BdD, API, fair eune application Qu'est-ce qui peut être fait à partir de ça