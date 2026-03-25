import os
import json
from datetime import datetime
from tkinter import Tk, filedialog

# Oculta janela principal
root = Tk()
root.withdraw()

# Selecionar pasta do projeto
pasta = filedialog.askdirectory(title="Selecione a pasta do projeto")
root.destroy()

if pasta:
    # Informações do projeto
    nome_projeto = os.path.basename(pasta)
    timestamp = os.path.getctime(pasta)
    data_criacao = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    projeto_info = {
        "nome_projeto": nome_projeto,
        "caminho": pasta,
        "data_criacao": data_criacao
    }

    # Mostrar no terminal
    print("\nInformações do Projeto:")
    for chave, valor in projeto_info.items():
        print(f"  {chave}: {valor}")

    # Exportar para JSON
    with open("projeto_info.json", "w", encoding="utf-8") as f:
        json.dump(projeto_info, f, indent=4, ensure_ascii=False)

    print("\n✅ projeto_info.json salvo com sucesso!")

else:
    print("Nenhuma pasta selecionada.")