cadastro = ""
masculino = idade18 = idade_feminina = 0

while True:
  while True:
    entrada = str(input('Feminino ou Masculino? F/M:'))
    if entrada.upper() == 'M' and entrada.upper() == 'F':
      entrada = str(input('Homem ou Mulher? M/F:'))
    else:
      break
  if entrada.upper() == 'M':
    masculino += 1
    while True:
      idade = int (input("Digite sua idade:"))
      if idade > 0:
        break
    if idade > 18:
      idade18 += 1
  elif entrada.upper() == 'F':
    while True:
      idade = int (input("Digite sua idade:"))
      if idade > 0:
        break
    if idade > 18:
      idade18 =+ 1
    elif idade < 20:
      idade_feminina += 1
  cadastro = str (input('Deseja cadastrar mais uma pessoa (S/N)'))
  if cadastro.upper() == 'N':
    break
  
painel_superior = "╔════════════════════════════════════════════════════╗"
painel_titulo =   "║                    Cadastro                        ║"
painel_vazio =    "║                                                    ║"
dados_18_anos =  f"║ Pessoas com mais de 18 anos: {idade18}                     ║"
dados_homens =   f"║ Quantos homens foram cadastrados: {masculino}                ║"
dados_mulheres = f"║ Mulheres com menos de 20 anos: {idade_feminina}                   ║"
painel_inferior = "╚════════════════════════════════════════════════════╝"


print(painel_superior)
print(painel_titulo)
print(painel_vazio)
print(dados_18_anos)
print(dados_homens)
print(dados_mulheres)
print(painel_vazio)
print(painel_inferior)
    
    
        
      
    
  