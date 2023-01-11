from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/', methods=['GET']) # adicionar uma rota, indica que sera retornado o index.html
def index():
    return render_template('index.html')