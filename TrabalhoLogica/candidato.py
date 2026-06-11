class Candidato:
    def __init__(self, id_cand, nome, idade, exp, tecnico, ingles):
        self.id = id_cand
        self.nome = nome
        self.idade = int(idade)
        self.exp = int(exp)
        self.tecnico = tecnico.strip().lower() == 'sim'
        self.ingles = ingles.strip().lower() == 'sim'
