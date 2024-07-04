tabuada = int(input('\033[0;34mDigite o valor da tabuada:'))

for contador in range(1,11):
  total = tabuada * contador
  print('\033[1;33m{} X {} = {}'.format(tabuada,contador,total))