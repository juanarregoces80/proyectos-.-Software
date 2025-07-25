edad = int(input("Indique su edad: "))
sexo = input("Indique si su sexo es masculino o femenino (M o F): ")

if sexo.lower() == "m":
    hpulsos = (210 - edad) / 10
else:
    hpulsos = (220 - edad) / 10

print("El número de pulsaciones que usted tiene es de:", hpulsos)
