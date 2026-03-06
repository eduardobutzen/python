#Outro jeito de validar cpf

while True:
  cpf = input ("Digite seu CPF(use somento números): ")
  if (len(cpf) != 11 and (cpf[0] != '0')):
    break
  print("CPF inválido")