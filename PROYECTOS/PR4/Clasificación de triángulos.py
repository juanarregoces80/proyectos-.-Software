lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))

if lado1 == lado2 == lado3:
    print("El triángulo es Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es Isósceles.")
else:
    print("El triángulo es Escaleno.")
