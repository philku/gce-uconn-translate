from flask import Flask, request, render_template
from google.cloud import translate_v2 as translate
translate_client = translate.Client()


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def translate():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        result = translate_client.translate(data['inputText'], target_language=data["toLang"])
        return render_template('index.html',translatedText=result['translatedText'])
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)