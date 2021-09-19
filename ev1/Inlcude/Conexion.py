from flask import Flask
from flaskext.mysql import MySQL

app = Flask(_name_)
app.config["Debug"] = True
app.config['MYSQL_DATABASE_USER']= 'sepherot_andrer'
app.config['MYSQL_DATABASE_PASSWORD']= 'QxS7HbzfXBIb'
app.config['MYSQL_DATABASE_DB']= 'sepherot_andrerBD'
app.config['MYSQL_DATABASE_HOST']= 'nemonico.com.mx'

mysql = MySQL(app)