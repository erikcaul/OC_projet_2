import csv


def data_saving(data_dict_list):
    data_dict_list = data_dict_list
    category = data_dict_list[0]['category']
    csv_file = 'csv_files/' + category + '.csv'
    fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                  'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for row in data_dict_list:
                writer.writerow(row)

    except IOError:
        print('I/O error')
