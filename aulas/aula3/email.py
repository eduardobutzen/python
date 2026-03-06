# fazer email @ufn.edu.br

nome_completo = input ("Digite seu nome completo: ")
palavras_nome = nome_completo.split(" ")
print("seu email é: ", palavras_nome[0].lower() + "." + palavras_nome[-1].lower() + "@ufn.edu.br")

