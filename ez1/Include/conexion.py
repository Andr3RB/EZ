from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config["Debug"] = True
app.config['MYSQL_DATABASE_USER']= 'sepherot_danield'
app.config['MYSQL_DATABASE_PASSWORD']= 'N8BQy5yiH6Zz'
app.config['MYSQL_DATABASE_DB']= 'sepherot_danieldBD'
app.config['MYSQL_DATABASE_HOST']= 'nemonico.com.mx'

mysql = MySQL(app)