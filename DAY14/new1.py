from flask import Flask,request,url_for
from markupsafe import escape

app = Flask(__name__)

# @app.route('/home')
# def home():
#     name = request.args.get("name","Flask")
#     return f"Hello, {escape(name)}"

@app.route('/user/<username>')
def show_user_profile(username):
     # show the user profile for that user
     return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
     return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
     return f"Subpath {escape(subpath)}"

@app.route('/')
def index():
     return f'''
     <a href = "{url_for('home')}">Home</a>
     '''
@app.route('/home')
def home():
     return "Welcome Home"
if __name__ == "__main__":
    app.run(debug=True, port=8000)