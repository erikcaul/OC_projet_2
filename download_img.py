import urllib.request

def download_img(image_url, upc):
    file_name = 'img_folder/' + upc + '.jpg'
    urllib.request.urlretrieve(image_url, file_name)

