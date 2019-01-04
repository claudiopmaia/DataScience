# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Digite as quantros notas do bimestre")
A, B, N, M = input().split()
N = int(N)
M = int(M)
A = int(A)
B = int(B)
print("A sua media é {}".format((N + M + A + B)/4))