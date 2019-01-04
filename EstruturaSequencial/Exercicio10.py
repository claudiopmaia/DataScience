# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
tempCelius= input("Qual a temperatura em Farenheit:")

tempCelius = int(tempCelius)

tempFarenheit = (tempCelius * 1,8) + 32

print("A temperatura em Celsius é {:.4f} " .format(tempCelius))