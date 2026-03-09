# from flask import Flask, redirect, request, render_template, url_for

# app = Flask(__name__)

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html", name = "Payal")

# @app.route("/login",methods = ["GET","POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         print(username, password)

#         if username == "admin" and password == "pass":
#             # return redirect(url_for('dashboard', username == username, password == password))
#             return redirect(url_for('dashboard'))
        
        
#         else : 
#             return redirect(url_for('error_page'))
        
#     return render_template("login.html")
    
# @app.route("/error")
# def error_page():
#     return render_template("error.html")

# @app.route("/dashboard")
# def dashboard():
#     username = request.args.get("username")
#     return render_template("dashboard.html",username=username)

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)




from flask import Flask, redirect, request, render_template, url_for
import requests

app = Flask(__name__)

# Home Route
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", name="Payal")


# Login Route (GET + POST in same route)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print("Username:", username)
        print("Password:", password)

        if username == "admin" and password == "pass":
            return redirect(url_for("dashboard", username=username))
        else:
            return render_template("error.html")

    return render_template("login.html")


# Dashboard Route
@app.route("/dashboard")
def dashboard():
    username = request.args.get("username")
    return render_template("dashboard.html", username=username)



url = "https://jsonplaceholder.typicode.com/posts"
user_id = 1
resonse = requests.get(url,params = {'userId': user_id})
# Run Server
if __name__ == "__main__":
    app.run(debug=True, port=8000)
