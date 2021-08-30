import urllib.request

def download_img(url, file_name):
    urllib.request.urlretrieve(url, file_name)