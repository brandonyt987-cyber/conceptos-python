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
    print(f"Mi condiccion {my_prueba} es igual a 15")
