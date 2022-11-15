#Cria um aplicativo para previsão do tempo usando a API do OpenWeatherMap

import requests
import json
import os
import time
from datetime import datetime

#aplicativo de previsão do tempo
def previsao_tempo():
    #limpa a tela
    os.system('clear')
    #pega a localização
    localizacao = input("Digite o nome da cidade: ")
    #pega a chave da API
    chave = "sua chave aqui da API"
    #cria a url
    url = "http://api.openweathermap.org/data/2.5/weather?q="+localizacao+"&appid="+chave
    #pega os dados
    dados = requests.get(url)
    #converte os dados para json
    dados = dados.json()
    #pega a temperatura
    temperatura = dados['main']['temp']
    #converte a temperatura de kelvin para celsius
    temperatura = temperatura - 273.15
    #pega a descrição do tempo
    descricao = dados['weather'][0]['description']
    #pega a velocidade do vento
    vento = dados['wind']['speed']
    #pega a umidade
    umidade = dados['main']['humidity']
    #pega a pressão
    pressao = dados['main']['pressure']
    #pega a data e hora
    data = datetime.now()
    #imprime os dados
    print("Data e hora: ", data)
    print("Temperatura: ", temperatura)
    print("Descrição: ", descricao)
    print("Vento: ", vento)
    print("Umidade: ", umidade)
    print("Pressão: ", pressao)
    #espera 5 segundos
    time.sleep(5)
    #limpa a tela
    os.system('clear')

def menu():
    #limpa a tela
    os.system('clear')
    #imprime o menu
    print("1 - Previsão do tempo")
    print("0 - Sair")
    #pega a opção
    opcao = int(input("Digite a opção: "))
    #limpa a tela
    os.system('clear')
    #retorna a opção
    return opcao
while True:
    #pega a opção
    opcao = menu()
    #verifica a opção
    if opcao == 1:
        #chama a função de previsão do tempo
        previsao_tempo()
    elif opcao == 0:
        #sai do programa
        break
    else:
        #opção inválida
        print("Opção inválida")
        #espera 2 segundos
        time.sleep(2)
        #limpa a tela
        os.system('clear')
