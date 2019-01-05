""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
    que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


areaParaPintar = input("Qqual o tamanho em metros quadrados da área a ser pintada? ")

areaParaPintar = int(areaParaPintar)
qtdLitros = areaParaPintar / 3
qtdLatas = areaParaPintar/18
valorTotal = qtdLatas * 80


print(" Voce vai precisar de : {:.0f} litros de tintas".format(qtdLitros))
print(" Quantidades de latas para o serviço é : {:.0f} Latas".format(qtdLatas))
print(" O valor para o serviço é R$: {:.2f}".format(valorTotal))







