x = 0
print("\nPrograma que calcula os divisores do número inserido")
while x < 1:
    num = int(input("\nDigite Um Numero Positivo: "))
    if num > 0:
        print(f"\nOs divisores de {num} são:\n")
        for i in range(1, num + 1):
            if num % i == 0:
                print(f"{i}\n")
                x += 1
    else:
        print("\nErro ! Digite Um Numero Positivo!")
        continue