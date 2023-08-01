print("Este programa te ayudará a validar el cuadrante de unas coordenadas dadas.")
print("A continuación te pediremos dos números.")

# Se solicitan los datos de las coordenadas y se declaran las variables
x = input("Introduce la primer coordenada: ")
y = input("Introduce la segunda coordenada: ")

# Se empieza la validación de las variables para la asiganación de los cuadrantes
if int(x) == 0 and int(y) == 0 :
    print("El punto que buscas es el Origen.")

elif int(x) > 0 and int(y) > 0 :
    print("El punto que buscas está en el Cuadrante I. Ambos puntos, en los ejes X y Y, fueron positivos.")

elif int(x) < 0 and int(y) > 0 :
    print("El punto que buscas está en el Cuadrante II. El punto en el eje X es negativo y el punto en el eje Y es positivo.")

elif int(x) < 0 and int(y) < 0 :
    print("El punto que buscas está en el Cuadrante III. Ambos puntos, en los ejes X y Y, fueron negativos.")

elif int(x) > 0 and int(y) < 0 :
    print("El punto que buscas está en el Cuadrante IV. El punto en el eje X es positivo y el punto en el eje Y es negativo.")

else :
    print("")