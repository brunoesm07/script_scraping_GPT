# Script

Resolvi praticar um pouco de automação e dessa vez o objetivo era desenvolver um script que atendesse às seguintes especificações:

1. **Acesso à URL:** O script deve ser capaz de receber uma URL como entrada. 
2. **Web Scraping:** A partir da URL fornecida, o script deve acessar a página web e fazer o scraping do conteúdo.
3. **Salvar Conteúdo:** O conteúdo extraído deve ser salvo em um arquivo de texto (.txt).
4. **Integração com GPT-4:** Utilize o conteúdo salvo no arquivo .txt para criar um prompt que será enviado ao modelo GPT-4 da OpenAI.
5. **Análise Resumida:** O script deve exibir na tela uma análise resumida do conteúdo da página, gerada pelo GPT-4, de forma humanizada, bem formatada e com emojis.

Algoritmo:

a) receber a informaçao de interesse: URL;

b) fazer o scaping do conteúdo, analisar e salvar em um arquivo .txt;

  b.1) scraping de conteúdo;

  b.2) analisa o conteúdo html;

  b.2.2) aponta as tags de texto;

  b.3) extrai o texto e salva o resultado em um arquivo .txt.

c) ler o arquivo .txt e inseri-lo em um prompt;

c.1) lê o arquivo .txt;

c.2) prepara o prompt para o modelo GPT.

d) enviar para o GPT da OpenAI e mostrar na tela a análise.

d.1) chama o modelo GPT para gerar a análise;

d.2) exibe a análise gerada.


# Bibliotecas utilizadas:

Documentação Requests: https://requests.readthedocs.io/en/latest/
-> Requests é uma biblioteca HTTP elegante e simples para Python, desenvolvida para seres humanos.

Documentação Beautiful Soup: https://beautiful-soup-4.readthedocs.io/en/latest/
-> Beautiful Soup é uma biblioteca Python para extrair dados de arquivos HTML e XML.

Documentação OpenAI: https://platform.openai.com/docs/libraries/python-library
-> A API OpenAI pode ser aplicada a praticamente qualquer tarefa.
