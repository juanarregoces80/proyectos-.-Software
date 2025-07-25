basesueldo = float(input("Ingrese el sueldo base de sus trabajadores: "))

leypolitica = basesueldo * 0.01
segsocial = basesueldo * 0.04
segforzoso = basesueldo * 0.005
box_ahorro = basesueldo * 0.05

amount_total = basesueldo - leypolitica - segsocial - segforzoso - box_ahorro

print("El Monto a descontar en caja de ahorro es:", box_ahorro)
print("El Monto a descontar en la ley de política pública es:", leypolitica)
print("El Valor a descontar del seguro forzoso es de:", segforzoso)
print("Valor de seguro social:", segsocial)
print("El Monto a pagar a los trabajadores es de:", amount_total)
