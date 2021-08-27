import csv

def data_saving(data_dict):
    csv_columns = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    data_dict = data_dict
    category = data_dict['category']
    csv_file = '_' + category + '_' + '.csv'
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in data_dict:
                writer.writerow(data)
    except IOError:
        print('I/O error')

