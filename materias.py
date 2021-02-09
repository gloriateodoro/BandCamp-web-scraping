import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://bandcamp.com/'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

lista_materias = soup.find_all(class_='row bcdaily-stories')
for lista_titulos in lista_materias:
    lista = lista_titulos.find_all('h3', class_='bcdaily-title')
    titulos = []
    for lista_dados in lista[:10]:
        titulos.append(lista_dados.next_element)
    class_and_link = lista_titulos.find_all('a')
    links = []
    for link in class_and_link[:10]:
        links.append((link.get('href')))
        
dict = {'titulo': titulos, 'link': links}
df = pd.DataFrame(dict)
df.to_csv('materias.csv')








