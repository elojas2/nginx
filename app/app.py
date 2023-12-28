from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime('%d/%m/%Y %H:%M') 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)