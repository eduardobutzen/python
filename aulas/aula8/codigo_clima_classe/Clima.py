import requests


class ClimaService:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def buscar(self, cidade: str) -> dict | None:
        """Faz a requisição à API e retorna os dados brutos, ou None em caso de erro."""
        params = {
            "q": cidade,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br",
        }
        resposta = requests.get(self.BASE_URL, params=params)

        if resposta.status_code == 200:
            return resposta.json()

        print(f"Erro ao obter dados para '{cidade}': HTTP {resposta.status_code}")
        return None

    def exibir(self, cidade: str) -> None:
        """Busca e exibe o clima formatado para uma cidade."""
        dados = self.buscar(cidade)
        if dados is None:
            return

        main    = dados["main"]
        weather = dados["weather"][0]
        wind    = dados["wind"]

        print(f"Cidade:               {cidade.capitalize()}")
        print(f"Temperatura:          {main['temp']}°C")
        print(f"Temperatura Mínima:   {main['temp_min']}°C")
        print(f"Temperatura Máxima:   {main['temp_max']}°C")
        print(f"Condição:             {weather['description'].capitalize()}")
        print(f"Umidade:              {main['humidity']}%")
        print(f"Velocidade do vento:  {wind['speed']} m/s")
        print("-" * 40)

    def exibir_varias(self, cidades: list[str]) -> None:
        """Exibe o clima para uma lista de cidades."""
        for cidade in cidades:
            self.exibir(cidade)


if __name__ == "__main__":
    api_key = "57f02dc11685a9611b42a5a22012380c"
    cidades = ["Santa Maria", "São Paulo", "Brasília"]

    servico = ClimaService(api_key)
    servico.exibir_varias(cidades)