velocidad = int(input("Ingresa la velocidad (km/h): "))

if velocidad <= 20:
    print("Muy lento")
elif velocidad <= 60:
    print("Moderado")
elif velocidad <= 120:
    print("Rápido")
else:
    print("Muy rápido")
