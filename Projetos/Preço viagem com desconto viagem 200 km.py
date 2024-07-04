viagem = int(input('Digite quantos km será a viagem:'))
if(viagem < 200):
  viagem_50 = viagem * 0.50
  print('Sua viagem custará {:.2f}'.format(viagem_50))
else:
  viagem_45 = viagem * 0.45
  print('Sua viagem custará {:.2f}'.format(viagem_45))
