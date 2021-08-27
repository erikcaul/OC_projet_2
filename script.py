from category_url_list_extract import category_url_list_extract
from category_books_extract import books_url_list_per_category
from extract_category import extract_category
from data_book_extract import data_book_extract
from save_data import data_saving
from save_data import data_file_init

category_url_list = category_url_list_extract('http://books.toscrape.com/index.html')
for category_url in category_url_list:
    url_list_per_category = books_url_list_per_category(category_url)
    category = extract_category(url_list_per_category[0])
    data_file_init(category)
    for book_url in url_list_per_category:
        data_book = data_book_extract(book_url)
        data_saving(data_book)
