import string
import random
from time import sleep

fraca = '12345678'
media = string.digits + string.ascii_lowercase
forte = '!@#$%¨&*' + string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase

def tela():
  menu = {'1':'Gerar senha',
          '2': 'Sair'}
  print('| Gerador de Senhas |')
  for k,v in menu.items():
    print(f'[{k}] - {v}')
  print()

def opcoes():
  print()
  print("Opaa !! Vi que você selecionou a opção gerar senha..")
  print()
  sleep(0.5)
  print("Temos 3 opções de senhas.. são elas:\n\n1 - Senha fraca. \n2 - Senha média. \n3 - Senha forte")
  sleep(0.5)
  print()

def desligar_sistema():
  print()
  print("Finalizando sistema..")
  sleep(0.5)
  print()
  
def senha_fraca():
  print()
  senha = ''
  for i in range(6):
    senha += random.choice(fraca)
  print()
  print(f'*** Senha gerada com sucesso!! Sua nova senha é: {senha} ***')
  print()

def senha_media():
  print()
  senha = ''
  for i in range(6):
    senha += random.choice(media)
  print()
  print(f'*** Senha gerada com sucesso!! Sua nova senha é: {senha} ***')
  print()
def senha_forte():
  print()
  senha = ''
  for i in range(6):
    senha += random.choice(forte)
  print()
  print(f'*** Senha gerada com sucesso!! Sua nova senha é: {senha} ***')
  print()

  