#Faça um Programa que peça dois números e imprima o maior deles.

A, B = input("Digite dois numeros ").split()
A = int(A)
B = int(B)

if A > B:
    print("O numero maior dos dois foi o primeiro numero que é:", A)
else:
    print("O numero maior dos dois foi segundo numero que foi o:", B)