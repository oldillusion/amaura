from flask import Flask, redirect

app = Flask(__name__, static_folder='public', static_url_path='/')

@app.route("/")
def index_html():
    return redirect("/index.html")