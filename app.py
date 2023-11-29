from flask import Flask, render_template
from flask import request

app = Flask(__name__)



@app.route('/')
def main_page():
    return render_template('hello.html')

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    name = 'Guest'
    first_name = request.form['first_name']
    last_name = request.form['second_name']
    name = f'{first_name} {last_name}'
    return f"Hello, {name}!"

app.run(debug=True)