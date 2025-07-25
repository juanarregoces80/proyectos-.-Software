years = int(input("Ingrese la cantidad de años en la empresa: "))

if years >= 1:
    bn1 = 100000
    bnfinal = bn1 + (years - 1) * 120000
else:
    bnfinal = 0

print("El Bono a pagar es de:", bnfinal)
