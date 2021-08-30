import csv

def data_file_init(category):
    # creation csvfile
    """data_dict = data_dict
    category = data_dict['category']"""
    csv_file = 'csv_files/' + category + '.csv'
    fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                  'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    except IOError:
        print('I/O error')

def data_saving(data_dict):
    data_dict = data_dict
    category = data_dict['category']
    csv_file = category + '.csv'
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, data_dict.keys())
            writer.writerow({'product_page_url': data_dict['product_page_url'], 'universal_product_code': data_dict['universal_product_code'], 'title': data_dict['title'], 'price_including_tax': data_dict['price_including_tax'], 'price_excluding_tax': data_dict['price_excluding_tax'], 'number_available': data_dict['number_available'], 'product_description': data_dict['product_description'], 'category': data_dict['category'], 'review_rating': data_dict['review_rating'], 'image_url': data_dict['image_url']})
            #for data in data_dict:
                #print(data)
                #print(data_dict[data])
                #item = data_dict[data]
                #print(type(item))
                # writer.writerow({data: data_dict[data]})
                # writer.writerow({'product_page_url': data['product_page_url'], 'universal_product_code': data['universal_product_code'], 'title': data['title'], 'price_including_tax': data['price_including_tax'], 'price_excluding_tax': data['price_excluding_tax'], 'number_available': data['number_available'], 'product_description': data['product_description'], 'category': data['category'], 'review_rating': data['review_rating'], 'image_url': data['image_url']})

    except IOError:
        print('I/O error')

