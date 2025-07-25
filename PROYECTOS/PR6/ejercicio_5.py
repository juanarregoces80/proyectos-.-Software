precio = float(input("Ingrese el precio del producto: "))
tipo = input("Ingrese el tipo de cliente (A/B/C): ").upper()

if tipo == "A":
    descuento = 0.30
elif tipo == "B":
    descuento = 0.20
elif tipo == "C":
    descuento = 0.10
else:
    descuento = 0

precio_final = precio * (1 - descuento)
print(f"El precio final con descuento es: {precio_final}")
