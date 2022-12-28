import requests #Biblioteca que permite fazer requisições 
import time
import json

class Bot:
    def __init__ (self):
        token='5810812199:AAFoebmRT8YjizOCA1DdKVScn4I7cRpoyoM'
        self.url_base = f'https://api.telegram.org/bot{token}/'


#iniciar bot
    def iniciar(self): 
        update_id= None
        while True:
            atualizacao = self.obterMensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                        update_id = mensagem ['update_id'] 
                        chat_id = mensagem ['message']['from']['id']#Para quem vai enviar a mensagem
                        resposta = self.criarResposta()
                        self.responder(resposta,chat_id)

            



#Obter mensagem 
    def obterMensagens (self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'

        if update_id:
            #Adiciona um parâmetro que vai permitir pegar apenas a última mesagem
            link_requisicao= f'{link_requisicao}&offset={update_id+1}'
        resultado =requests.get(link_requisicao)
        return json.loads(resultado.content)

#Criar uma resposta 
    def criarResposta (self):
        return 'oá'
#Responder
    def responder(self,resposta,chat_id):
        #enviar
        #link formatado com parametro sendMessage passando para qual chat sera enviado e a resposta enviada
        link_de_envio = f'{self.url_base}sendMensage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio) 


bot = Bot()
bot.iniciar()