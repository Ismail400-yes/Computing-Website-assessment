import sqlite3 as sql
from flask import Flask, render_template
from flask import request
import database_manager

app = Flask(__name__, template_folder='templates_1')

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    data = database_manager.listExtension(page=page)
    return render_template('home_page.html', chat_pfp=data, page=page)

@app.route('/friends_list')
def friends_list():
    return render_template('friends_list.html')

@app.route('/settings_page')
def settings_page():
    return render_template('settings_page.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)