numHuevos = 12

# print("Tengo" + numHuevos + " huevos.")

#Opcion 1
print("Tengo " + str(numHuevos) + " huevos.")

#Opcion 2 
print("Tengo %s huevos." %numHuevos)


#Calcular la superficie o area de un cuadrado

lado = int(input("Ingrese la medida del lado del cuadrado: "))
superficie = lado * lado
print("La superficie del cuadrado es: " + str(superficie))

# Ejercicio

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
correo = input("Introduce tu correo: ")
telefono = input("Introduce tu telefono: ")

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Tengo " + str(edad) + " años")
print("correo: " + correo)
print("Telefono: " + telefono)