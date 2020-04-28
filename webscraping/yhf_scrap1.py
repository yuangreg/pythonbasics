# pip install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, requests

url = "http://www.6vhao.tv/dy4/2018-09-15/34683.html"
response = urlopen(url)
content = response.read().decode("utf-8", "ignore")  # ignore errors when decode

soup = BeautifulSoup(content, features="html.parser")
download_links = soup.find_all('a', {'href': re.compile('ed2k.*')})


with open('links1.txt', 'w', encoding="utf-8") as f:
    for link in download_links:
        print(link['href'])
        f.write(link['href']+'\n')
