###st5rings

my = "primera"
other = 'ola como es la gamineria'

#longitud
'''es la longitud del contenido de la variable'''

print(len(my))
print(len(other))

#concatenar 

print(my + " linea y dice " + other)

#caracteres
'''salto de linea es \n y se pone pegado el texto a la n'''
newstring = 'este es un string \ncon salto de linea'
print(newstring)

#tabulaciones \7
"""
. En print(mytab), mytab es una variable string que contiene
el carácter de tabulación, el cual, al imprimirse, genera un
espacio en blanco similar a pulsar la tecla Tab. 
"""
mytab= "\teste es un string o tabulacion"
print(mytab)

#escapar string
#esto permite combinar las dos funciones
myscape = "\teste se escapa \nescapado"
print(myscape)

#como no hacerle caso 
mypool = "\\teste no hace el tab \\nni para escapar"
print(mypool)

#formateo

name, surname, age= "brandon", "osorno", 18
#%s esto hace que el primer texrto que yo le pase despues de %s lo pone 
#%d para un entero
#%s para un string

#pasos para que aparesca
#para que sepa a quines llamar se usa el .format y se ponen y se usa las  
# {} para que aparesca el texto, esto sirve para cuando tengamos idiomas 

print("mis datos son {} {} y mi edada es {}" .format(name, surname, age) )

#% se pone de a uno por uno
print("mis datos son %s %s y mi edada es %d" %(name,  surname, age) )

print( "mis datos son" + name + " " + surname + " y mi edad es " + str(age))#esto no es tan bueno y toca pasar la edad a un str


#formateo cadena de texto o inferencia de datos
print(f"mi nombre es {name} {surname} y mi edad es {age}") #esta es muy util

#desempaquetado de caracteres

#esto se iguala a y b a python y a, b valen lo mismo
language = "python"

'''esto da error porque la plabra python tiene 6 caractes
y solo le estamps dando 2 "a, b = language" '''      
a, b, c, d, e, f= language
print(a)
print(e) 

#DIVISION

""" 1 y 3 son letras de la palabra python y paython se cuenta desde 0, 1, 2, 3, 4, 5
si yo hago esto language_slice = language[3:] pone las letras que van despues del 3
con esto  sirve [-2] y empieza desde -1 porque no existe -0"""

language_slice = language[1:3]
print(language_slice)

language_slice = language[3:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#REVERSE
"""esto es para que le de la vuelta a las palabras"""
reversed_lang = language[::-1]
print(reversed_lang)


#funciones
"""
len contrar caracteres o poner un . para ver las funciones"""

print(language.capitalize()) #pone la letra en mayuscula
print(language.upper()) #pone todo en mayuscula
print(language.count("o")) #sirve para contar cuantas letras especificas tiene
print(language.isnumeric()) #pregunta si la variable es un numero 
print("34".isnumeric())#aqui si aparece true
print(language.lower()) #todas minusculas
print(language.upper().isupper()) #primero se pne todas en mayusculas y se comprueva con issupper
print(language.lower().isupper()) #todas minusculas y despues lo comprueba)
print(language.startswith("py"))#pregunta por que comienza, tener cuidado con las letras mayusculas y minusculas
