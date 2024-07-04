cem_reais = ciquenta_reais = vinte_reais = dez_reais = cinco_reais = dois_reais = 0 
um_real =  ciquenta_cent = vinte_cinco_cent = dez_cent = cinco_cent = um_centavo = 0

moeda = float (input())

while moeda > 0:
  if moeda >= 100:
    cem_reais += 1
    moeda -= 100
  elif moeda >= 50:
    ciquenta_reais += 1
    moeda -= 50
  elif moeda >= 20:
    vinte_reais +=1
    moeda -= 20
  elif moeda >= 10:
    dez_reais += 1
    moeda -= 10
  elif moeda >= 5:
    cinco_reais +=1
    moeda -= 5
  elif moeda >= 2:
    dois_reais += 1
    moeda -= 2
  elif moeda >= 1:
    um_real += 1
    moeda -= 1
  elif moeda >= 0.50:
    ciquenta_cent +=1
    moeda -= 0.50
  elif moeda >= 0.25:
    vinte_cinco_cent += 1
    moeda -= 0.25
  elif moeda >= 0.10:
    dez_cent += 1
    moeda -= 0.10
  elif moeda >= 0.05:
    cinco_cent += 1
    moeda -= 0.05
  elif moeda >= 0.01:
    um_centavo += 1
    moeda -= 0.01

print('NOTAS: \n{:.2f} nota(s) de R$ 100.00 \n{:.2f} nota(s) de R$ 50.00 \n{:.2f} nota(s) de R$ 20.00 \n{:.2f} nota(s) de R$ 10.00 \n{:.2f} nota(s) de R$ 5.00 \n{:.2f} nota(s) de R$ 2.00'.format(cem_reais, ciquenta_reais, vinte_reais, dez_reais, cinco_reais, dois_reais))

print ('NOTAS: \nmoeda(s) de R$ 1.00 ',format(um_real))

print('\n{:.2f} moeda(s) de R$ 0.50 \n{:.2f} moeda(s) de R$ 0.25 \n{:.2f} moeda(s) de R$ 0.10 \n{:.2f} moeda(s) de R$ 0.05 \n{:.2f} moeda(s) de R$ 0.01'.format(ciquenta_cent,vinte_cinco_cent,dez_cent,cinco_cent,um_centavo ))
  
    
    

  
    
    
  