import sys
sys.path.insert(1, './src/utils')

import localstorage
import console
from scrapping_faltas import scrappFaltas
from scrapping_notas import scrappNotas

console.clear()

while True:
  credenciais = localstorage.getItems()

  if(credenciais):
    matricula = credenciais['matricula']
    senha = credenciais['senha']
  else:
    matricula = input('Digite a matrícula: ')
    senha = input('Digite a senha: ')
    localstorage.setItem("matricula", matricula)
    localstorage.setItem("senha", senha)
    continue

  escolha = input(f'1 - Faltas / 2 - Notas / 3 - Sair {"/ 4 - Mudar usuário" if credenciais else ""} >> ')

  match (escolha):
    case "1":
      scrappFaltas(matricula, senha)
    case "2":
      scrappNotas(matricula, senha)
    case "3":
      print('Obrigado por utilizar o sistema. Seu usuário ficará salvo caso você estiver logado!')
      break
    case "4":
      confirma = input("Está ação fará com que você tenha que inserir suas credenciais novamente, deseja prosseguir? [y/n] >> ")
      match (confirma):
        case 'y':
          localstorage.deleteItems()
        case 'n':
          continue
        case _:
          print('Opção inválida.')
    case _:
      print('Opção inválida.')