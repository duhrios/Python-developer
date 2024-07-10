import random

placar = 0
while True:
  escolha_usuario = int (input('Escolha o numero:'))
  escolha_pc = random.randint(1,10)
  escolha_impar_par = str ((input ('Escolha impar ou par (I/P):')))
  soma = escolha_usuario + escolha_pc
  print(f'Você escolheu {escolha_usuario} e o Pc {escolha_pc} a soma é {soma}')
  if escolha_impar_par == 'i'and  soma % 2==1 or escolha_impar_par == "p" and soma %2 ==0:
    
    print('Você ganhou')
    placar +=1
 
  else:
    print ('Você perdeu!')
    break
    
    
if placar > 0:
  print(f'Você ganhou {placar} vezes')
else:
  print('Você não ganhou nenhuma vez \nMais sorte da vez')



