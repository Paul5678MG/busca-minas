import random

multiplicador = int(input("Multiplicador para matriz: "))

numeros = []
cantidad = multiplicador * multiplicador

for num in range(1,cantidad+1):
    if num % multiplicador == 0:
        print(num, end="\n")
        numeros.append([num,""])
    else:
        print(num, end=" ")
        numeros.append([num,""])

bombas = []
while len(bombas) < multiplicador:
    bomba = random.randint(1,cantidad)
    if bomba not in bombas:
        bombas.append(bomba)

for n in numeros:
    for b in bombas:
        if n[0] == b:
            n[1] = f"Bomba💥"

respuesta = int(input("Seleccionar un número: "))

for n in numeros:
    if n[0] == respuesta:
        if n[1] != "":
            print(n[1])
            print("Game-Over❌")
            exit()
print("Ganaste✅")