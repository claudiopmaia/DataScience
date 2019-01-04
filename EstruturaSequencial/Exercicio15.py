""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
    que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


areaPintar = input("Qqual o tamanho em metros quadrados da área a ser pintada? ")

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




