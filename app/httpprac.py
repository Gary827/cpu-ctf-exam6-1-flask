from flask import Flask,render_template, request,redirect, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("rabbit"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
@auth.login_required
def index1():
    str1 = "Hello "+ auth.current_user() +"!" + " The Flag is CTF{H77p_B@s1c_@uth0r1zat1on_1$_n0t_secure}"
    return str1
    # return "Hello, Flag is CTF{'H77p_B@s1c_@uth0r1zat1on_1$_n0t_secure'}".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

