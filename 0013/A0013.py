from bs4 import BeautifulSoup
import requests

proxies = {
"http": "dev-proxy.oa.com:8080",
  "https": "dev-proxy.oa.com:8080",
}

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    html = requests.get(url, proxies=proxies)

    soup = BeautifulSoup(html.text, 'lxml')
    i = 1
    for item in soup.find_all('img'):
        link = item.get('src')
        if link is not None:
            if link.startswith('http://imgsrc.baidu.com/forum/w'):
                image = requests.get(link, proxies=proxies)
                if image.status_code == 200:
                    open(str(i) + '.jpg', 'wb').write(image.content)
                    i += 1