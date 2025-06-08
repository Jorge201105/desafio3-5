

def agregar_ingrediente(mi_pizza):
    ingredientes = {
        1:"Tomate",
        2: "Champiñones",
        3: "Aceitunas",
        4: "Cebolla",
        5: "Pollo",
        6: "Jamon",
        7: "Carne",
        8: "Tocino",
        9: "Queso"
    }
    print("las opciones son las siguientes: ")

    for k,v in ingredientes.items():
        print(f"{k}.-{v}")

    opcion = int(input(" : "))
    
    if opcion in ingredientes:
        ingrediente = ingredientes[opcion]
        mi_pizza["ingredientes"].append(ingrediente)
        print(ingredientes)