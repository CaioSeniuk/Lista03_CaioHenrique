pares = 0 
impares = 0
print("\nPrograma que identifica números pares e ímpares\n")
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        pares += 1
    else: 
        impares += 1
print(f"\nQuantidade De números Pares: {impares}\n" + f"Quantidade De números Ímpares: {pares}\n")
