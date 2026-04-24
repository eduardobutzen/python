import csv

def tratamento(caminho_arquivo):
    with open(caminho_arquivo) as arquivo:
        lista = arquivo.read().splitlines()

    lista.sort()
    return lista


def analisar_texto(lista):
    frase = input('Digite uma frase para ser analisada: ')
    lista_texto = frase.split()

    for palavra_negativa in lista:
        ocorrencia = 0

        for palavra_texto in lista_texto:
            if palavra_negativa == palavra_texto:
                ocorrencia += 1

        if ocorrencia > 0:
            print(f'A palavra "{palavra_negativa}" foi encontrada {ocorrencia} vezes')


def main():
    caminho = "D:/faculdade/python/aulas/aula7/projeto/lista.csv"

    lista = tratamento(caminho)
    analisar_texto(lista)


main()