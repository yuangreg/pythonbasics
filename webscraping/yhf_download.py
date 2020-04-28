IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"


def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './images/image1.png')      # whole document


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./images/image2.png', 'wb') as f:
        f.write(r.content)                      # whole document


def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)    # stream loading

    with open('./images/image3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


urllib_download()
print('downloaded image1')
request_download()
print('downloaded image2')
chunk_download()
print('downloaded image3')