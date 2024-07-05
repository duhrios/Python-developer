V=print ("          \033[4;34;40m Calculadora Inteligente!\033[m")
print ('\n[1] Para adção \n[2] Para Multiplicar \n[3] Para Divisão \n[4] Para subtração \n[5] Para maior \n[6] Sair')
escolha_usuario = 0
sair = 6
while escolha_usuario != sair:
  escolha_usuario = int(input('\nDigite sua Escolha:'))
  if escolha_usuario == 1:
    numero1 = int(input('Digite os dois numeros:'))
    numero2 = int(input(''))
    soma = numero1 + numero2
    print (' A soma de {} e {} é: {}'.format(numero1, numero2,soma))
  elif escolha_usuario == 2:
    numero1 = int(input('Digite os dois numeros:'))
    numero2 = int(input(''))
    soma = numero1 * numero2
    print (' A multiplicação de {} e {} é: {}'.format(numero1, numero2,soma))
  elif escolha_usuario == 3:
    numero1 = int(input('Digite os dois numeros:'))
    numero2 = int(input(''))
    soma = numero1 / numero2
    print (' A divisão de {} e {} é: {}'.format(numero1, numero2,soma))
  elif escolha_usuario == 4:
    numero1 = int(input('Digite os dois numeros:'))
    numero2 = int(input(''))
    soma = numero1 - numero2
    print (' A subtração de {} e {} é: {}'.format(numero1, numero2,soma))
  elif escolha_usuario == 5:
    numero1 = int(input('Digite os dois numeros:'))
    numero2 = int(input(''))
    maior = max(numero1, numero2)
    print (' O maior de {} e {} é: {}'.format(numero1, numero2,maior))
  elif escolha_usuario >= 7:
    print ('Opção invalida por favor digite uma opçao valida:')
  elif escolha_usuario == 6:
    sair = 6
    print ('Obrigado!!!')
  
    