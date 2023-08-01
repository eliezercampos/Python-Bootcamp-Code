print("Este programa te ayudará a validar el cuadrante de unas coordenadas dadas.")
print("A continuación te pediremos dos números.")

# Se solicitan los datos de las coordenadas y se declaran las variables
x = input("Introduce la primer coordenada: ")
y = input("Introduce la segunda coordenada: ")

# Se empieza la validación de las variables para la asiganación de los cuadrantes
# Este primer if valida si el valor de las coordenadas es 0, en caso de ser TRUE, imprime el resultado
if int(x) == 0 and int(y) == 0 :
    print("El punto que buscas es el Origen.")

# Este elif se usa para validar que los valores de las coordenadas son mayores a cero.
elif int(x) > 0 and int(y) > 0 :
    print("El punto que buscas está en el Cuadrante I. Ambos puntos, en los ejes X y Y, fueron positivos.")

# Este elif se usa para validar que el valor de X es menor que 0 y el valor de Y mayor a 0.
elif int(x) < 0 and int(y) > 0 :
    print("El punto que buscas está en el Cuadrante II. El punto en el eje X es negativo y el punto en el eje Y es positivo.")

# Este elif se usa para validar que los valores de las coordenadas son menores a cero.
elif int(x) < 0 and int(y) < 0 :
    print("El punto que buscas está en el Cuadrante III. Ambos puntos, en los ejes X y Y, fueron negativos.")

# Este elif se usa para validar que el valor de X sea mayor a 0 y el valor de Y menor a 0.
elif int(x) > 0 and int(y) < 0 :
    print("El punto que buscas está en el Cuadrante IV. El punto en el eje X es positivo y el punto en el eje Y es negativo.")

else :
    print("")