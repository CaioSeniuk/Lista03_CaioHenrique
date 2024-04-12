lista = [2,4,7,2,3,3,1,0,2,6]
maior = []
print("\nPrograma que identifica automaticamente qual o número que mais se repete dentro da função [2,4,7,2,3,3,1,0,2,6]")
for i in lista:
    maior.append(lista.count(i))
maisrepetido = lista[maior.index(max(maior))]
print(f"\nO número mais repetido na lista foi o: {maisrepetido}\n\n")