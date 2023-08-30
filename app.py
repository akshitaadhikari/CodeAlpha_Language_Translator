from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text_to_translate = data['text']
        target_language = data['language']

        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=target_language).text

        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
