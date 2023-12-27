from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime('%d/%m/%Y %H:%M') 

# @app.route('/cache')
# def cache():
#     return index()

# @app.route('/nocache')
# def nocache():
#     return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)