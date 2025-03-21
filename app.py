from flask import Flask, request, render_template
from db import conn

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Truy vấn sql
        cur = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cur.execute(query)
        user = cur.fetchone()

        if user:
            return f"Welcome {user[1]}!"
        else:
            return "Invalid credentials!"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
