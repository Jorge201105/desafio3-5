
from pizza.menu import menu 
from pizza.crear_pizza import crear_pizza
from pizza.seleccionar_masa import seleccionar_masa
from pizza.quitar_ingrediente import quitar_ingrediente
from pizza.elegir_salsa import elegir_salsa
from pizza.agregar_ingrediente import agregar_ingrediente
from pizza.elegir_salsa import elegir_salsa
from pizza.tiempo_preparacion import tiempo_preparacion
from pizza.confirmar_pedido import confirmacion

def main():
    mi_pizza=crear_pizza()

    while True:
        menu()
        opcion = input("ingrese su opción : ")
       
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

        elif opcion == "6":
           t = tiempo_preparacion(mi_pizza)
           print(f"El tiempo que demorará la pizza son {t} minutos ")

        elif opcion == "7":
           print(confirmacion())



        else:
            print("salir")
            exit()



if __name__ == "__main__":
    main()
        
