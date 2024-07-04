Reta_1 = float (input('Digite 3 retas:'))
Reta_2 = float (input())
Reta_3 = float (input())

if Reta_1 == Reta_2 and Reta_2 == Reta_3:
 print ("Triângulo equilátero: 3 retas iguais")
elif Reta_1 == Reta_2 and Reta_3 != Reta_1:
 print('Triângulo isósceles: 2 retas iguais, 1 reta diferente.')
elif Reta_1 == Reta_3 and Reta_2 != Reta_1:
  print('Triângulo isósceles: 2 retas iguais, 1 reta diferente')
elif Reta_3 == Reta_2 and Reta_3 != Reta_1:
  print ('Triângulo isósceles: 2 retas iguais, 1 reta diferente')
else:
  print('Triângulo escaleno: 3 retas diferentes')