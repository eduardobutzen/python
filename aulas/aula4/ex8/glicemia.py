class Glicemia:

    def __init__(self, valor, data, hora):
        self.valor = valor
        self.data = data
        self.hora = hora

    def __str__(self):
        return f"Valor: {self.valor} | Data: {self.data} | Hora: {self.hora}"