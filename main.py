import requests
from bs4 import BeautifulSoup
import os
from openai import OpenAI

# Receber URL (o usuario indicará a URL desejada)
url = input("Informe a url: ")

# Faz o scraping do conteúdo da página
response = requests.get(url)
content = response.text

# Analisa o conteúdo html
soup = BeautifulSoup(content, 'html.parser')

# Encontra todas as tags de texto
text_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span'])

# Extrai o texto de cada tag e salva no arquivo .txt
with open("pagina.txt", "w", encoding="utf-8") as file:
    for tag in text_tags:
        file.write(tag.get_text() + "\n")

# Lê o conteúdo do arquivo
with open("pagina.txt", "r", encoding="utf-8") as file:
    page_content = file.read()

# Prepara o prompt para o modelo GPT
prompt = f"Você é um especialista em análise de conteúdo. Aqui está o conteúdo da página:\n\n{page_content}\n\nAgora, por favor, faça uma análise resumida e humanizada do conteúdo em português, bem formatada e com emojis nas palavras mais relevantes."

# Define a chave de API da OpenAI
OpenAI.api_key = 'Sua GPT_KEY',

# Chama o modelo GPT para gerar a análise
response = OpenAI.Completion.create(
    engine="gpt-3.5-turbo",  # Substitua pelo motor desejado
    prompt=prompt,
    max_tokens=500,  # Ajuste conforme necessário
    n=1,
    stop=None,
    temperature=0.7,  # Ajuste conforme necessário
)

# Exibe a análise gerada
print(response.choices[0].text)