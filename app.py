import os,os.path
from random import randrange
DIR = './images'
foto_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/craw/', methods=['GET'])
def respond():
    return jsonify({
    "url" : f"https://raw.githubusercontent.com/blacksmithop/fotos/master/images/{randrange(1,foto_count)}.jpg"
    })

@app.route('/')
def index():
     return render_template("index.html")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
