from category_url_list_extract import category_url_list_extract
from category_books_extract import category_books_extract
from data_book_extract import data_book_extract
from save_data import data_saving

category_url_list = category_url_list_extract('http://books.toscrape.com/index.html')
for category_url in category_url_list:
    books_url_list_per_category = category_books_extract(category_url)
    for book_url in books_url_list_per_category:
        data_book = data_book_extract(book_url)
        print(data_book)
        data_saving(data_book)

