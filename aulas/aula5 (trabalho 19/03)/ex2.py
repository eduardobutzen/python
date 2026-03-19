heroivida = 100 
monstrovida = 100

while heroivida > 0 and monstrovida > 0:

    dano = (int(input("quanto de dano quer dar ao heroi? ")))
    heroivida = heroivida - dano
    dano = (int(input("Quanto de dano quer dar ao monstro? ")))
    monstrovida = monstrovida - dano

    print ("Vida do herói: ", heroivida)
    print ("Vida do monstro: ", monstrovida)

if monstrovida == 0:
    print ("vitória do herói")
else:
    print ("Vitória do monstro")
