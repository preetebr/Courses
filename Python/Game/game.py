#Install: pip install requests
#Install: pip install beautifulsoup4



import requests
from bs4 import BeautifulSoup

# URL da página que você quer extrair informações
url = "https://www.google.com/"

try:
    # Fazendo a solicitação HTTP com um cabeçalho de agente de usuário
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, timeout=10)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parseando o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraindo o conteúdo
        content = soup.prettify()

        # Exibindo o conteúdo
        print(content)
    else:
        print(f"Falha ao acessar a URL. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro ao acessar a URL: {e}")
