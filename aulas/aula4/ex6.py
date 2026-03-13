estado = input("Digite a sigla do estado onde a pessoa nasceu: ").upper()

if estado == "RJ":
    print("Carioca")

elif estado == "SP":
    print("Paulista")

elif estado == "MG":
    print("Mineiro")

elif estado == "AC" or estado == "AL" or estado == "AP" or estado == "AM" or estado == "BA" or estado == "CE" or estado == "DF" or estado == "ES" or estado == "GO" or estado == "MA" or estado == "MT" or estado == "MS" or estado == "PA" or estado == "PB" or estado == "PR" or estado == "PE" or estado == "PI" or estado == "RN" or estado == "RS" or estado == "RO" or estado == "RR" or estado == "SC" or estado == "SE" or estado == "TO":
    print("Outros estados")

else:
    print("Sigla inválida")