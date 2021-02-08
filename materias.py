import requests
from bs4 import BeautifulSoup

url = 'https://bandcamp.com/'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

lista_materias = soup.find_all(class_='row bcdaily-stories')
for lista_titulos in lista_materias:
    lista = lista_titulos.find_all('h3', class_='bcdaily-title')
    titulos = []
    for lista_dados in lista:
        titulos.append(lista_dados.next_element)
        if lista_dados.next_element == 'The Best Electronic Music on Bandcamp: January 2021':
            break
    print(titulos)     

for lista_titulos in lista_materias:
    class_and_link = lista_titulos.find_all('a')
    links = []
    for link in class_and_link:
        links.append((link.get('href')))
        if link.get('href') == 'https://daily.bandcamp.com/best-electronic/the-best-electronic-music-on-bandcamp-january-2021':
            break
    print(links)

dict = {'titulo': titulos, 'link': links}

import pandas as pd
df = pd.DataFrame(dict)
print(df)

df.to_csv('materias.csv')
materias = pd.read_csv('materias.csv', index_col=0)







