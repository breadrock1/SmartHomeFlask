import json
import sqlite3
from pathlib import Path
from random import random
from hashlib import sha256

PATH_TO_DATABASE = ""
PATH_TO_SQL_FILE = ""

class Database(object):
    def __init__(self):
        self.connection = self.__init_connection()
        self.__init_database()


    '''     Init block      '''
    def __getPasswordHash(self, passwd) -> str:
        return sha256(passwd.encode('utf-8')).hexdigest()

    def __generateAPIKey(self, passwd) -> str:
        salt = str(random.random() % 100) + passwd
        return sha256(salt.encode('utf-8')).hexdigest()

    def __is_file_exist(self) -> bool:
        return Path(__file__).parent.joinpath('clients.db').exists()

    def __init_database(self) -> None:
        query = open(PATH_TO_SQL_FILE, 'r').read()

        try:
            curs = self.connection.cursor()
            curs.execute(query)
        except sqlite3.Error as e:
            print(f'Failed! While executing query: {e.__traceback__}')

    def __init_connection(self) -> sqlite3.Connection:
        if not self.__is_file_exist():
            print('Failed! The database file has not been founded')
            exit(-1)

        try:
            return sqlite3.connect(PATH_TO_DATABASE)
        except sqlite3.Error as e:
            print(f'Failed! While connecting to database: {e.__traceback__}')
            exit(-1)


    '''     Main block      '''
    def create_account(self, user, email, passwd) -> json:
        api = self.__generateAPIKey(passwd)
        passwd = self.__getPasswordHash(passwd)

        query = '''
            INSERT INTO users(
                                id,
                                user_login, 
                                user_pass, 
                                user_nickname, 
                                user_email,
                                user_registered
                                ) VALUES (DEFAULT, ?, ?, ?, ?, DEFAULT );
        '''

        try:
            curs = self.connection.cursor()
            curs.execute(query, [user, passwd, user, email])
            self.connection.commit()
        except sqlite3.Error as e:
            print(f'Failed! While executing query: {e.__traceback__}')
            return {"status": False, "msg": "Failed executing query: while signup new user"}

        return {"status": True, "api_key": api}

    def login_account(self, user, passwd) -> json:
        return {"status": True}

    def delete_account(self, apikey) -> json:
        if not self.validate_api_key(apikey):
            return {"status": False, "msg": "Failed! Specified API key does not exist"}

        query = f'''
            DELETE FROM users WHERE id = (
                SELECT id_user FROM apikeys WHERE apikey = {apikey}
            );
        '''

        try:
            curs = self.connection.cursor()
            curs.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f'Failed! While executing query: {e.__traceback__}')
            return {"status": False, "msg": "Failed executing query: while delete user"}

        return {"status": True}

    def get_api_key(self, user, passwd) -> json:
        api_key = ""
        passwd = self.__getPasswordHash(passwd)

        query = f'''
            SELECT apikey FROM apikeys WHERE id_user = (
                SELECT id FROM users WHERE user_login="{user}" AND user_pass="{passwd}
            );
        '''

        try:
            curs = self.connection.cursor()
            curs.execute(query)
            self.connection.commit()
            api_key = list(curs.fetchone())[0]
        except sqlite3.Error as e:
            print(f'Failed! While executing query: {e.__traceback__}')
            return {"status": False, "msg": "Failed executing query: while getting user API key"}

        return {"status": True, "api_key": api_key}

    def reset_api_key(self, user, apikey, passwd) -> json:
        return {"status": True, "api_key": apikey}

    def validate_api_key(self, apikey) -> bool:
        query = f'''
            SELECT COUNT(*) FROM apikeys WHERE apikey = {apikey};
        '''

        try:
            curs = self.connection.cursor()
            curs.execute(query)
            result = list(curs.fetchone())[0]
            if result > 0: return True
        except sqlite3.Error as e:
            print(f'Failed! While executing query: {e.__traceback__}')

        return False