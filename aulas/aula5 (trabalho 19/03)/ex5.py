dias = int(input("Quantos dias deseja analisar? "))

contador = 0
soma = 0

while contador < dias:
    temp = float(input(f"Digite a temperatura do dia {contador + 1}: "))
    soma = soma + temp
    contador = contador + 1

media = soma / dias

print(f"Média das temperaturas: {media:.2f}°C")

if media > 25:
    print("Acima do esperado")
else:
    print("Dentro da normalidade")