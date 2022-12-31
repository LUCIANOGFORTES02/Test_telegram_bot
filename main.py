import requests 
import webbrowser as wb
import time
import json

menu="""Escolha uma das opções (Clique no item):
        /opcao1 Fazer um pedido no ifood
        /opcao2 Reclamar de um pedido
        /opcao3 Fazer uma avaliação
        """

class Bot:
    def __init__ (self):
        token='5810812199:AAFoebmRT8YjizOCA1DdKVScn4I7cRpoyoM'
        self.url_base = f'https://api.telegram.org/bot{token}/'
        
# Quando se coloca uma / e uma palavra se torna um link

#iniciar bot
    def iniciar(self): 
        update_id = None
        while True:
            atualizacao = self.obterMensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                        update_id = mensagem ['update_id'] 
                        chat_id = mensagem ['message']['from']['id']#Para quem vai enviar a mensagem
                        first_message = mensagem['message']['message_id']==1 #Para saber se é a primeira mensagem
                        resposta = self.criarResposta(mensagem,first_message)
                        print(resposta)
                        self.responder(resposta,chat_id)

#Obter mensagem 
    def obterMensagens (self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            #Adiciona um parâmetro que vai permitir pegar apenas a última mesagem
            link_requisicao = f'{link_requisicao}&offset={update_id+1}'
        resultado =requests.get(link_requisicao)
        print(json.loads(resultado.content))#Método que retorna um dicionário
        return json.loads(resultado.content)

#Criar uma resposta 
    def criarResposta (self,mensagem,first):
        mensagem=mensagem['message']['text']
        if first==True or mensagem.lower() == "menu":
            return menu
        elif mensagem == "/opcao1":
            wb.open("https://www.ifood.com.br/inicio")
            return f'Pedido realizado'
        elif mensagem == "/opcao2":
            wb.open("https://www.reclameaqui.com.br/")
            return f'Reclamação concluída'
        elif mensagem == "/opcao3":
            return f'Avaliação concluída'
        return f'Digite "menu"'
    
    

    
#Responder
    def responder(self,resposta,chat_id):
        #enviar
        #link formatado com parametro sendMessage passando para qual chat sera enviado e a resposta enviada
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio) 


bot = Bot()
bot.iniciar()