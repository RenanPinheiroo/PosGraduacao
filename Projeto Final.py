from flask import Flask
from Base import usuario

app = Flask(__name__)

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    return usuario


app.run()