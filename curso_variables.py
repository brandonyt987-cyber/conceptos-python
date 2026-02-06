#variables

"""
un programa almacena datos y empieza a trabajar con ellos 
en python las variables se ponen solo el texto y en minuscula
para definir una variable
camel caes = la primera letra en minuscula y en unanueva palabra minuscula
"""

frist= "brandon"
second= 2
my_float_variable= 1.4

print(frist)
print(my_float_variable)

print(type(second))

print("hpla mundo soy",(frist))

#funciones

Fouth= "variabe"

#concatenacino de cadenas

"""
proceso de unir dos o más cadenas de caracteres (strings),
variables o constantes para formar una sola cadena más larga
"""
print(frist, second, my_float_variable,Fouth)

#funciones del sistema
#cuenta cunatos caracteres hay

print(len(frist))

print("esto vale:",my_float_variable)

#variables en una sola linea
#asi se pueden crear varibales seguidas, no es bueno hacerlo muy seguido
name, surname, age =" David", "osorno", 18

print("tengo:",age,"anos mi segundo nombre es:", name, "y mi apellido es", surname)

#teclado en consola
'''
frist_name = input("what's coming up?")
age= input("how older you?")

print(frist_name)
print(age)
'''

#cambio su tipo
#se arreasigna el valor de la variable como aqui, python no es tipado fuerte

name= 34
age= "david"
print(name)
print(age)

# FORZAR EL TIPO
"""
De esta forna podemos, podemos ayudarnos a entender lo que queremos que sea un string
aqui se configura el id para indicar un error
str = significa string
"Oye Python (y al programador), esta variable debería ser un string."
"""

mango: str ="fruta"
mango= 4
print(mango)
