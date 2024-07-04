import requests

# Substitua com suas credenciais
API_KEY = 'sua_chave_de_api'
TOKEN = 'seu_token'
BOARD_ID = 'id_do_quadro'  # Você pode obter o ID do quadro na URL do quadro no Trello

# URL da API do Trello para criar um novo cartão
url = f"https://trello.com/b/ZMNdA4wc/pessoal"

# Solicita informações ao usuário
nome_tarefa = input("Digite o nome da nova tarefa: ")
descricao_tarefa = input("Digite a descrição da nova tarefa: ")
id_lista = input("Digite o ID da lista onde deseja adicionar a tarefa: ")

# Dados do cartão a ser criado
data = {
    'name': nome_tarefa,
    'desc': descricao_tarefa,
    'idList': id_lista,
}

# Realiza uma requisição POST para criar um novo cartão
response = requests.post(url, data=data)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    print("Tarefa criada com sucesso!")
else:
    print(f"Falha ao criar tarefa: {response.status_code} - {response.text}")
