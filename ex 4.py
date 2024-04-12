print("\nPrograma que calcula a média das idades inseridas\n")
qtdIdade = int(input("\nDigite a quantidade de idades para calcular a média: "))
somaIdade = 0 
contador = 0
while contador < qtdIdade:
    idade = int(input(f"\nInsira a idade nº{contador+1}: "))
    if idade < 0:
        print("\nErro ! Insira uma idade válida !\n")
        continue
    else:
        somaIdade += idade
        contador +=1
print(f"\nA média das idades é igual a: {somaIdade/qtdIdade:.2f} anos\n")

    