import os,os.path
from random import randrange
DIR = './images'
foto_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/craw/', methods=['GET'])
def respond():
    return jsonify({
    "url" : f"https://raw.githubusercontent.com/blacksmithop/fotos/master/images/{randrange(1,foto_count)}.jpg"
    })

@app.route('/')
def index():
     return render_template("index.html")
    
@app.route('/upload/', methods=['GET'])
def upload():
    return render_template("upload.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
