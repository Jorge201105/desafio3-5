

def elegir_salsa(mi_pizza):
    salsa = ["1","2","3","4"]
    opcion = input("""

Selecciona la salsa:
1.- Salsa Tomata
2.- Salsa Alfredo
3.- Salsa Barbecue
4.- Salsa Pesto                   
                   
""")
    
    if opcion == salsa[0]:
        mi_pizza["salsa"] = "Salsa_Tomate"
        print(f"base de {mi_pizza["salsa"]} agregada correctamente  ")

    elif opcion == salsa[1]:
        mi_pizza["salsa"] = "Salsa_Alfredo"

    elif opcion == salsa[2]:
        mi_pizza["salsa"] = "Salsa_Barbecue"
    
    elif opcion == salsa[3]:
        mi_pizza["salsa"] = "Salsa_Pesto"

    else:
        print("opcion no valida")

    return mi_pizza
    