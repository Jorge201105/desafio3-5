
from pizza.menu import menu 
from pizza.crear_pizza import crear_pizza
from pizza.seleccionar_masa import seleccionar_masa
from pizza.quitar_ingrediente import quitar_ingrediente
from pizza.elegir_salsa import elegir_salsa
from pizza.agregar_ingrediente import agregar_ingrediente
from pizza.elegir_salsa import elegir_salsa



def main():
    mi_pizza=crear_pizza()

    while True:
        menu()
        opcion = input("ingrese su opción")
       
        if opcion =="1":
            seleccionar_masa(mi_pizza)
            print(mi_pizza)

        elif opcion == "2":
            elegir_salsa(mi_pizza)
            print(mi_pizza)
        
        elif opcion == "3":
            agregar_ingrediente(mi_pizza)
            print(mi_pizza)


        elif opcion == "4":
            quitar_ingrediente(mi_pizza)
            print(mi_pizza)

        elif opcion == "5":
            print(mi_pizza)

        else:
            print("salir")



if __name__ == "__main__":
    main()
        
