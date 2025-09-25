import sqlite3
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates_1')

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/friends_list')
def friends_list():
    return render_template('friends_list.html')

@app.route('/settings_page')
def settings_page():
    return render_template('settings_page.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/')
def index():
    conn = sqlite3.connect('database/data_source.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 'Chat Image Link', Title FROM conversation-table")
    conversation_table = cursor.fetchall()
    conn.close()
    return render_template('home_page.html', chat_pfp=conversation_table)


if __name__ == '__main__':
    app.run(debug=True)