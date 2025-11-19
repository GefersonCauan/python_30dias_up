# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# dados = {
#     "title": "Curso",
#     "body": "Aprendendo API",
#     "userId": 1
# }

# resposta = requests.post(url, json=dados)
# print(resposta.status_code)
# print(resposta.json())

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo à minha API"})

@app.route('/soma', methods=['POST'])
def somar():
    dados = request.get_json()
    resultado = dados['a'] + dados['b']
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
