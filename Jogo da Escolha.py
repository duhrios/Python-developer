import random

numero = [1,2,3,4,5,6,7,8,9,10]
tentativas = 1
escolha_usuario =  int(input('Digite um numero de 0 a 10:'))
escolha_random = random.choice(numero)

while escolha_usuario != escolha_random:
  print ('Você Errou!!! \n Tente novamente!')
  tentativas += 1
  escolha_usuario =  int(input('Digite um numero de 0 a 10:'))
  

print ('\n--------Parabens Você acertou!!!------- \n \nSeu numeoro de tentativas foi {} vezes '.format(tentativas))