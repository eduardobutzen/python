frase = input ("Digite uma frase: ")
print ("A frase possui ", len(frase), " caracteres: ", frase)
print ("a frase original é: ", frase)
print ("a frase em maiúscula é: ", frase.upper())
print ("a frase em minúscula é: ", frase.lower())

'''for i in range(len(frase)):
  if (frase[i] == "a"):
    frase[i] = "@"
  if (frase[i] == "e"):
    frase[i] = "&"'''

for i in range(len(frase)):
  if (frase[i] == "a"):
    frase[i] = "@"
  if (frase[i] == "e"):
    frase[i] = "&"