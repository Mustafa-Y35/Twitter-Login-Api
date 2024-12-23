import sqlite3
from flask import session

def userLogin(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = c.fetchone()
    conn.close()

    if stored_password and password == stored_password[0]:
        session["username"] = username
        return True
    else:
        return False

def userLogOut():
    if "username" in session:
        session.pop("username", None)
        return True
    return False

def getCurrentUsername():
    username = ""
    login_auth = False
    if "username" in session:
        username = session["username"]
        login_auth = True
    return username, login_auth
