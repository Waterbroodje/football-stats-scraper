import requests
from bs4 import BeautifulSoup

url = "https://eredivisie.nl/clubs/feyenoord/spelers/santiago-tomas-gimenez/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find('div', class_='table-wrapper-grid')
for x in tables.find_all('table', class_='table'):
    cat = x.find('th', class_='table__th')
    print("Categorie: " + cat.text.strip())

    for y in x.find_all('td'):
        print(y.text.strip())