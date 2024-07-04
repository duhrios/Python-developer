velocidade = int(input('Velocidade do Carro:'))
if (velocidade > 80):
  multa = (velocidade- 80) * 7
  print('----------Multa---------\n\n Você foi multado no valor de {}R$'.format(multa))
else:
  print('Parabêns você não levou nenhuma multa')