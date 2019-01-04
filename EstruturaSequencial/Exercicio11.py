""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. """

import  math
int1, int2, real1 = input("Digite dois números inteiros e um número real:").split()

int1 = int(int1)
int2 = int(int2)
real1 = float(real1)

valor = (int1 * int1) * (int2 / 2)

print("o produto do dobro do primeiro com metade do segundo  {:.0f} " .format(valor))

valor = (math.pow(int1, 3)) + real1

print("a soma do triplo do primeiro com o terceiro  {:.0f} " .format(valor))

valor = math.pow(real1, 3)

print("o terceiro elevado ao cubo.  {:.0f} " .format(valor))
