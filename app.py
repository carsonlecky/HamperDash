from flask import Flask, request, session, redirect, make_response, jsonify, render_template
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["SECRET_KEY"] = "5849035894735897234098579283475093847598"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def companydata():   

    return render_template('p.html')


def getValues(): 

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

    return values
    

@app.route('/values')
def values(): 

    values = getValues()

    return make_response(jsonify(values), 200)

@app.route('/post', methods=['POST'])
def post(): 

    try: 
        print(request.json())
    except: 
        print(request.text)

    return make_response('ok', 200)



if __name__ == "__main__":
    app.run(debug=True)
