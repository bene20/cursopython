print('Exercício 1')
resp = input('Digite um número: ')
if not resp.isdigit():
  print(f'{resp} não é um número!')
elif (int(resp) % 2 == 0):
  print(f'{resp} é um número par!')
else:
  print(f'{resp} é um número ímpar!')

print("Exercício 2")  
resp = input("Que horas são?")
if not resp.isdigit():
  print(f'{resp} não é um número')
elif (int(resp)>18) or (int(resp)<4):
  print('Boa noite!')
elif (int(resp)>=4) and (int(resp)<12):
  print('Bom dia!')
elif (int(resp)>=12) and (int(resp)<18):
  print('Boa tarde!')
else:
  print(f'{resp} não é uma hora válida')

print("Exercício 3")
nome = input("Digite seu nome: ")
if len(nome) <= 1:
  print("Por favor, digite um nome com pelo menos 2 caracteres!")
elif len(nome) <= 4:
  print("Seu nome é curto!")
elif len(nome) <=6:
  print("Seu nome é normal!")
else:
  print("Seu nome é grande!")