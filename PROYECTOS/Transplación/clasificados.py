P = int(input("Escriba cuántas palabras hay en total: "))
C = int(input("Escriba cuántos cm hay en total: "))
R = int(input("Escriba cuántos colores se han usado en total: "))

PS = P * 20000
CMS = C * 15000
CRS = R * 25000

Precio = PS + CMS + CRS

print("El precio total es de", Precio, "$")
