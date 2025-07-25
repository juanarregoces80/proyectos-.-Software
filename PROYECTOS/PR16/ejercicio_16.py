num = int(input("Ingresa un número entero: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible por 2 y por 3")
elif num % 2 == 0:
    print("Divisible solo por 2")
elif num % 3 == 0:
    print("Divisible solo por 3")
else:
    print("No es divisible por 2 ni por 3")
