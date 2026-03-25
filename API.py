from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Pasta fixa inicial para teste
PASTA_PROJETO = r"C:\Users\luis.rafael\Pasta-prejeto-trabalho"

@app.route('/projeto', methods=['GET'])
def analisar_projeto():

    nome_projeto = os.path.basename(PASTA_PROJETO)

    timestamp = os.path.getctime(PASTA_PROJETO)
    data_criacao = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    dados = {
        "nome_projeto": nome_projeto,
        "caminho": PASTA_PROJETO,
        "data_criacao": data_criacao
    }

    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)