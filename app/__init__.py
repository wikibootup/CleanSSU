from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#Fix location This code
from app import models, controllers

# u = models.PaymentInfo(admin_group='dongyeon', card_company='sinhan', date_time='20150622', cost='10000', payment_store='Club')
# db.session.add(u)
# db.session.commit()

# print("Success!")

# paymentinfos = models.PaymentInfo.query.all()

# for item in paymentinfos:
# 	print(item.id, item.admin_group)
