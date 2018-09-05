from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    if name is None:
        name= 'tout le monde'
    return f""" 
        Salut <em>{name}</em>,
        vous êtes {random.randint(10, 30)} aujourd'hui 
    """


app.run(debug=True)