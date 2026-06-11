import os
from sistema_triagem import SistemaDeTriagem

def main():
    csv_path = os.path.join(os.path.dirname(__file__), 'candidatos.csv')
    sistema = SistemaDeTriagem(csv_path)
    if sistema.candidatos:
        sistema.executar_todos_desafios()

if __name__ == "__main__":
    main()
