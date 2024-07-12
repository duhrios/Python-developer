total = custa1000 = 0
prod_mais_barato = float('inf')
nome_mais_barato = ""

while True:
  nome = str(input("Qual é o nome do produto:"))
  valor_produto = float(input(f'Digite o valor do(a) {nome}: R$ '))
  total += valor_produto
  if valor_produto < prod_mais_barato:
      nome_mais_barato = nome
  if valor_produto >= 1000:
      custa1000 += 1
  cadastro = ' '
  while cadastro not in 'SN':
    cadastro = str (input ('Digite se quer continuar (S/N): ')).strip().upper()[0]
  if cadastro == 'N':
    break
print(f'\nO Total da compra foi {total:.2f}R$\n\n'
  f'A quantidade de produtos que custa 1000 é {custa1000}R$\n\n'
  f'O produto mais barato foi {nome_mais_barato} que custou {prod_mais_barato}R$')
