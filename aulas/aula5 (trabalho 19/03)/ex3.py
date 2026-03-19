nivel = 0

while nivel >= 0:

    nivel = (int(input("Qual é o nível do rio hoje? ")))

    if nivel <= 3:
        print ("Estado normal")
    elif nivel > 3 and nivel <= 5:
        print ("Estado de Alerta")
    elif nivel > 5:
        print ("Evacuação imediata")


print ("flag digitada, programa encerrado!")