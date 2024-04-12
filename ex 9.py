numeros = []
print("\nPrograma que ordena os 10 números digitados de forma crescente")
for i in range(10):
    numero = int(input(f"\nDigite o {i+1}º número inteiro: "))
    numeros.append(numero)
x = sorted(numeros)
print(f"\nNúmeros em ordem crescente: {x}\n")