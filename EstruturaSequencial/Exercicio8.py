""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
"""
valorHora, horaTrabalhada = input("Digite o valor da hora trabalhada e a quantidade de horas trabalhada:").split()

valorHora = float(valorHora)
horaTrabalhada = int(horaTrabalhada)

salario = valorHora * horaTrabalhada

print(" O salario do mês é R$: {:.2f}".format(salario))