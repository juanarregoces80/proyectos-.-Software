conversion = input("Elige la conversión (1: km a millas, 2: C a F, 3: kg a libras): ")

match conversion:
    case "1":
        km = float(input("Ingresa kilómetros: "))
        if km >= 0:
            millas = km * 0.621371
            print(f"{km} km = {millas} millas")
        else:
            print("Valor no válido.")
    case "2":
        c = float(input("Ingresa grados Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    case "3":
        kg = float(input("Ingresa kilogramos: "))
        if kg >= 0:
            libras = kg * 2.20462
            print(f"{kg} kg = {libras} libras")
        else:
            print("Valor no válido.")
    case _:
        print("Opción inválida.")
