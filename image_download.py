import urllib.request

def image_download(url, file_name):
    urllib.request.urlretrieve(url, file_name)

# image_download('http://books.toscrape.com/media/cache/9b/09/9b0935dc936c92900c2dc5d2114da72f.jpg', 'test_image.jpg')