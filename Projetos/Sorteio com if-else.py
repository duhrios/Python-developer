import random

numero = [1,2,3,4,5]
escolha_usuario =  int(input('Digite um numero de 0 a 5:'))
escolha_random = random.choice(numero)

if escolha_usuario >= 6:
  print('Que pena você escolheu um numero\nfora do intervalo de 1 a 5')
elif escolha_random == escolha_usuario:
  print('Parabens você acertou')
else:
  print('Que pena você errou\nO numero sorteado foi {}'.format(escolha_random))

  
