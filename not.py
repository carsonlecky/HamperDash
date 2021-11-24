import requests
from bs4 import BeautifulSoup

req = requests.get('https://docs.google.com/spreadsheets/d/1WfQ6Ccgfv6QAcVChW0itOKI-qBieeYZS55pZugiEvw0/edit?usp=sharing')
data = req.text

soup = BeautifulSoup(data, 'html.parser')

values = []

rows = soup.find_all('tr')
for row in rows:
    cols = row.find_all('td', {'class': 's8'})
    for col in cols: 
        if col == []:
            continue
        yeee = col.get_text()
        if yeee != '250': 
            values.append(yeee)


grade8 = values[0]
grade9 = values[1]
grade10 = values[2]
grade11 = values[3]
grade12 = values[4]

print(grade8)
print(grade9)
print(grade10)
print(grade11)
print(grade12)
