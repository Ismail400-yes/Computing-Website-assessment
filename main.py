import sqlite3 as sql
from flask import Flask, render_template, request, redirect,flash
import database_manager

app = Flask(__name__, template_folder='templates_1')
app.secret_key = 'happy'

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/home_page')
def index():
    page = int(request.args.get('page', 1))
    data = database_manager.listExtension(page=page)
    return render_template('home_page.html', chat_pfp=data, page=page)

@app.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_input = request.form['email'].strip()
        password_input = request.form['password'].strip()

        # Connect to SQLite
        conn = sql.connect('data_source.db')
        cursor = conn.cursor()

        # Check for matching email and password
        cursor.execute("SELECT * FROM user-table WHERE Email = ? AND Password = ?", (email_input, password_input))
        result = cursor.fetchone()
        conn.close()

        if result:
            # Match found — redirect to homepage
            return redirect('/home_page')
        else:
            # No match — ask to retry
            flash("Invalid username or password. Please try again.")
            return redirect('/')

    return render_template('login_page.html')  # Show login form


@app.route('/friends_list')
def friends_list():
    return render_template('friends_list.html')

@app.route('/settings_page')
def settings_page():
    return render_template('settings_page.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/list_of_friends_page')
def list_of_friends_page():
    return render_template('list_of_friends_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)