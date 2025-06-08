

def confirmacion():
    c = input("Escriba 1 si efectuará su pedido  \n escriba 2 para cancelar su pedido \n  : ")
    if c == "1":
        return "gracias por realizar su pedido con nosotros"
    
    elif c=="2":
        return "lamentamos que no realece su pedido con nosotros lo esperamos para la próxima"
    
    else:
        return " Sólo puedes elegir entre 1 y 2"
            
          
    