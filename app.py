import os,os.path
from random import randrange
DIR = './images'
foto_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/craw/', methods=['GET'])
def respond():
    return jsonify({
    "url" : f"https://github.com/blacksmithop/fotos/blob/master/images/{randrange(foto_count)}.jpg"
    })
# A welcome message to test our server
@app.route('/')
def index():
    return jsonify({
    "data": "Welcome to fotos!"
    })

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
