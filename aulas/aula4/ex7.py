nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print ("Aluno aprovado com a media: " + str((media)))
elif media < 7 and media >= 3:
    print ("Aluno em recuperação: " + str (media))
else:
    print ("Aluno reprovado com a média " +str((media)))