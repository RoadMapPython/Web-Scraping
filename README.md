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
import requests

texto_html = requests.get('https://www.vagas.com.br/vagas-de-programador-python?')

print('Cabeçalho')
print(texto_html.headers)

O cabeçalho mostra as informações do site , vários atributos utilizados.

======================================================================<br />
import requests

texto_html = requests.get('https://www.vagas.com.br/vagas-de-programador-python')

print('Cabeçalho\n')
print(texto_html.headers)

print('\nConteudo\n')
print(texto_html.content)

O conteudo ele mostra todo o conteudo do site em si , todo o código html dele ,
sabe quando você clica em inspecionar? então é isso!

======================================================================<br />
Iremos utilizar o BeaultifulSoup da biblioteca bs4, com isso teremos de instalar 
o pacote.
* Windows+R 
* Digita cmd 
* E digite o comando:pip install bs4

======================================================================<br />
import requests
from bs4 import BeautifulSoup

texto_html = requests.get('https://www.vagas.com.br/vagas-de-programador-python')

conteudo = texto_html.content

site = BeautifulSoup(conteudo, 'html.parser')

print(type(site))

Estamos salvando o conteudo na váriavel "conteudo" 
Na váriavel "site" que criamos , passamos a variavel "conteudo" para o BeautifulSoup , 
em formato html.
O print foi somente para visualizar qual o tipo do site , não para imprimir a variavel site,
pois se imprimisse iria aparecer muita coisa

Podemos também imprimir com 
print(site.prettify())
que mostra o código todo html de uma forma mais organizada no padrão html

======================================================================<br />
import requests
from bs4 import BeautifulSoup

texto_html = requests.get('https://www.vagas.com.br/vagas-de-programador-python')

conteudo = texto_html.content

site = BeautifulSoup(conteudo, 'html.parser')
corpo= site.find('div',attrs={'class':'pesquisaConteudoWrapper' })
print(corpo.prettify())

aqui iremos colocar dentro da variavel "corpo" uma parte do site que desejamos ver,
utilizamos o find para achar o div com a classe documentFirstHeading.
attrs significa atributos,
Ele procura o primeiro div com a classe desejada e talvez mais a frente iremos comentar sobre.

======================================================================<br />
=====================|Primeiro código explicado|======================<br />
from bs4 import BeautifulSoup
import requests 

* Endereco da WEB a ser analisado

texto_html=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text

* Vamos ler o arquivo html transformar em lxml, para facilitar a leitura com python

soup=BeautifulSoup(texto_html,"lxml")

* Buscador de vagas
emprego=soup.find('li',class_="vaga odd")

* Nome da empresa sem as tags html

nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")

* Habilidades Necessarias
habilidades=emprego.find('div',class_="detalhes").text.replace("","")

* data de publicacao
/m

datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
print("Nome da empresa{}" .format(nomedaempresa))
print("Habilidades Necessarias{}".format(habilidades))
print(datadepubli)

=====================|Segundo código explicado|======================<br />
from bs4 import BeautifulSoup
import requests 


html_text=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text
soup=BeautifulSoup(html_text,"lxml")
* Buscar tudo  pagina WEB , a tag li na class vaga odd
empregos=soup.find_all('li',class_="vaga odd")
for emprego in empregos:
* Nome da empresa sem as tags html
  nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
* Habilidades Necessarias
  habilidades=emprego.find('div',class_="detalhes").text.replace("","")
* data de publicacao
  datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
  print("Nome da empresa{}" .format(nomedaempresa)
       +"Habilidades Necessarias{}".format(habilidades)
       +"Data da Publicacao{}".format(datadepubli))

  print(" ")     
  
=====================|Terceiro código explicado|======================<br />
from bs4 import BeautifulSoup
import requests 

* Bucar no endereco html
html_text=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text
* Transformar o html em lxml para facilitar a leitura do python
soup=BeautifulSoup(html_text,"lxml")
* Buscar tudo  pagina WEB , a tag li na class vaga odd
empregos=soup.find_all('li',class_="vaga odd")

with open ("empregos.txt","w") as arquivo:
  for emprego in empregos:
  * Nome da empresa sem as tags html
    nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
  * Habilidades Necessarias
    habilidades=emprego.find('div',class_="detalhes").text.replace("","")
  * data de publicacao
    datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
    informacoes={
      "Nome da empresa":nomedaempresa+"",
      "Habilidades Necessarias":habilidades+"",
      "Data da publicacao":datadepubli+"",
    }
    arquivo.write (str(informacoes)+"\r\n" +"\r\n")
======================================================================<br />
---Dicionário---<br />
requests<br />
response<br />
get<br />
content<br />
headers<br />
