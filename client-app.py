import requests
import random

duracao = True
endpoints = ["renda-variavel", "renda-fixa", "fii", "cripto"]

while duracao == True:
    requisicao = requests.get("http://app:5000/" + endpoints[random.randint(0,3)])
    print(requisicao.status_code)