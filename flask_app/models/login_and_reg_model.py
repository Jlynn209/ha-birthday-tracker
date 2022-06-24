from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


DATABASE = 'birthday_db'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.pw = data['pw']
        self.role = data['role']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def get_one_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


    @classmethod
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    
    @staticmethod
    def validate_reg(user):
        is_valid = True
        
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 character.", "err_reg")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 character.", "err_reg")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("invalid email address!", "err_reg")
            is_valid = False
        if len(user['pw']) < 6:
            flash("password must be at least 6 character.", "err_reg")
            is_valid = False
        if user['pw'] != user['confirmed_pw']:
            flash("password must match.", "err_reg")
            is_valid = False
        return is_valid
