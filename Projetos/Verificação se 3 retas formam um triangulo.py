reta_1 = float (input('Digite 3 retas:'))
reta_2 = float (input())
reta_3 = float (input())

if reta_1 > reta_2 and reta_1 > reta_3:
  soma_retas_menores = reta_2 + reta_3
  if soma_retas_menores > reta_1:
    print('É possível fazer um triangulo')
  else:
    print ('Não é Possível')
elif reta_2 > reta_1 and reta_2 > reta_3:
  soma_retas_menores = reta_1 + reta_3
  if soma_retas_menores > reta_2:
    print('É possível fazer um triangulo')
  else:
    print ('Não é Possível')
elif reta_3 > reta_2 and reta_3 > reta_1:
  soma_retas_menores = reta_1 + reta_2
  if soma_retas_menores > reta_3:
    print('É possível fazer um triangulo')
  else:
    print ('Não é Possível')
else:
  print ('Não é possivel fazer o trinagulo.')   