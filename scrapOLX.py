from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


url = 'https://www.olx.com.br/imoveis'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
req = Request(url, headers = headers)
response = urlopen(req)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
cards = []
card = {}
anuncio = soup.find('li', {'class': 'sc-1fcmfeb-2 ggOGTJ'})
(anuncio.find('p', {'class': 'fnmrjs-16 jqSHIm'} ).getText())
card['value'] = (anuncio.find('p', {'class': 'fnmrjs-16 jqSHIm'} ).getText())
print(card)
