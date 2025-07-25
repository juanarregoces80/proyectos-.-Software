saldoinicial = float(input("Ingrese el saldo inicial del ahorrador: "))
numbermounths = int(input("Ingrese el número de meses: "))

monto = 0.015 * saldoinicial * numbermounths
saldofinal = saldoinicial + monto

print("El saldo final equivale a:", saldofinal)
