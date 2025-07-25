temp = float(input("Ingresa la temperatura: "))
unidad = input("Ingresa la unidad (C para Celsius, F para Fahrenheit): ").upper()

if unidad == "C":
    convertida = (temp * 9/5) + 32
    print(f"{temp}°C equivalen a {convertida}°F")
elif unidad == "F":
    convertida = (temp - 32) * 5/9
    print(f"{temp}°F equivalen a {convertida}°C")
else:
    print("Unidad no válida.")
