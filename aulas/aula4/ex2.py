distancia = int(input("Digite a distância da viagem (quilometros): "))
tempo = float (input("tempo desejado (horas): "))

velocidade_media = distancia / tempo

print ("A velocidade média para fazer essa viagem em " + str (int(tempo)) + " horas é igual a: " + str (velocidade_media) + "km/h")