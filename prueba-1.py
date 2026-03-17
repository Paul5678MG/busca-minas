multiplicador = 3

cantidad = multiplicador * multiplicador

for num in range(1,cantidad+1):
    if num % multiplicador == 0:
        print(num, end="\n")
    else:
        print(num, end=" ")

