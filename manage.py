import json
from flask import Flask, render_template, request, jsonify, redirect
import os
from helpers import Medium


app = Flask(__name__)

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home_page():
    medium = Medium(username="esteininger")
    posts = medium.get()
    return render_template('index.html', posts=posts)


@app.route('/txt')
def blog_redirect():
    return redirect("https://esteininger.medium.com/")


@app.route('/meet')
def calendar_redirect():
    return redirect("https://calendly.com/nux")

# files


@app.route('/map')
def vanlife_map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True, port=5012)
