from flask import Flask,render_template
 
app = Flask("app")

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", name = "Payal")



@app.route('/login')
def  login():
    return render_template("login.html")

app.run(debug=True)

"""
Flask templates = HTML + Python logic

browser -> Flask route -> Template Engine -> HTML -> Browser

Flask never sends Python
Flask sends rendered HTML
Jinja runs before HTML reaches browser


{{ output data}}
{% Logic %}
{##}
"""

