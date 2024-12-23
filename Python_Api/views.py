from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from controllers import userLogin, userLogOut, getCurrentUsername

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/login", methods=["POST"])
def api_login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username']
    password = data['password']

    if userLogin(username, password):
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route("/logout", methods=["POST"])
def api_logout():
    if userLogOut():
        return jsonify({"message": "Logout successful"}), 200
    else:
        return jsonify({"error": "No user currently logged in"}), 400

@app.route("/current-user", methods=["GET"])
def api_current_user():
    username, login_auth = getCurrentUsername()
    if login_auth:
        return jsonify({"username": username, "message": "User is logged in"}), 200
    else:
        return jsonify({"error": "No user logged in"}), 401

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            if userLogin(username, password):
                flash("Giriş başarılı")
                return redirect(url_for("login"))
            else:
                flash("Giriş başarısız: Kullanıcı adı veya şifre yanlış")
                return redirect(url_for("login"))
        else:
            flash("Kullanıcı adı ve şifre girilmelidir")
            abort(400)
    
    username, login_auth = getCurrentUsername()
    return render_template("index.html", username=username, login_auth=login_auth)

@app.route("/logout", methods=["GET"])
def logOut():
    if userLogOut():
        flash("Çıkış başarılı")
        return redirect(url_for("login"))
    else:
        flash("Henüz giriş yapılmış bir kullanıcı yok")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
