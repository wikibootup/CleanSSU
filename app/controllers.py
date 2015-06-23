from flask import request, render_template
from app import app, models
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc

db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
	paymentinfos = models.PaymentInfo.query.order_by(desc(models.PaymentInfo.id))

	return render_template('index.html', paymentinfos=paymentinfos)

@app.route('/insertdata', methods=['GET', 'POST'])
def insertdata():

	if request.method=='POST':
		admin_group = request.form['admin_group']
		card_company = request.form['card_company']
		date_time = request.form['date_time']
		cost = request.form['cost']
		payment_store = request.form['payment_store']

		paymentinfo = models.PaymentInfo(admin_group=admin_group, card_company=card_company, date_time=date_time, cost=cost, payment_store=payment_store)
		db.session.add(paymentinfo)
		db.session.commit()

		return "OK!"

	if request.method=='GET':
		return "Hello, World!"