#si algo se cumple  lo ejecuta si no pues no

""" con el if= true se ejecuta si es falso no se ejcuta
my_condition = False

if my_condition: #if my condition = true y la variable esta en true es redundante
    print("Esta condicion es un if")

print(" aqui condinua la ejecucion|")

# solo imprime esto aqui condinua la ejecucion|

"""  

"""las condiccionales tienen una jerarquia, los elif si se cumple uno ya no mira
las otras con el if si mira las otras
si en elif se pone la condiccion ==1 es igual a elif my_condition pero esta se necesita
poner la condiccion"""

my_condition = 5*2
if my_condition ==11 :
    print("Se ejecuta la condiccion del segundo if")

#if my_condition >10  : una condiccion, necesita una condiccion
if my_condition>10 and my_condition <20:
    print("es menor que 10 y mayor que 20")
    #para que no se cumpla la condiccion

elif my_condition == 1: #este necesita una condiccion esto es igual a elif my_condition pero esta mal
    print("Es  igual que 1") #dentro

else: #es la que se ejcuta si no se cumple nada
    print("Es menor o igual que 10") #dentro
    print("Es menor o igual que 10") #dentro
print("Esta afuera del else")#fuera del else porque ya no esta tabulado

print(" aqui condinua la ejecucion|")

#con un string vacion nos da un false
my_string ="cadena"
'''esto es lo mismo if my_string =="cadena, 
    pero esto es diferente if my_string =="cadena texto'''
if my_string: 
    print("Mi cadena")

my_string = ""
#si pongo el not, ahora no lo imprime porque lo vuelve vacia, no vacio es vacio
if not my_string: 
    print("Mi cadena es vacia")


"""
CONDICIONALES
IF 
ELIF
ELSE
"""
