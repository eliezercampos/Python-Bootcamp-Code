print("Este programa permitirá contar las letras de una palabra y ver si cumple con el criterio.")
print("Deberás escribir una palabra con un rango de 4 a 8 caracteres.")

# Se declaran variables máximas de la palabra (Mayor a 4 y menor a 8)
num1 = 4
num2 = 8

# Se solicita la palabra al usuario
palabra = input("Por favor escribe la palabra que quieras: ")

# Se realiza la comparación de la palabra vs los criterios
# Si la palabra es mayor o igual a 4 (Variable num1) y si la palabra es menor o igual a 8 (Variable num2), imprime mensaje correcto
if len(palabra) >= num1 and len(palabra) <= num2 :
    print("La longitud de palabra es correcta")
    
#Se usa elif para comparar si la palabra es menor a 4 y contar las letras que faltan
elif len(palabra) < num1 :
    resta = int(num1) - len(palabra)
    print("Te hacen falta ", resta, "letras.")

elif palabra > str(num2) :
    sobra = len(palabra) - int(num2)
    print("Te sobran", sobra, "letras.")

else :
    print("")