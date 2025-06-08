

def quitar_ingrediente(mi_pizza):
    ingredientes = mi_pizza["ingredientes"]
    print("la opción para quitar son estas:")

    for i in ingredientes:
        print(f"1 {i}")   

    opcion = int(input(": "))
    ingrediente = ingredientes[opcion]
    mi_pizza["ingredientes"].remove(ingrediente)