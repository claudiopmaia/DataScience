""" Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58  """


altura = input("Digite sua altura:")

altura = float(altura)

pesoIdeal = (72.7*altura) - 58

print("Seu peso ideal é .  {:.2f} Kilos " .format(pesoIdeal))