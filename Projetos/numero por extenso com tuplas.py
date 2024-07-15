numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 
  resposta = int (input("Digite um nuemro de 0 a 20:"))
  if 0 <=  resposta <= 20:
    break   
print(numeros[resposta])