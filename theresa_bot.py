# -*- coding: utf-8 -*-
"""
	Code written entirely by Eric Alcaide: https://github.com/EricAlcaide

	First bot in Python practice. Will send some inspirational quotes
	to begin the day freshly or to help ocercome those bad moments.

	Will be your best bot-friend! Telegram Version
"""

#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
from keras.models import load_model
import numpy as np 
import pandas as pd 
from random import randint
import sys
import json

app = Flask(__name__)

placeholders = {'Sustainability':'/api/twitter/renfe/','Traffic':'/api/incidents/origin/','IoT':''}

@app.route('/')
def web():
	return render_template('index.html')

@app.route('/register/')
def register():
	return render_template('register.html')

@app.route('/registered/',  methods = ['POST'])
def registered():
	# Write it to a csv file
	name = str(request.form['full_name'])
	email = str(request.form['email_name'])
	key = str(randint(0, 100000000))
	# Extract data and append the new register
	with open('users_data.csv', 'a') as f:
		f.write("\n")
		f.write(str(name+','+email+','+key))

	return render_template('registered.html', key = key)

@app.route('/api/',  methods = ['POST'])
def api():
	# Only accept transaction if valid
	keys = pd.read_csv('users_data.csv', delimiter=",").iloc[:, 2].values.tolist()
	print(1)
	try:
		print(int(request.form['key']))
		print(keys)
		# if int(request.form['key']) in keys:
		if True:
			print(2)
			# Make prediction
			try:
				model = load_model('predict_4d_short_100_long_2_2000_renkos_0_3.h5')
				data = np.array(request.form['data'])
				return json.dumps(data)
				# if len(data.shape) == 3 and data.shape[-2:] == (444,4):
				if True:
					pred = model.predict(data)
					print(4)
					return {'prediction': pred}
				else:
					print(5)
					return "Array of unexpected shape"
			except:
				print(3.1)
				return "Unexpected error"
		else:
			print(2.1)
			return "Key not accepted"
	except Exception as e:
		print(1.1)
		return {'exception': e}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
