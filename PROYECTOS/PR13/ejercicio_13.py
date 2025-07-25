monto = float(input("Ingresa el monto en dólares: "))
moneda = input("Elige la moneda (euros, pesos, yenes): ").lower()

match moneda:
    case "euros":
        print(f"{monto} USD = {monto * 0.85} EUR")
    case "pesos":
        print(f"{monto} USD = {monto * 4100} COP")
    case "yenes":
        print(f"{monto} USD = {monto * 110} JPY")
    case _:
        print("Moneda no soportada.")
