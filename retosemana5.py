
print("Hola! Este programa hará un cálculo entre dos años que tú escojas.")
print("A continuación te pediremos que introduzcas el año.")
print("NOTA: Favor de introducir los años con el formato yyyy. (Ejemplo: 2022, 2030, 2019, etc.)")


start1 = input("Hola! Introduce el año actual: ")
start2 = input("Ahora introduce otro año para calcular: ")
year1 = 0
year2 = 0
result1 = 0
result2 = 0

if start1.isnumeric() :
    year1 = int(start1)
if start2.isnumeric() :
    year2 = int(start2)
else :
    print("No son correctos los formatos del año. Intenta de nuevo.")
    exit()

if year1 > year2 :
    result1 = year1 - year2
    if result1 == 1 :
        print("Desde el año " + str(year2) + " ha pasado un año")
    else :
        print("Han pasado " + str(result1) + " años desde el año que has introducido.")

elif year1 < year2 :
    result2 = year2 - year1
    if result2 == 1 :
        print("Para llegar a " + str(year1)+ " hace falta un año")
    else :
        print("Faltan " + str(result2) + " años para llegar al año que has introducido.")

elif year1 == year2 :
    print("Has introducido el mismo año que el actual")
    