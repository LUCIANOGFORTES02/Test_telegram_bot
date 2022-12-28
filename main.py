import requests #Biblioteca que permite fazer requisições 
import time
import json

class Bot:
    def _init_ (self):
        token='5810812199:AAFoebmRT8YjizOCA1DdKVScn4I7cRpoyoM'
        self.url_base = f'https://api.telegram.org/bot{token}'


#iniciar bot
    def iniciar(self):
        update_id= None
        while True:
            pass



#Obter mensagem 
    def obterMensagens (self,update_id):
        link_requisicao = f'{self.url_base}/getUpdates?timeout=100'

        if update_id:
            #Adiciona um parâmetro que vai permitir pegar apenas a última mesagem
            link_requisicao= f'{link_requisicao}&offset={update_id+1}'
        requests.get(link_requisicao)


#Criar uma resposta 
    def criarResposta (self):
        pass
#Responder
    def responder(self):
        pass
