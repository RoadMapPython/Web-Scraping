from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text

site=BeautifulSoup(html_text,"lxml")

empregos=site.find_all('li',class_="vaga odd")

with open ("empregos.txt","w") as arquivo:
	for emprego in empregos:

		nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")


		habilidades=emprego.find('div',class_="detalhes").text.replace("","")


		datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
		informacoes={
		"Nome da empresa":nomedaempresa+"",
		"Habilidades Necessarias":habilidades+"",
		"Data da publicacao":datadepubli+"",
		}
arquivo.write (str(informacoes)+"\r\n" +"\r\n")