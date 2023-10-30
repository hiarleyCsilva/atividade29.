# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = float('-inf')  
menor_peso = float('inf')   
for i in range(1, 6):

    peso = float(input(f"Digite o seu peso {i}: "))

    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f"O maior peso lido é: {maior_peso} kg")
print(f"O menor peso lido é: {menor_peso} kg")
