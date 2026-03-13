glicemia = float(input("Digite a glicemia: "))
meta_pre_refeicao = float(input("Digite a meta pré refeição: "))
fator_sense = float(input("Digite o fator da sensibilidade: "))

insulina = (glicemia - meta_pre_refeicao) / fator_sense

if insulina < 0:
    print("Não é necessário aplicar insulina.")
else:
    print("A quantidade de insulina que vc deve tomar é:", insulina)

    

