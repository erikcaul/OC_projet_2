from extract_category_url_list import extract_category_url_list
from extract_books_url_list_per_category import extract_books_url_list_per_category
from extract_category import extract_category
from extract_transf_books_data import extract_transf_books_data
from save_data import data_saving
from save_data import data_file_init

category_url_list = extract_category_url_list('http://books.toscrape.com/index.html')
for category_url in category_url_list:
    url_list_per_category = extract_books_url_list_per_category(category_url)
    category = extract_category(url_list_per_category[0])
    data_file_init(category)
    for book_url in url_list_per_category:
        data_book = extract_transf_books_data(book_url)
        data_saving(data_book)
