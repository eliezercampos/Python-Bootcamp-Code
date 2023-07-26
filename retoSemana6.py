print("Hola! Vamos a crear una contraseña y vamos a confirmarla.")
print("Una de las premisas será que tiene que iniciar con un número.")


password1 = input("Empecemos! Introduce una contraseña por favor: ")

for i in password1 :
    if i.isdigit() :
        password2 = input("Por favor, escribe nuevamente la contraseña: ")
        while password1 != password2 :
            print("Las contraseñas no coinciden.")
            password2 = input("Por favor, escribe nuevamente la contraseña: ")
        else : 
            if password1 == password2 :
                print("Contraseña correcta y confirmada")
            break
    
    else :
            print("La contraseña debe empezar con un número")
            break