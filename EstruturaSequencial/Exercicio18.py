""" Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
    que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


areaParaPintar = input("Qqual o tamanho em metros quadrados da área a ser pintada? ")

areaParaPintar = float(areaParaPintar)
qtdLitros = areaParaPintar / 6
qtdLatas = areaParaPintar/18
qtdGaloes = areaParaPintar/3.6
valorTotalGaloes = qtdLatas * 25
valorTotalLatas = qtdLatas * 80


print(" Voce vai precisar de : {:.0f} litros de tintas".format(qtdLitros))
print(" Quantidades de latas para o serviço é : {:.0f} Latas".format(qtdGaloes))
print(" O valor para o serviço é R$: {:.2f}".format(valorTotalGaloes))
print(" Quantidades de latas para o serviço é : {:.0f} Latas".format(qtdLatas))
print(" O valor para o serviço é R$: {:.2f}".format(valorTotalLatas))







