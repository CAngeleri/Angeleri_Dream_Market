from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from datetime import datetime

class Product:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.stock = data['stock']
        self.sku = data['sku']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.image_path = data['image_path']

    @classmethod
    def get_by_id(cls, product_id):
        query = 'SELECT * FROM products WHERE id = %(id)s'
        data = {'id':  product_id}
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM products'
        results = connectToMySQL(DB).query_db(query)
        products = [cls(row) for row in results]
        return products

    @classmethod
    def save(cls, data):
        query = '''
            INSERT INTO products (name, description, price, stock, sku, category_id)
            VALUES (%(name)s, %(description)s, %(price)s, %(stock)s, %(sku)s, %(category_id)s)
        '''
        new_product_id = connectToMySQL(DB).query_db(query, data)
        return new_product_id

    @classmethod
    def delete(cls, id):
        query = 'DELETE FROM products WHERE id = %(id)s;'
        data = {'id': id}
        connectToMySQL(DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = '''
            UPDATE products
            SET name = %(name)s,
                description = %(description)s,
                price = %(price)s,
                stock = %(stock)s,
                sku = %(sku)s,
                category_id = %(category_id)s
            WHERE id = %(id)s
        '''
        connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_product(name, description, price, stock, sku, category_id):
        is_valid = True
        flash_messages = []

        if len(name) < 3:
            flash_messages.append('Name must be at least 3 characters long.')
            is_valid = False

        if len(description) < 3:
            flash_messages.append('Description must contain at least 3 characters.')
            is_valid = False

        if not price:
            flash_messages.append('Please provide a price.')
            is_valid = False

        if not stock:
            flash_messages.append('Please provide stock information.')
            is_valid = False

        if not sku:
            flash_messages.append('Please provide a SKU.')
            is_valid = False

        if not category_id:
            flash_messages.append('Please provide a category ID.')
            is_valid = False

        return is_valid, flash_messages
