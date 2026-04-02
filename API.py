from flask import Flask, jsonify, send_file
import os
import json
import datetime
import threading
from tkinter import Tk, filedialog

app = Flask(__name__)

@app.after_request
def add_ngrok_header(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

@app.route('/manifest.json')
def manifest():
    return send_file('manifest.json')

@app.route('/selecionar-pasta' , methods = ["GET"])
def selecionar_pasta():
    resultado = {}
    
    def abrir_janela():
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        pasta = filedialog.askdirectory(title="Selecione a pasta do projeto")
        root.destroy()
        
        if pasta:
            nome_projeto = os.path.basename(pasta)
            timestamp = os.path.getmtime(pasta)
            data_criacao = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            dados = {
                'nome_projeto' : nome_projeto,
                'caminho_projeto' : pasta,
                'data_criacao' : data_criacao
            }
            
            with open('projeto_info.json', 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
                
                resultado['dados'] = dados
        else:
            resultado['erro'] = "Nenhuma pasta selecionada."
            
            t = threading.Thread(target=abrir_janela)
            t.start()
            t.join()
            
            if 'dados' in resultado:
                return jsonify(resultado['dados'])
            else:
                return jsonify({"erro": resultado['erro']}), 400

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

@app.route('/icon.svg')
def icon():
    return send_file('icon.svg', mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)