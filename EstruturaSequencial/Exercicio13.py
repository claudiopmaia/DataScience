""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7   """


altura = input("Digite sua altura:")

altura = float(altura)

pesoIdeal = (72.7*altura) - 58

print("Seu peso ideal se for homem é .  {:.2f} Kilos " .format(pesoIdeal))

pesoIdeal = (62.1*altura) - 44.7

print("Seu peso ideal se for mulher é .  {:.2f} Kilos " .format(pesoIdeal))