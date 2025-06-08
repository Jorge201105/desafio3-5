

def quitar_ingrediente(mi_pizza):
    ingredientes = mi_pizza["ingredientes"]

    if not ingredientes:
        print("No hay frutas que quitar")
        return
    
    print("la opción para quitar son estas:")

    for i,ingrediente in enumerate(ingredientes):
        print(f"{i} . {ingrediente}")   

    opcion = int(input(": "))
    ingrediente = ingredientes[opcion]
    mi_pizza["ingredientes"].remove(ingrediente)