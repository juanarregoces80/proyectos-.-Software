clima = input("¿Cómo está el clima? (soleado, lluvioso, frío): ").lower()
hora = input("¿Qué hora del día es? (mañana, tarde, noche): ").lower()

match clima:
    case "soleado":
        if hora == "mañana":
            print("Recomendación: Jugo natural y frutas.")
        elif hora == "tarde":
            print("Recomendación: Ensalada fresca.")
        else:
            print("Recomendación: Pescado a la plancha.")
    case "lluvioso":
        if hora == "mañana":
            print("Recomendación: Chocolate caliente con pan.")
        elif hora == "tarde":
            print("Recomendación: Sopa de pollo.")
        else:
            print("Recomendación: Guiso o estofado.")
    case "frío":
        if hora == "mañana":
            print("Recomendación: Café con huevos.")
        elif hora == "tarde":
            print("Recomendación: Pasta caliente.")
        else:
            print("Recomendación: Caldo o bebida caliente.")
    case _:
        print("Clima no reconocido.")
