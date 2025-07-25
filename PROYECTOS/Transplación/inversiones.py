inv1 = float(input("Ingrese la cantidad a invertir por la 1ra persona: "))
inv2 = float(input("Ingrese la cantidad a invertir por la 2da persona: "))
inv3 = float(input("Ingrese la cantidad a invertir por la 3ra persona: "))

invtotal = inv1 + inv2 + inv3

p1 = inv1 * 100 / invtotal
p2 = inv2 * 100 / invtotal
p3 = inv3 * 100 / invtotal

print("El Porcentaje que invierte la 1ra persona es de:", p1, "%")
print("El Porcentaje que invierte la 2da persona es de:", p2, "%")
print("El Porcentaje que invierte la 3ra persona es de:", p3, "%")
