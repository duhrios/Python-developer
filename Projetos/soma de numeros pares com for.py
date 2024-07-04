soma = 0
for contador in range(1,7,1):
  numeros = int(input('Digite o valor {}:'.format(contador)))
  if numeros % 2 == 1:
    soma += numeros
print('Soma dos numeros impares é:{}'.format(soma))
    