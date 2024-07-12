total = 0
valor = float (input())
total = valor
cedula = 100
cont_cedula = 0
while True:
  if total >= cedula:
    total -= cedula
    cont_cedula +=1
  else:
    if cont_cedula > 0:
      print (f'{cont_cedula} nota(s) de R$ {cedula:.2f}')
    if cedula == 100:
      cedula = 50.00
      cont_cedula = 0
    elif cedula == 50.00:
      cedula = 20.00
      cont_cedula = 0
    elif cedula == 20.00:
      cedula = 10.00
      cont_cedula = 0
    elif cedula == 10.00:
      cedula = 5.00
      cont_cedula = 0
    elif cedula == 5.00:
      cedula = 1.00
      cont_cedula = 0
    if total == 0:
      break
  

  
  
  
    
  
  