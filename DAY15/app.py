from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login",methods=['POST', 'GET'])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
































# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/profile')
# def profile():
#     return render_template(
#         "profile.html",
#         name = "Alex",
#         age = 25,
#         skills = ["Python","Flask","Security"]
#     )

# if __name__ == "__main__":
#     app.run(debug=True,port=8000)
