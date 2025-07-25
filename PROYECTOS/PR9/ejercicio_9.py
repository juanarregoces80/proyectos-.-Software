mes = int(input("Ingresa el número del mes (1-12): "))

if mes in [3, 4, 5]:
    print("Es Primavera.")
elif mes in [6, 7, 8]:
    print("Es Verano.")
elif mes in [9, 10, 11]:
    print("Es Otoño.")
elif mes in [12, 1, 2]:
    print("Es Invierno.")
else:
    print("Mes no válido.")
