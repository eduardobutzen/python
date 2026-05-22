import requests


class InflacaoService:
    """
    Busca dados mensais do IPCA (inflação oficial do Brasil)
    diretamente da API pública do IBGE — sem chave de acesso necessária.

    Tabela SIDRA 1419 → IPCA variação mensal (%)
    Fonte: https://servicodados.ibge.gov.br
    """

    BASE_URL = "https://servicodados.ibge.gov.br/api/v3/agregados/1419/periodos/{periodo}/variaveis/63"
    MESES = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março",
        "04": "Abril",   "05": "Maio",      "06": "Junho",
        "07": "Julho",   "08": "Agosto",    "09": "Setembro",
        "10": "Outubro", "11": "Novembro",  "12": "Dezembro",
    }

    def __init__(self, ano: int):
        self.ano = ano

    def _montar_periodo(self) -> str:
        """Gera a string de período no formato AAAAMM para os 12 meses do ano."""
        return "|".join(f"{self.ano}{mes:02d}" for mes in range(1, 13))

    def buscar(self) -> list[dict]:
        """Faz a requisição à API do IBGE e retorna lista de {'mes', 'variacao'}."""
        url = self.BASE_URL.format(periodo=self._montar_periodo())
        params = {"localidades": "N1[all]"}  # Brasil inteiro

        resposta = requests.get(url, params=params)

        if resposta.status_code != 200:
            print(f"Erro na requisição: HTTP {resposta.status_code}")
            return []

        dados_brutos = resposta.json()

        # Navega na estrutura JSON da API do IBGE
        series = dados_brutos[0]["resultados"][0]["series"][0]["serie"]

        resultados = []
        for periodo, valor in series.items():
            mes_num = periodo[4:]  # Ex: "202401" → "01"
            resultados.append({
                "periodo": periodo,
                "mes":     self.MESES.get(mes_num, mes_num),
                "variacao": float(valor) if valor not in (None, "") else None,
            })

        return resultados

    def exibir(self) -> None:
        """Exibe os dados de inflação mensais formatados no terminal."""
        dados = self.buscar()
        if not dados:
            print("Nenhum dado encontrado.")
            return

        print(f"\n{'=' * 45}")
        print(f"  IPCA — Inflação mensal {self.ano} (Fonte: IBGE)")
        print(f"{'=' * 45}")
        print(f"  {'Mês':<12} {'Variação (%)':>12}")
        print(f"  {'-'*12} {'-'*12}")

        acumulado = 1.0
        for item in dados:
            if item["variacao"] is not None:
                acumulado *= (1 + item["variacao"] / 100)
                print(f"  {item['mes']:<12} {item['variacao']:>+11.2f}%")
            else:
                print(f"  {item['mes']:<12} {'N/D':>12}")

        acumulado_pct = (acumulado - 1) * 100
        print(f"  {'-'*12} {'-'*12}")
        print(f"  {'Acumulado':<12} {acumulado_pct:>+11.2f}%")
        print(f"{'=' * 45}\n")


if __name__ == "__main__":
    ano = int(input("Digite o ano desejado (ex: 2024): "))
    servico = InflacaoService(ano)
    servico.exibir()