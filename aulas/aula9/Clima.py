import requests


class CidadeClima:

    def __init__(self, nome, temperatura, umidade, condicao):
        self.nome = nome
        self.temperatura = temperatura
        self.umidade = umidade
        self.condicao = condicao

    def __str__(self):
        return (
            f"Cidade: {self.nome}\n"
            f"Temperatura: {self.temperatura:.1f} °C\n"
            f"Umidade: {self.umidade}%\n"
            f"Condição: {self.condicao.capitalize()}"
        )


API_KEY = "c72a841b3e6030ece59d7a062a3d6b42"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cidades = ["São Paulo", "London", "Tokyo", "New York", "Paris"]

relatorio_clima = []

for cidade in cidades:
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }
    resposta = requests.get(BASE_URL, params=parametros)
    dados = resposta.json()

    objeto = CidadeClima(
        dados["name"],
        dados["main"]["temp"],
        dados["main"]["humidity"],
        dados["weather"][0]["description"]
    )
    relatorio_clima.append(objeto)

for cidade_clima in relatorio_clima:
    print(cidade_clima)
    print()