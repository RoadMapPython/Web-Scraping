# Web-Scrapping
## Componentes usados na live,e um readme para mais detalhes e o link da live gravada: YouTube:
###### -Obs: tem um dicionário de palavras no final do documento

============================|Introdução|=====================================<br />
Web-Scrapping é o termo para usar um programa para baixar e processar conteúdo da web.
Por exemplo, o Google executa muitos programas de Web-Scrapping para indexar 
páginas da Web para seu mecanismo de busca.

Alguns conceitos 
* webbrowser: Vem com python e abre um navegador para uma página específica.

* requests: Baixa arquivos e páginas da Web da internet.

* bs4: Parses HTML, o formato em que as páginas da Web estão escritas.

* selenium: Lança e controla um navegador da Web. O módulo de selênio é capaz de preencher formulários e simular cliques do mouse neste navegador.

Quero tentar introduzir dois conceitos e aborda-los nessa live que vai ser o "webbrowser" e o "requests"

Web-Scrapping é basicamente é eu extrair dados de paginas web, conseguindo acessar exatamente o que desejo 
,so que no meu codigo em python ,facil ne?

==========================|Construção do codigo|============================<br />
Vou começar com o webbrowser

import webbrowser
webbrowser.open('https://sistemas.riopomba.ifsudestemg.edu.br/dacc/index.php/roadmap-python-ensino')

Aqui abrimos a pagina web que desejamos via código python, util ne? 

======================================================================<br />

Agora iremos realizar a instalação de uma biblioteca que iremos usar durante a criação do código
* Vamos la no windows+R 
* Digita cmd 
* E digite o comando pip install requests

======================================================================<br />
Vamos importar a biblioteca "requests" e usar o metodo get

import requests

response = requests.get('https://www.pudim.com.br/')

Os códigos de status das respostas HTTP indicam se uma requisição HTTP foi corretamente concluída.
As respostas são agrupadas em cinco classes:

* Respostas de informação (100-199),
* Respostas de sucesso (200-299),
* Redirecionamentos (300-399)
* Erros do cliente (400-499)
* Erros do servidor (500-599).
======================================================================<br />

import requests

response = requests.get('https://www.pudim.com/')
print('Status do codigo:', response.status_code)

print('Cabeçalho')
print(response.headers)

print('\n↓↓ Content ↓↓')
print(response.content)
======================================================================<br />
======================================================================<br />
---Dicionário---<br />
requests<br />
response<br />
get<br />
content<br />
headers<br />
