import requests
from bs4 import BeautifulSoup

keyword = 'hyper crimson'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

url = 'https://www.kith.com/sitemap_products_1.xml'

r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

for items in soup.find_all("url"):
    item = items.find("image:title")
    if item is not None:
        title = item.text
        url = items.find("loc").text
        time = items.find("lastmod").text
        if keyword.lower() in title.lower():
            print(title, url, time)


