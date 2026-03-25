import os
import json
import requests
from dotenv import load_dotenv

# ─── CARREGAR CREDENCIAIS ───────────────────────────────
load_dotenv("power-up.env")
API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN   = os.getenv("TRELLO_TOKEN")
ID_LIST = os.getenv("TRELLO_ID_LIST")

# ─── ETIQUETAS POR TIPO ─────────────────────────────────
ETIQUETAS = {
    "1": ("Residencial", "green"),
    "2": ("Comercial",   "blue"),
    "3": ("Industrial",  "orange"),
    "4": ("Reforma",     "yellow"),
    "5": ("Outro",       "purple")
}

# ─── FUNÇÕES ────────────────────────────────────────────

def carregar_json():
    with open("projeto_info.json", "r", encoding="utf-8") as f:
        return json.load(f)

def escolher_tipo():
    print("\n🏷️  Tipo do projeto:")
    for num, (nome, cor) in ETIQUETAS.items():
        print(f"  {num}. {nome}")
    escolha = input("\nEscolha o número: ").strip()
    return ETIQUETAS.get(escolha, ("Outro", "purple"))

def get_board_id():
    url = f"https://api.trello.com/1/lists/{ID_LIST}"
    r = requests.get(url, params={"key": API_KEY, "token": TOKEN})
    if r.status_code == 200:
        return r.json().get("idBoard")
    print(f"❌ Erro ao buscar Board ID: {r.status_code}")
    return None

def criar_etiqueta(id_board, nome, cor):
    url = f"https://api.trello.com/1/boards/{id_board}/labels"
    r = requests.post(url, params={
        "key":   API_KEY,
        "token": TOKEN,
        "name":  nome,
        "color": cor
    })
    if r.status_code == 200:
        return r.json().get("id")
    print(f"❌ Erro ao criar etiqueta: {r.status_code}")
    return None

def criar_card(projeto, tipo_nome, id_etiqueta):
    url = "https://api.trello.com/1/cards"
    descricao = (
        f"📁 Caminho: {projeto['caminho']}\n"
        f"📅 Criado em: {projeto['data_criacao']}\n"
        f"🏷️ Tipo: {tipo_nome}"
    )
    params = {
        "key":      API_KEY,
        "token":    TOKEN,
        "idList":   ID_LIST,
        "name":     projeto["nome_projeto"],
        "desc":     descricao,
        "idLabels": id_etiqueta
    }
    r = requests.post(url, params=params)
    if r.status_code == 200:
        print(f"\n✅ Card criado com sucesso!")
        print(f"🔗 Link: {r.json()['shortUrl']}")
    else:
        print(f"\n❌ Erro ao criar card: {r.status_code} - {r.text}")

# ─── EXECUÇÃO ───────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("       IMPORTADOR TRELLO — PROJETOS")
    print("=" * 45)

    # 1. Carregar dados do JSON
    projeto = carregar_json()
    print(f"\n📂 Projeto: {projeto['nome_projeto']}")
    print(f"📅 Criado em: {projeto['data_criacao']}")
    print(f"📁 Caminho: {projeto['caminho']}")

    # 2. Escolher tipo/etiqueta
    tipo_nome, cor = escolher_tipo()

    # 3. Buscar board e criar etiqueta
    print(f"\n⏳ Conectando ao Trello...")
    id_board    = get_board_id()
    id_etiqueta = criar_etiqueta(id_board, tipo_nome, cor) if id_board else None

    # 4. Criar card
    criar_card(projeto, tipo_nome, id_etiqueta)
    print("=" * 45)
