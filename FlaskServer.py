import json

from flask import Flask
from flask import abort
from flask import request
from flask import sessions
from flask import render_template

from src.config import *
from src.database.Database import Database


app = Flask(__name__, template_folder=TEMPLATE_DIR)


def loadJsonData(data) -> json:
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        print(f'[-]\tFailed to decode json data. Error: {e.msg}')
        return {'result': -1, 'message': e.msg}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


'''
    DATABASE BLOCK
'''
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')

    if request.method == 'POST':
        if request.form:
            try:
                username    = request.form.get('user')
                email       = request.form.get('email')
                password    = request.form.get('password')
                r_password  = request.form.get('r_password')

            except Exception as e:
                print(f'[-]\tFailed to get credentials from post-form. Error: {e}')
                return {'result': -1, 'message': e}

        else:
            data = request.get_data().decode('UTF-8')
            json_data = loadJsonData(data)

            try:
                username    = json_data.get('username')
                email       = json_data.get('email')
                password    = json_data.get('password')
                r_password  = json_data.get('r_password')

            except KeyError as e:
                print(f'[-]\tFailed to get credentials from post-request. Error: {e}')
                return {'result': -1, 'message': e}

        database = Database()
        database.create_account(user=username, email=email, passwd=password, r_passwd=r_password)

    abort(405)


@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')

    if request.method == 'POST':
        if request.form:
            try:
                username = request.form.get('user')
                password = request.form.get('password')

            except Exception as e:
                print(f'[-]\tFailed to get credentials from post-form. Error: {e}')
                return {'result': -1, 'message': e}

        else:
            data = request.get_data().decode('UTF-8')
            json_data = loadJsonData(data)

            try:
                username = json_data.get('username')
                password = json_data.get('password')

            except KeyError as e:
                print(f'[-]\tFailed to get credentials from post-request. Error: {e}')
                return {'result': -1, 'message': e}

        database = Database()
        database.login_account(user=username, passwd=password)

    abort(405)


@app.route('/logout')
def logout():
    pass


@app.route('/get_apikey')
def get_apikey():
    pass


@app.route('/reset_apikey')
def reset_apikey():
    pass


'''
    MAIN BLOCK
'''
@app.route('/')
def test():
    pass


if __name__ == "__main__":
    port = 8080
    host = "0.0.0.0"
    app.run(host=host, port=port)