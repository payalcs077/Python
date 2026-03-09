from flask import Flask, render_template, request, url_for ,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is homepage</h1>"

@app.route("/login", methods = ["GET","POST"])
def login():
    dataincoming = ""
    if  request.method == "POST":
        dataincoming = request.form.get("input_data")
        dataincoming_p = request.form.get("input_password")
        print(dataincoming)
        return redirect(url_for("dashboard",dataincoming = dataincoming, dataincoming_p=dataincoming_p))
    return render_template("login.html",dataincoming = dataincoming)

# @app.route("/dashboard/")
# def dashboard(dataincoming ,dataincoming_p):
    
#     return render_template("dashboard.html",dataincoming = dataincoming, dataincoming_p=dataincoming_p)

@app.route("/dashboard/")
def dashboard():
    all_params = request.args.to_dict()
    return render_template("dashboard.html", data=all_params)


if __name__ == "__main__":
    app.run(debug=True,port=8000)


    """
    important topics
    session limitations =
    Cannot put large data

    asynchrounous
    stateless http
    cookies
    sessions
    """ 