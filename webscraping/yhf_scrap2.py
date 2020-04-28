from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://www.gaoqingxiazai.com/xz/32355.html"
response = urlopen(url)
content = response.read().decode("utf-8", "ignore")

soup = BeautifulSoup(content, features="html.parser")
course_links = soup.find_all('input', {'class': 'down_url'})


with open('links2.txt', 'w', encoding="utf-8") as f:
    for link in course_links:
        print(link['value'])
        f.write(link['value']+'\n')