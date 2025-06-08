
from pizza.menu import menu 
from pizza.crear_pizza import crear_pizza
from pizza.seleccionar_masa import seleccionar_masa




def main():
    pizza=crear_pizza()

    while True:
        menu()
        opcion = input("ingrese su opción")
       
        if opcion =="1":
            seleccionar_masa()
            pass

        elif opcion == "2":
            print("2")
        
        elif opcion == "3":
            print("3")

        elif opcion == "4":
            print("4")

        elif opcion == "5":
            print("5")

        else:
            print("salir")



if __name__ == "__main__":
    main()
        
