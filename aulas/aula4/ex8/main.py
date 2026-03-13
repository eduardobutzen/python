import glicemia

lista = []

leitor = open(lista, "r", encoding="utf-8")

for linha in leitor:

        linha = linha.strip()
        vetor_linha = linha.split(",")

        valor = int(vetor_linha[0])
        data = vetor_linha[1]
        hora = vetor_linha[2]

        obj = glicemia(valor, data, hora)

        lista.append(obj) = input ("Digite a glicemia [valor,data,hora]")

for item in leitor:
        print(item)

