from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class PreUser:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.city = data['city']
        self.state = data['state']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, form_data):
        query = '''
        INSERT INTO pre_user (first_name, last_name, email, city, state, message) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(city)s, %(state)s, %(message)s)
        '''
        return connectToMySQL(DB).query_db(query, form_data)

    
    ### Pre-User Validations ###
    
    @staticmethod
    def validate_pre_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('First name must contain at least 3 letters', 'register')
            is_valid = False

        if len(data['last_name']) < 2:
            flash('Last name must contain at least 3 letters', 'register')
            is_valid = False

        if len(data['email']) < 5 or not EMAIL_REGEX.match(data['email']):
            flash('Please enter a valid email address', 'register')
            is_valid = False
            
        if len(data['city']) < 2:
            flash('Please enter a valid city', 'register')
            is_valid = False
            
        if len(data['state']) < 2:
            flash('Please enter a valid state', 'register')
            is_valid = False

        if len(data['message']) < 5:
            flash('Message must contain at least 5 characters', 'register')
            is_valid = False

        return is_valid
