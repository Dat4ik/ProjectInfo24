from flask import Flask, render_template
from flask import request

app = Flask(__name__)

letter = 'A'

@app.route('/')
def main_page():
    return render_template('hello.html')

@app.route('/game', methods = ['GET', 'POST'])
def city_game():
    global letter
    city = request.form['first_name']
    fl = city[0]
    if fl == letter:
        if (city[-1] == 'ь'):
            letter = city[-2]
            return render_template('hello.html', text = f'Write city on letter {letter}')
        else:
            letter = city[-1]
            return render_template('hello.html', text = f'Write city on letter {letter}')
    else:
        return render_template('hello.html', text = f'Incorect, write city on letter {letter}')

app.run(debug=True)