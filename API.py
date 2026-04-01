from flask import Flask, jsonify, send_file
import os
import json
import datetime

app = Flask(__name__)

@app.after_request
def add_ngrok_header(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

@app.route('/manifest.json')
def manifest():
    return send_file('manifest.json')

@app.route('/projeto', methods=['GET'])
def analisar_projeto():
    try:
        with open('projeto_info.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return jsonify(dados)
    except FileNotFoundError:
        return jsonify({"erro": "projeto_info.json não encontrado. Execute o leitor-de-conteudo.py primeiro."}), 404

@app.route('/projeto-pdi.html')
def projeto_pdi():
    return send_file('projeto-pdi.html')

@app.route('/popup.html')
def popup():
    return send_file('popup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)