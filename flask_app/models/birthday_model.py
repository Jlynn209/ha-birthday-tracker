from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'birthday_db'

class Birthday:
    def __init__( self , data ):
        self.id = data['id']
        self.handle = data['handle']
        self.birthday = data['birthday']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# Pending transactions

    @classmethod
    def get_all_pending(cls):
        query = "SELECT * FROM pending;"

        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        for data in results:
            users.append( cls(data) )
        return users
    

    @classmethod
    def create_pending(cls, data):
        query = "INSERT INTO pending(handle, birthday) VALUES (%(handle)s, %(birthday)s);"

        results = connectToMySQL(DATABASE).query_db(query, data)

        return results
    

    @classmethod
    def delete_pending(cls, data):
        query =  "DELETE FROM pending WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod
    def get_one_pending(cls, data):
        query = "SELECT * FROM pending WHERE pending.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


# Approved birthdays

    @classmethod
    def get_all_birthdays(cls):
        query = "SELECT * FROM birthday_db.birthdays ORDER BY MONTH(birthday) ASC, DAY(birthday);"

        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        for data in results:
            users.append( cls(data) )
        return users
    

    @classmethod
    def create_birthday(cls, data):
        query = "INSERT INTO birthdays(handle, birthday) VALUES (%(handle)s, %(birthday)s);"

        results = connectToMySQL(DATABASE).query_db(query, data)

        return results
    

    @classmethod
    def delete_birthday(cls, data):
        query =  "DELETE FROM birthdays WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_one_birthday(cls, data):
        query = "SELECT * FROM birthdays WHERE birthday.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ### SET ###=%(###)s,###=%(###)s,###=%(###)s WHERE id = %(id)s;" 
    #     return connectToMySQL('NAME_OF_DATA_BASE').query_db(query,data)
            
