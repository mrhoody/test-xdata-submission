from typing import Tuple
from flask import Flask, request, response


app = Flask(__name__)

@app.route('/asr', methods=['POST'])
def hello() -> Tuple(str, str):
    if request.accept_mimetypes['multipart/form-data']:
        transcript = True
        duration = True
        return transcript, duration

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(debug=True)

