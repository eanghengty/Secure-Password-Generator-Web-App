#[new] flask app for password generator
from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/generate',methods=['POST'])

def generate():
    data = request.json
    length=int(data.get('length',12))
    use_uppercase=data.get('uppercase')
    use_numbers=data.get('numbers')
    use_symbols=data.get('symbols')
    characters=string.ascii_lowercase
    if use_uppercase:
        characters+=string.ascii_uppercase
    if use_numbers:
        characters+=string.digits
    if use_symbols:
        characters+=string.punctuation

    if not characters:
        return jsonify({'error': 'No character sets selected.'}), 400
    
    password=''.join(random.choice(characters) for _ in range(length))
    return jsonify({'password' : password})

if __name__ == "__main__":
    app.run(debug=True)