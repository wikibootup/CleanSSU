from app import db

class PaymentInfo(db.Model):

	id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
	admin_group = db.Column(db.String(128), nullable=False)
	card_company = db.Column(db.String(128), nullable=False)
	date_time = db.Column(db.String(128), nullable=False)
	cost = db.Column(db.Integer(), nullable=False)
	payment_store = db.Column(db.String(128), nullable=False)

	def __init__(self, admin_group, card_company, date_time, cost, payment_store):
		self.admin_group = admin_group
		self.card_company = card_company
		self.date_time = date_time
		self.cost = cost
		self.payment_store = payment_store

	def __repr__(self):
		return '<PaymentInfo %r>' % (self.payment_store)
