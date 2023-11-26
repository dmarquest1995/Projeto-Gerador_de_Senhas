import defs
from time import sleep

while True:
  print()
  defs.tela()
  print()
  opcao = int(input("Digite a opção desejada: "))

  while opcao > 2 or opcao < 1: #Tratando erro com While
    print("Opção Inválida ! Utilize uma das opções disponíveis em tela.")
    print()
    opcao = int(input("Digite a opção desejada: "))
    

  if opcao == 2:
    defs.desligar_sistema()
    break

  while opcao == 1:
    defs.opcoes()
    break

  opcao_senha = int(input('Qual delas você deseja? Escolha um número: '))
    
  while opcao_senha == 1:
    defs.senha_fraca()
    break

  while opcao_senha == 2:
    defs.senha_media()
    break

  while opcao_senha == 3:
    defs.senha_forte()
    break
  
  resposta = int(input('Desejar retornar ao Menu ou Sair? Para "Menu" digite 1 e para "Sair" digite 2: '))
  if resposta == 1:
    print()
  elif resposta == 2:
    print()
    print('Fechando sistema..')
    sleep(0.5)
    break
  
  
    


