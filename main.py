import requests
from bs4 import BeautifulSoup

def get_stats(url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}

    for table in soup.find_all('table', class_='table'):
        category_name = table.find('thead').text.strip()
        data[category_name] = {cells[0].text.strip(): cells[1].text.strip() for row in table.find_all('tr') if (cells := row.find_all('td')) and len(cells) == 2}

    return data

def run():
    clubs_url = "https://eredivisie.nl/competitie/clubs/"
    clubs_response = session.get(clubs_url)
    clubs_soup = BeautifulSoup(clubs_response.text, 'html.parser')
    clubs = clubs_soup.find('div', 'content-block')

    for club_link in clubs.find_all('a'):
        link = club_link.get('href')

        if link.startswith("https://eredivisie.nl/competitie/clubs/"):
            player_response = session.get(link + '#team-staff')
            player_soup = BeautifulSoup(player_response.text, 'html.parser')

            for player_card in player_soup.find_all('a', 'card-player'):
                player_url = player_card.get('href')
                print(player_url)
                print(get_stats(player_url))
                print('--\n')

if __name__ == "__main__":
    session = requests.Session()
    run()