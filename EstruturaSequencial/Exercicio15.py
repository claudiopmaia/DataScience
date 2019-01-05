

""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""


valorHora, horaTrabalhada = input("Quanto voce ganha por hora trabalhada? E quantas horas você trabalhou no mes? ").split()

valorHora = float(valorHora)
horaTrabalhada = int(horaTrabalhada)

salarioBruto = valorHora * horaTrabalhada
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato



print(" O salario Bruto é R$: {:.2f}".format(salarioBruto))
print(" O valor pago ao IR é R$: {:.2f}".format(ir))
print(" O valor pago ao INSS é R$: {:.2f}".format(inss))
print(" O valor pago ao Sindicato é R$: {:.2f}".format(sindicato))
print(" O salario Liquido é R$: {:.2f}".format(salarioLiquido))




