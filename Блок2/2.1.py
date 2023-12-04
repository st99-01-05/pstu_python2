import requests
from bs4 import BeautifulSoup
import json

def scrape_airport_codes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    airport_data = {}
    table = soup.find('table', {'class': 'wikitable'})

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            if len(columns) >= 4:
                iato = columns[0].get_text().strip()
                icao = columns[1].get_text().strip()
                iata_code = columns[2].get_text().strip()
                airport_data[iata_code] = {'IATO': iato, 'ICAO': icao}

    return airport_data

def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def get_airport_code(airport_data, name, language='en'):
    for airport_name in airport_data.keys():
        if airport_name.lower() == name.lower():
            return [airport_data[airport_name]['IATO'], airport_data[airport_name]['ICAO']]
    return None

def Merge(dict1, dict2):
    return(dict1.update(dict2))

if __name__ == "__main__":
    alphabet = ['A','B','C','D','E','F',
                'G','H','I','J','K','L',
                'M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z']
    wikipedia_url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_"
    # Собираем данные
    airport_data = {}
    for ch in alphabet:
        if airport_data != {}:
            Merge(airport_data, scrape_airport_codes(wikipedia_url+ch))
        else:
            airport_data = scrape_airport_codes(wikipedia_url+ch)

    save_data_to_json(airport_data, 'airport_codes.json')

    airport_name = input('Введите название аэропорта: ')
    code = get_airport_code(airport_data, airport_name, language='en')
    if code:
        print(f"IATA и IKAO коды для {airport_name}: {code}")
    else:
        print(f"Аэропорт с названием '{airport_name}' не найден.")