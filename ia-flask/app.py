from flask import Flask, appcontext_popped, redirect, url_for, request, render_template
import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()


@app.route('/', methods=['POST'])
def index_post():
    #ler os valores do formulario
    texto = request.form['text']
    lingua = request.form['language']

    # carregar os valores de .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']
    
    pacote = '/translate?api-version=3.0'
    param_lang_alv = '&to=' + lingua
    construir_url = endpoint + pacote + param_lang_alv

    # informaçoes do setup do header
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # criar o body que ira receber o texto a ser traduzido
    body = [{'text': texto}]

    translator_request = requests.post(construir_url, headers=headers, json=body)

    translator_response = translator_request.json()
    translated_text = translator_response[0]['translations'][0]['text']

    # chamar o template renderizado, passando o texto traduzido, o texto original e a lingua para o template

    return render_template(
        'results.html',
        translated_text=translated_text,
        texto=texto,
        lingua=lingua
    )



app = Flask(__name__)
@app.route('/', methods=['GET']) # adicionar uma rota, indica que sera retornado o index.html
def index():
    return render_template('index.html')