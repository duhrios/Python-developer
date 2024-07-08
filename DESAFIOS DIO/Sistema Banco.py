menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao_usuario = int(input(menu))
  if opcao_usuario == 1:
    valor = float (input ('Digite o deposito:'))
    if valor > 0:
      saldo += valor
      extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
      print('Operação Invalida!!! \nDigite uma operação valida')
  elif opcao_usuario == 2:

    valor = int (input('Digite o valor do saque:'))
    if saldo <= valor:
      print("Operação Invalida!!! \nSaldo menor que saque.")
    else:
      if valor >= limite:
        print('Operação Invalida!!! \nSaque é maior que valor diario')
      else:
        if valor < 0:
          print ('Operação invalida!!! \nValor do saque informado não é válido.')
        else:
          if numero_saques < LIMITE_SAQUES:
            numero_saques +=1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
  elif opcao_usuario == 3:
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")

  elif opcao_usuario == 4:
      break

  else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")
          
print ('Obrigado!!!')          
    
      