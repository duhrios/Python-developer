ano = int(input('Digite o ano:'))

if ano % 4 == 0:
  if ano % 100 == 0:
    if ano % 400 == 0:
      print('ano é bixesto!')
    else:
      print('Não é bixesto!') 
  else:
    print('ano é bixesto!') 
else:
  print('Não é bixesto!')