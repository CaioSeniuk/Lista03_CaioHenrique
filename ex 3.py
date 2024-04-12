print("\n")
while True:
    numero = int(input("\nInsira um número positivo inteiro entre 1 e 10: "))
    if numero > 10 or numero < 1:
        print(f"\nErro ! Insira um número válido !")
        continue
    else:
        for i in range(1,11):
            print(numero, "x", i, "=", numero *i)
    break