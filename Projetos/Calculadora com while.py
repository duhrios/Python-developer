contador = 1
total = 0
tabuada = int(input('Digite o numero da tabuada: '))

while contador <10:
total = tabuada * contador
print('a tabuada é {}X{}={}'.format(tabuada, contador, total))
contador +=1
