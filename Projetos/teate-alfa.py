digite = input('Digite qualquer coisa:')
  if digite.isalnum():
    print(f"{digite} é alfanumérico.")
  elif digite.isalpha():
    print(f"{digite} contém apenas letras.")
  elif digite.isnumeric():
    print(f"{digite} contém apenas números.")
  else:
    print(f"{digite} não se encaixa em nenhuma categoria.")
