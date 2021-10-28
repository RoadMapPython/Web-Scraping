# Web-Scrapping
## Componentes usados na live,e um readme para mais detalhes e o link da live gravada: YouTube:
###### -Obs: tem um dicionário de palavras no final do documento

=======================|📚Introdução📚|=====================<br />
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

==========================|⚙️Construção do codigo⚙️|============================<br />
Vou começar com o webbrowser

import webbrowser

webbrowser.open('https://www.vagas.com.br/vagas-de-programador-python')

Aqui abrimos a pagina web que desejamos via código python, util ne? 

======================================================================<br />
Agora iremos realizar a instalação de uma outra biblioteca que iremos usar durante a criação do código
* Vamos la no windows+R 
* Digita cmd 
* E digite o comando:pip install requests

======================================================================<br />
Vamos importar a biblioteca "requests" e usar o metodo get

import requests

texto_html = requests.get('https://www.vagas.com.br/vagas-de-programador-python')
print('Status do codigo:', texto_html.status_code)

Os códigos de status das respostas HTTP indicam se uma requisição HTTP foi corretamente concluída.
As respostas são agrupadas em cinco classes:

* Respostas de informação (100-199),
* Respostas de sucesso (200-299),
* Redirecionamentos (300-399)
* Erros do cliente (400-499)
* Erros do servidor (500-599).

======================================================================<br />
Iremos utilizar o BeaultifulSoup da biblioteca lxml, com isso teremos de instalar 
o pacote.
* Windows+R 
* Digita cmd 
* E digite o comando:pip install lxml

=====================|⚙️Construção do Primeiro código⚙️|======================<br />
from bs4 import BeautifulSoup
import requests 

texto_html=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text

* Primeiramente passamos o texto do site para formato lxml para o pythom compreender melhor.<br />
site=BeautifulSoup(texto_html,"lxml")

* Procuramos algum <li> com a classe "vaga odd".<br />
emprego=site.find('li',class_="vaga odd")

Como achei vaga odd no inspecionar? <br />
Siga as setinhas abaixo :)<br />
<div class="pesquisaConteudoWrapper"> <br />
  <section id="pesquisaResultado"> <br />
    <section class="grupoDeVagas">  <br />
      <div id="todasVagas"> <br />
         <li class="vaga odd"> <br />
  
* Procuramos o nome da empresa sem as tags html e as habilidades necessárias<br />
nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
habilidades=emprego.find('div',class_="detalhes").text.replace("","")

\n

datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
print("Nome da empresa{}" .format(nomedaempresa))
print("Habilidades Necessarias{}".format(habilidades))
print(datadepubli)
  
Aqui iremos procurar a data de publicação , e imprimir as variaveis nomedaempresa e habilidades.
  
=====================|⚙️Segundo código⚙️|======================<br />
from bs4 import BeautifulSoup<br />
import requests 

texto_html=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text<br />
site=BeautifulSoup(html_text,"lxml")<br />
  
* Aqui buscamos tudo da tag <li> que tenha classe "vaga odd"<br />
empregos=site.find_all('li',class_="vaga odd")
  
for emprego in empregos:<br />
  
* Nome da empresa sem as tags html<br />
  nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
  
* Habilidades Necessarias<br />
  habilidades=emprego.find('div',class_="detalhes").text.replace("","")
  
* data de publicacao<br />
  datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")<br />
  print("Nome da empresa{}" .format(nomedaempresa)<br />
       +"Habilidades Necessarias{}".format(habilidades)<br />
       +"Data da Publicacao{}".format(datadepubli))

  print(" ")     
  
=====================|⚙️Terceiro código explicado⚙️|======================<br />
from bs4 import BeautifulSoup<br />
import requests 


  * Bucar no endereco html<br />
html_text=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text<br />

  * Transformar o html em lxml para facilitar a leitura do python<br />
site=BeautifulSoup(html_text,"lxml")<br />

  * Buscar tudo  pagina WEB , a tag li na class vaga odd<br />
empregos=site.find_all('li',class_="vaga odd")

with open ("empregos.txt","w",'encoding='utf-8') as arquivo:<br />
  for emprego in empregos:<br />
  
  * Nome da empresa sem as tags html<br />
    nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")<br />
  
  * Habilidades Necessarias<br />
    habilidades=emprego.find('div',class_="detalhes").text.replace("","")<br />
  
  * data de publicacao<br />
    datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")<br />
    informacoes={<br />
      "Nome da empresa":nomedaempresa+"",<br />
      "Habilidades Necessarias":habilidades+"",<br />
      "Data da publicacao":datadepubli+"",<br />
    }<br />
    arquivo.write (str(informacoes)+"\r\n" +"\r\n")
======================================================================<br />
---Dicionário---<br />
requests<br />
response<br />
get<br />
content<br />
headers<br />
