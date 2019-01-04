# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
print("Digite a medida do raio")
R = input()
R = int(R)
A = math.pi * (R * R)
print("A Área do circulo é {:.2f} centimetros ".format(A))