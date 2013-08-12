# -*- coding: utf-8 -*- 
from flask import json
from flask import Response
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def Dvz(): 
  DVZ = {
       "Dolar": [{'name': 'Amerikan doları'}, {'short': 'USD'}, {'place': 'USD'}, {'alıs':'1.914'}, {'satıs':'1.924'}],
       "Riyal": [{'name': 'Riyal'}, {'short': 'RL'}, {'place': 'Suudi Arabistan'},{'alıs':'0.5055'}, {'satıs':'0.5155'}],
       "Frank": [{'name': 'Frank'}, {'short': 'CFP'},  {'place': 'Fransa'}, {'alıs':'2.06'}, {'satıs':'2.085'}],
       "Euro": [{'name': 'Euro'}, {'short': 'EUR'}, {'place': 'Almanya'},{'alıs':'2.548'}, {'satıs':'2.563'}],
       "Sterlin": [{'name': 'Sterlin'}, {'short': 'GBP'}, {'place': 'Birleşik Krallık'}, {'alıs':'2.95'}, {'satıs':'2.995'}]
    }
  js = json.dumps(DVZ)
 
  resp = Response(js, status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
    app.run()
