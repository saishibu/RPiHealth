#!/usr/bin/python3
import datetime,sys,os,io
from flask import Flask, jsonify,request
from flaskext.mysql import MySQL
import random
app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")

@app.route('/')
def API1():
	data = {'EnergyAvailability':round(random.uniform(0,10),2),'CostPerUnit':round(random.uniform(1,6),2)}
	return jsonify(data)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=2020,debug=1)
