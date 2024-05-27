from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB, app
from flask_app.controllers import users
from flask_app.controllers import products

from flask import Flask
from flask_mail import Mail

def get_db():
    return connectToMySQL(DB)

app.secret_key = 'word'  
mail = Mail(app)

# easily call DB in controller methods 
mySQL = get_db()

# run app/debug
if __name__ == "__main__":
    app.run(debug=True)
    
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'devCameronAngeleri@gmail.com'  
app.config['MAIL_PASSWORD'] = 'TempPass1!'   
app.config['MAIL_DEFAULT_SENDER'] = 'devCameronAngeleri@gmail.com'  

mail = Mail(app)