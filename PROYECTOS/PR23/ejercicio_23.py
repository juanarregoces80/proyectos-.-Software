edad_perro = int(input("Ingresa la edad del perro: "))

if edad_perro <= 2:
    edad_humana = edad_perro * 10.5
else:
    edad_humana = 2 * 10.5 + (edad_perro - 2) * 4

print(f"Edad equivalente en humanos: {edad_humana}")
