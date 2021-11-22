from flask import Flask, request, session, redirect, make_response, jsonify, render_template
from flask_mongoengine import MongoEngine
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "5849035894735897234098579283475093847598"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def companydata():   

    return render_template('p.html')


@app.route('/admin/')
def createCompany(): 

    return 'admin page'



if __name__ == "__main__":
    app.run(debug=True)
