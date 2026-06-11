import csv
from candidato import Candidato

class SistemaDeTriagem:
    def __init__(self, arquivo_csv):
        self.candidatos = []
        self.carregar_dados(arquivo_csv)

    def carregar_dados(self, arquivo_csv):
        try:
            with open(arquivo_csv, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    candidato = Candidato(
                        id_cand=row['ID'],
                        nome=row['Nome'],
                        idade=row['Idade'],
                        exp=row['Exp'],
                        tecnico=row['Tecnico'],
                        ingles=row['Ingles']
                    )
                    self.candidatos.append(candidato)
        except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")

    def desafio1_qualificacao_tecnica(self):
        print("=" * 50)
        print("DESAFIO 1: Triagem de Qualificação Técnica (Operador E)")
        print("Candidatos com maioridade legal (>=18) E curso técnico completo")
        print("=" * 50)
        for c in self.candidatos:
            if c.idade >= 18 and c.tecnico:
                print(f"ID: {c.id} | Nome: {c.nome}")
        print()

    def desafio2_talentos_internacionais(self):
        print("=" * 50)
        print("DESAFIO 2: Expansão de Talentos Internacionais (Operador OU)")
        print("Maturidade profissional (exp >= 3) OU domínio de inglês")
        print("=" * 50)
        for c in self.candidatos:
            if c.exp >= 3 or c.ingles:
                print(f"ID: {c.id} | Nome: {c.nome}")
        print()

    def desafio3_potencial_jovem(self):
        print("=" * 50)
        print("DESAFIO 3: Filtro de Potencial Jovem (Lógica Combinada)")
        print("Menos de 25 anos E (curso técnico OU experiência >= 1)")
        print("=" * 50)
        for c in self.candidatos:
            if c.idade < 25 and (c.tecnico or c.exp >= 1):
                print(f"ID: {c.id} | Nome: {c.nome}")
        print()

    def desafio4_classificacao_salarial(self):
        print("=" * 50)
        print("DESAFIO 4: Classificação Salarial (Operação Condicional)")
        print("Experiência > 5 anos -> SÊNIOR, SENÃO -> JÚNIOR")
        print("=" * 50)
        for c in self.candidatos:
            if c.exp > 5:
                print(f"Nome: {c.nome} | Categoria: SÊNIOR")
            else:
                print(f"Nome: {c.nome} | Categoria: JÚNIOR")
        print()

    def executar_todos_desafios(self):
        self.desafio1_qualificacao_tecnica()
        self.desafio2_talentos_internacionais()
        self.desafio3_potencial_jovem()
        self.desafio4_classificacao_salarial()
