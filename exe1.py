# Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.

import math


raio = float(input("Informe o valor do raio do círculo: "))


area = math.pi * (raio ** 2)

print(f"A área do círculo com raio {raio} é: {area:.2f}")
