from flask import Flask, render_template, request, jsonify, redirect
import os


app = Flask(__name__)

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/txt')
def blog_redirect():
    return redirect("https://esteininger.medium.com/")


if __name__ == '__main__':
    app.run(debug=True, port=5012)
