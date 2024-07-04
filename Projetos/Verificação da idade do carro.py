
tempo= int(input('Digite a idade do seu carro:'))
if tempo <=5:
  print('carro novo')
elif tempo > 5 and tempo <15:
  km = int(input('Qual a km do carro:'))
  if km <= 10000:
      print('Seminovo')
else:
  print('Carro Velho')
print("--------FIM-------")
  