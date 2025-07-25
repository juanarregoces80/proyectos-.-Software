horas = int(input("Ingrese el número de horas estacionado: "))

if horas <= 1:
    tarifa = 5
elif horas <= 3:
    tarifa = 10
else:
    tarifa = 15

print(f"La tarifa a pagar es: ${tarifa}")
