from urllib.error import HTTPError
from flask import Flask, render_template, url_for, jsonify, request, abort
import translate, sentiment

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-text', methods=['POST'])
def detect_text():
    data = request.get_json()
    text_input = data['text']
    response = translate.get_detectlanguage(text_input)
    return jsonify(response)

@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    translation_input = data['from']
    response = translate.get_translation(text_input, translation_output, translation_input)
    if isinstance(response,dict):
        abort(400, description = response["error"]["message"])
    return jsonify(response)

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    return jsonify(response)

@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(str(e)), 400
