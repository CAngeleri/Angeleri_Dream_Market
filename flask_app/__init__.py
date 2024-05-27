# importing Flask and creating our app
from flask import Flask
app = Flask(__name__)
app.secret_key = "word"
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)



# creating global var of DB 'name_of_schema' in MySQL
DB = 'dream_market_schema'

