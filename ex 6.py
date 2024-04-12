print("\n")
dentro = 0
fora = 0
for i in range(10):
    num = int(input("\nInsira um número: "))
    if 10 <= num <= 20:
        dentro += 1
    else:
        fora += 1
print(f"\nQuantidade de números dentro do intervalo [10,20]: {dentro}" + f"\nQuantidade de números fora do intervalo [10,20]: {fora}\n")
