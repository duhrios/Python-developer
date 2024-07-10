numero_um = int(input(""))
numero_dois = int(input(""))
numero_tres = int(input(""))

if numero_um > numero_dois and numero_um > numero_tres and numero_dois > numero_tres:
  print ('A ordem é {} {} {}'.format(numero_um,numero_dois, numero_tres))
elif numero_um > numero_dois and numero_dois < numero_tres:
  print('A ordem é {} {} {}'.format(numero_um,numero_tres,numero_dois))
elif numero_dois > numero_um and numero_tres < numero_um:
  print('A ordem é {} {} {}'.format(numero_dois,numero_um,numero_tres))
elif numero_dois > numero_um and numero_tres > numero_um:
  print('A ordem é {} {} {}'.format(numero_dois,numero_tres,numero_um))
elif numero_tres > numero_um and numero_um > numero_dois:
  print('A ordem é {} {} {}'.format(numero_tres, numero_um, numero_dois))
elif numero_tres > numero_dois and numero_dois > numero_um:
  print('A ordem é {} {} {}'.format(numero_tres, numero_dois, numero_um))

  
  