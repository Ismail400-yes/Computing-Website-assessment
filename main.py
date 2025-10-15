import sqlite3 as sql
from flask import Flask, render_template, request, redirect,flash
import database_manager

app = Flask(__name__, template_folder='templates_1')
app.secret_key = 'happy'

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    data = database_manager.listExtension(page=page)
    return render_template('home_page.html', chat_pfp=data, page=page)

@app.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_input = request.form.get['email'].strip()
        password_input = request.form.get['password'].strip()

        conn = sql.connect('database/data_source.db')
        cursor = conn.cursor()

        query = """
        SELECT Email, Password
        FROM user_table
        WHERE Email = ? AND Password = ?
        """
        cursor.execute(query, (email_input, password_input))
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

@app.route('/messages_page', methods=['GET', 'POST'])
def messages():
    conn = sql.connect('database/data_source.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        sender = request.form['sender'].strip()
        content = request.form['content'].strip()
        cursor.execute("INSERT INTO messages (sender, content) VALUES (?, ?)", (sender, content))
        conn.commit()

    cursor.execute("SELECT sender, content, timestamp FROM messages ORDER BY timestamp DESC")
    all_messages = cursor.fetchall()
    conn.close()

    return render_template('messages_page.html', messages=all_messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)