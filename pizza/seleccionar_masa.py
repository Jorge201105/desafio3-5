


def seleccionar_masa(mi_pizza):
    masa = ["1","2", "3"]
    eleccion =input("""
selecciona la masa:
1.- Masa Traducional
2.- Masa Delgada
3.- Masa Borde queso
""")
    
    
    if eleccion == masa[0]:
        mi_pizza["masa"] = "masa_tradicional"
        print(f"masa de {mi_pizza["masa"]} agregada correctamente")

    elif eleccion == masa[1]:
        mi_pizza["masa"] ="masa_delgada"
        print(f"masa de {mi_pizza["masa"]} agregada correctamente")

    elif eleccion == masa[2]:
        mi_pizza["masa"] ="masa_borde_queso"
        print(f"masa de {mi_pizza["masa"]} agregada correctamente")

    else:
        print("opción no valida")

    return mi_pizza
          


    