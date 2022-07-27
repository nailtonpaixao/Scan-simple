import requests

lista = open('Sec list','r')

site = " Link "

for item in lista.readlines():
        request = requests.get(site + item)
        tamanho_da_resposta = len(request.text)
        if(tamanho_da_resposta > 0):
                print("Arquivo encontrado: " + site + item)
