valores = []
pares = []
impares = []
soma_pares = 0
soma_impares = 0

print("Digite 10 valores:")
for i in range(10):
    valor = int(input(f"Valor {i+1}: "))
    valores.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
        soma_pares += valor
    else:
        impares.append(valor)
        soma_impares += valor

tupla_impares = tuple(impares)

quantidade_pares = len(pares)
quantidade_impares = len(impares)

# Exibe os resultados
print("\nNúmeros pares:", pares)
print("Números ímpares (em tupla):", tupla_impares)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma de todos os números pares:", soma_pares)
print("Soma de todos os números ímpares:", soma_impares)