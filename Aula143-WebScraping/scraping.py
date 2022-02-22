import requests
from bs4 import BeautifulSoup

url = 'http://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):  # <- o "." vai pegar onde tem "question" obtida inspecionando o site!
    titulo = pergunta.select_one('.question-hyperlink')  # <- select_one vai pegar UM elemento apenas.
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post ')
    print(data.text, titulo.text, votos.text, '\t')
