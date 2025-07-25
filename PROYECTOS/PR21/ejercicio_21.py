lados = int(input("Número de lados de la figura: "))

if lados == 3:
    print("Triángulo")
elif lados == 4:
    print("Cuadrado o rectángulo")
elif lados == 5:
    print("Pentágono")
elif lados == 6:
    print("Hexágono")
else:
    print("Figura no soportada")
