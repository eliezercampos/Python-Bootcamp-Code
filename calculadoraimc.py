print()
print()
print("Bienvenido a la Calculadora IMC")
print("Esta calculadora te permitira obtener tu Indice de Masa Corporal")
print("Vamos a necesitar unos datos para poder darte tu IMC")
print()

# Solicitud de nombre y apellidos

print()
print("Introduce tu nombre")
nombre = input()
print("Hola", nombre,"!")
print()
print("Ahora, necesitaremos tu apellido paterno")
apellido_paterno = input()
print()
print("Para finalizar, necesitaremos tu apellido materno")
apellido_materno = input()
print("Muchas gracias!")
while True:
    print("Como datos de referencia, pedimos tu edad en años")
    edad = input()
    try:
        edad = int(edad)
    except ValueError:
        print("Favor de introducir solo numeros.")
        continue
    else:
        break

# Empezamos con el proceso de solicitud de datos para calculo de IMC


print("Es momento de solicitar tus datos para calcular tu IMC")
print()
print("Primero solicitamos tu peso en kgs:")
while True:
    peso = input()
    try:
        peso = float(peso)
    except ValueError:
        print("Favor de introducir solo numeros.")
        continue
    else:
        peso = float(peso)
        break
print("Por favor, escribe tu estatura en metros.")
print("Ejemplo, si mide 153 cms, favor de poner 1.53")
while True:
    alt = input()
    try:
        alt = float(alt)
    except ValueError:
        print("Favor de introducir numeros con punto decimal.")
    else:
        alt = float(alt)
        break

# Se hace aquí la operacion para obtener el resultado del IMC

print()
print("Procedemos al calculo de tu IMC", nombre)
print("Este calculo se realiza tomando tu peso y dividiendo el mismo entre la estatura al cuadrado")
imc = peso / alt**2
print(nombre, "de acuerdo a los datos proporcionados tu IMC es:", imc)
print()
print("A continuación encontrarás tus datos completos:")
print()
print("Nombre completo del usuario: ", nombre, apellido_paterno, apellido_materno)
print()
print("Edad del usuario: ", edad)
print()
print("Peso del usuario: ", peso)
print()
print("Estatura del usuario: ", alt)
print()
print("IMC del usuario: ", imc)
print()
print("Gracias por usar esta calculadora de IMC", nombre,"!")
print()
print("¡Que tengas un excelente día!")
print("Presiona cualquier tecla para salir")
input()
