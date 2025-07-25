mes = int(input("Número del mes (1-12): "))

if 1 <= mes <= 3:
    print("Primer trimestre")
elif 4 <= mes <= 6:
    print("Segundo trimestre")
elif 7 <= mes <= 9:
    print("Tercer trimestre")
elif 10 <= mes <= 12:
    print("Cuarto trimestre")
else:
    print("Mes no válido")
