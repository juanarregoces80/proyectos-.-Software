sensores = int(input("Cantidad de sensores activados: "))

if sensores <= 2:
    print("Alerta baja")
elif sensores <= 5:
    print("Alerta media")
else:
    print("Alerta alta")
