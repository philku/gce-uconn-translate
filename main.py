from flask import Flask, request, render_template

# START Translate requirements
from google.cloud import translate_v2 as translate
translate_client = translate.Client()
# END Translate requirements


app = Flask(__name__)   # Flask is the web framework we're using

@app.route('/', methods=['POST','GET'])         # This defines when the function below will be called
def translate():
    if request.method == 'POST':

        # This code will run if a POST is received
        data = request.form.to_dict(flat=True)  # Reads the body of the post request and assigns it to the "data" variable
        result = translate_client.translate(data['inputText'], target_language=data["toLang"]) # Sends data to the translate API
        return render_template('index.html',translatedText=result['translatedText'])    # Renders the page with the response

    else:

        # This code will run if a GET is received
        return render_template('index.html')


# Don't worry about this part
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)