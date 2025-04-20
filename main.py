#[new] flask app for password generator
from flask import Flask, render_template, request, jsonify #flask core functions
import random #use to randomly pick character
import string #use character set such as letter,digit,punctuation

app = Flask(__name__) #create flask app instance

@app.route('/') #define route for homepage

def index():
    return render_template('index.html') #render homepage

#define route to handle password generation
@app.route('/generate',methods=['POST'])

def generate():

    #get json data from frontend
    data = request.json

    #extract setting from the request

    length=int(data.get('length',12)) #default length = 12
    use_uppercase=data.get('uppercase') #checkbox value: include uppercase
    use_numbers=data.get('numbers') #checkbox value: include number
    use_symbols=data.get('symbols') #checkbox value: include symbol

    #start with lowercase letter
    characters=string.ascii_lowercase

    #conditionally add other character sets
    if use_uppercase:
        characters+=string.ascii_uppercase
    if use_numbers:
        characters+=string.digits
    if use_symbols:
        characters+=string.punctuation

    #if no character set seletected, return error
    if not characters:
        return jsonify({'error': 'No character sets selected.'}), 400
    
    #generate the password by randomly selecting characters
    password=''.join(random.choice(characters) for _ in range(length))

    #return then generated password as json
    return jsonify({'password' : password})

#run the app in debug mode if run directly
if __name__ == "__main__":
    app.run(debug=True)