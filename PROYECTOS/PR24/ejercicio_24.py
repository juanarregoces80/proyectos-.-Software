ica = int(input("Ingresa el índice de calidad del aire (ICA): "))

if ica <= 50:
    print("Bueno")
elif ica <= 100:
    print("Moderado")
elif ica <= 150:
    print("No saludable para grupos sensibles")
elif ica <= 200:
    print("No saludable")
elif ica <= 300:
    print("Muy no saludable")
else:
    print("Peligroso")
