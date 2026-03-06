#implementações e restrições

eh_invalida_data = True
while (eh_invalida_data):
  eh_invalida_data = False

data  = input ("Digite uma data: ")
dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)

if(dia < 1 or dia > 31):
  print("Data inválida como dia inválido")
  eh_invalida_data = True
  
if(ano < 1990 or ano > 2023):
  print("Data invaálida como ano inválido")
  eh_invalida_data = True
  
if(mes < 1 or mes > 12):
  print("Data inválida como mês inválido")
  eh_invalida_data = True

cpf = input ("Digite seu CPF(use somento números): ")
if (len(cpf) != 11):
  print("CPF inválido")
  


