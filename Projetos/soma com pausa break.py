exit = 999
soma = 0
cont = 0
while True:
    valor = int (input('Digite o Valor:'))
    cont +=1
    if valor == exit:
        break
    soma += valor
print(f'A quantidade de vezes que foi adicionado um novo numero é {cont} e a soma é: {soma}')