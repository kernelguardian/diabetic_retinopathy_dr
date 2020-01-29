from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return 'error_page'

@app.route('/ml',methods=['POST'])
def ml():
    return 'ml'

