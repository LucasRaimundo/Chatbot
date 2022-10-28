import os

def processarResposta(resposta, nome):
  if resposta=='1':
    print(f'{os.linesep}{nome} resposta{os.linesep}')

  elif resposta=='2':
    print(f'{os.linesep}{nome} resposta{os.linesep}')

  elif resposta=='3':
    print(f'{os.linesep}{nome} resposta{os.linesep}')

  elif resposta=='4':
    print(f'{os.linesep}{nome} resposta{os.linesep}')

  else:
    print('Resposta Inválida')
  

def start():
  print('Olá, bem vindo ')
  nome = input('Digite seu nome: ')
  email = input('Digite seu email: ')
  while True:
    resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - Pergunta 1{os.linesep}[2] - Pergunta 2{os.linesep}[3] - Pergunta 3{os.linesep}[4] - Pergunta 4{os.linesep}')
    processarResposta(resposta, nome)



if _name_ == '_main_':
  start()