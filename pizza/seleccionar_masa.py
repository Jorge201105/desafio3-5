


def seleccionar_masa(pizza):
    masa = ["masa_tradicional","masa_delgada", "masa_borde_queso"]
    eleccion =input("""
selecciona la masa:
1.- Masa Traducional
2.- Masa Delgada
3.- Masa Borde queso
""")
    test = masa[0]
    print(masa,eleccion,test)
    if eleccion == masa[0]:
        pizza["masa"] = "masa_tradicional"
        print(f"masa de {pizza} ")

    elif eleccion == masa[1]:
        pizza["masa"] ="masa_delgada"
        
          


    