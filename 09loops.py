### Loops ###
"""iterar es repetir algo o un codigo
pasar por un codigo varias veces es un bucle o un ciclo
"""
#WHILE
""" 1 mientras sea verdadero hace algo
2 imprime si la condiccion se cunple infinitas veces
3 puedo detener un while haciendo que la condicion sea diferente
4 repite hasta que la condiccion no se cumpla
"""
"""
#PRUEBA DEL BUCLE INFINITO
my_prueba = 0
while my_prueba <10: #esto quema la ram
    print(my_prueba) #esto imprime 0 infinitas veces, imprime 0 por se cumple la condiccion
"""
#soluccion bucle infinito
my_prueba = 0

while my_prueba <10: #esto es como un if
    print(my_prueba)
    my_prueba += 1 #esto hace que incremente el numero y no se cumpla la condiccion
    #va hasta 9 porque 10 no es menor que 10
    """no va funcionar poque este es individual no dentro de un whileif my_prueba ==10:
    print("Mi condiccion es igual a 10")
    no lo acepta elif my_prueba == 10:
    print("Mi condiccion es igual a 10")"""
else: #esto es algo que no se tiene en muchos lenguajes, else no puede ir solo y puede ser opcional
    print("Mi condiccion es mayor o igual que 10")

print("ejecuccion continua ")#aparece cuando el bucle ya no cumple la condiccion
print(f"valor de mi conditional {my_prueba}")


while my_prueba <20:
    my_prueba +=2
    if my_prueba ==15:#esto no se cumple porque nunca va apareces el 15 con +2
        print("Mi condiccion es menor que 20")
        break #sirve para detener la ejecucion del bucle, si la condiciion se cumple 
    print(f"Mi condiccion {my_prueba} es igual a 15")

# FOR
"""
El for se usa para repetir o iterar un listado de elementos
iteracion= es poder repetir un cojunto de instrucciones, pasos o tareas varias veces 
While= sirve para hacer que un codigo se repetita varias veces en funcion de una condiccion

"""
my_list = [34, 45, 62, 52, 30, 30, 17]

for element in my_list:
    print(element) #significa que todo lo que entre se repite en la lista

my_typle = (35, 1.77, "brasil", " alo", "brandon")
#este for se ejecuta segun la cantidad 
for element in my_typle:
    print(element) # este for sirve para hacer que un codigo se repita varias veces en funcion fe una condicion
    if element == "alo":
        break #se usa para detenerlo y nos aslimos completamente de laa condiccion
#elif my_list == 1: NO SE UTILIZA CON EL FOR
   # print("Element valor 2")
else: #el else cuando se rompe el bucle no se muestra
    print("El bucle for para mi typle ha finalizado")

for element in my_direct:
    print(element)
    if element =="edad":
    continue #esto hace que la ejecucion en ese punto,se vuelva bucle con el primero
    #el continue no es buena idea porque para la ejecuccion
    print("se ejecuta")

else: 
    print("El bucle")

    