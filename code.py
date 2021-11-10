import requests
from bs4 import BeautifulSoup

texto_html=requests.get('https://www.vagas.com.br/vagas-de-programador-python').text

site=BeautifulSoup(texto_html,"lxml")

emprego=site.find('li',class_="vaga odd")
nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
habilidades=emprego.find('div', class_='detalhes').text.replace("","")
datadepubli=emprego.find('span', class_="data-publicacao").text.replace("","")
print("Nome da empresa{}".format(nomedaempresa)
     +"Habilidades Necessarias{}".format(habilidades)
     +"Data de publicação{}".format(datadepubli)
        )
