# pip install requests
import requests


def get():
    r = requests.get("https://www.gaoqingxiazai.com/xz/32355.html")
    print(r.url)
    print(r.text)


def post_name():
    # http://pythonscraping.com/pages/files/form.html
    # Check from Inspect -> Network -> Preserve log
    data = {'firstname': 'greg', 'lastname': 'yuan'}
    r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
    print(r.text)


def post_image():
    # http://pythonscraping.com/files/form2.html
    file = {'uploadFile': open('./image.jpg', 'rb')}
    r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
    print(r.text)


def post_login():
    # http://pythonscraping.com/pages/cookies/login.html
    payload = {'username': 'greg', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())
    # http://pythonscraping.com/pages/cookies/profile.php
    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    print(r.text)


def session_login():
    # http://pythonscraping.com/pages/cookies/login.html
    session = requests.Session()
    payload = {'username': 'greg', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())
    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(r.text)


#get()
#post_name()
#post_image()
#post_login()
#session_login()