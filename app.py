from flask import Flask, request, render_template, redirect, url_for, session
from db import conn

app = Flask(__name__)
app.secret_key = 'this_is_a_secret_key'

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
        cur.close()
        print(user)
        if user:
            session['username'] = user[1]
            return redirect('/profile')
        else:
            return "Invalid credentials!"

    return render_template('login.html')
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Nếu chưa đăng nhập, redirect đến trang đăng nhập
    if 'username' not in session:
        return redirect(url_for('login'))

    # Nếu đã đăng nhập, hiển thị trang profile
    username = session['username']
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cur.execute(query)
    user = cur.fetchone()
    cur.close()
    
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        user_id = user[0]
        email = request.form['email']
        age = request.form['age']

        # Cập nhật thông tin người dùng trong cơ sở dữ liệu
        cur = conn.cursor()
        query = f"UPDATE users SET email = {email}, age = {age} WHERE user_id = {user_id}"
        cur.execute(query)
        cur.close()
    if not user:
        return "User not found!"
    else:
        # Hiển thị thông tin người dùng
        return render_template('profile.html',user_id=user[0], username=user[1], email=user[3], age=user[4])
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
