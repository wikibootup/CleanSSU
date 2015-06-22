from flask import request
from app import app

#Api write
@app.route('/insertdata', methods=['GET', 'POST'])
def insertdata():

	if request.method=='POST':
		admin_group = request.form['admin_group']
		card_company = request.form['card_company']
		date_time = request.form['date_time']
		cost = request.form['cost']
		payment_store = request.form['payment_store']

		return payment_store

	if request.method=='GET':
		return "Hello, World!"

