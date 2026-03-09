from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple hardcoded authentication
        if username == "admin" and password == "1234":
            message = "Login Successful!"
        else:
            message = "Invalid Credentials"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
