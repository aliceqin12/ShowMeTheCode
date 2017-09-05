import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://github.com/Show-Me-the-Code/show-me-the-code'
html = requests.get(url)

soup = BeautifulSoup(html.text, "lxml")
print(soup.get_text())