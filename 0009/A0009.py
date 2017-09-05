from bs4 import BeautifulSoup
import  requests

url = 'https://github.com/Show-Me-the-Code/show-me-the-code'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
for item in soup.find_all('a'):
    link = item.get('href')
    if link is not None:
        if link.startswith(r'http://') or link.startswith(r'https://'):
            print(link)