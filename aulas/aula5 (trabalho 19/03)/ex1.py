biomassameta = (int(input("Digite a meta de biomassa: ")))

biomassa = 0
soma = 0 
contador = 0

while biomassa == soma:

    biomassa = (int(input("Quanto de biomassa tem a arvore que vc plantou? ")))
    soma = soma + biomassa
    contador = contador + 1

print ("A quantidade de biomassa atingiu a meta com ", contador, " árvores")

    