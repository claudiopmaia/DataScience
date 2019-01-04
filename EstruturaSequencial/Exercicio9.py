# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
tempFarenheit= input("Qual a temperatura em Farenheit:")

tempFarenheit = int(tempFarenheit)

tempCelius = (5*(tempFarenheit-32)/9)

print("A temperatura em Celsius é {:.4f} " .format(tempCelius))