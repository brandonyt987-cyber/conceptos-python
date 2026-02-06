#operadores Aritmeticos

#operaciones como sumas, restas, multiplicacion

#type es un indicador de el tipo de dato que usamos
#input = pide datos por teclado


##print(input("ingresa un numero:"))

print(2+4)
print(3-2)
print(3*4)
print(3/4) #division

#modulo, es establecer una operacion y ver el resto o los mmultiplos
print(10% 2)

#flor divition, es una aproximacion a un numero entero aunque la division no de entero
print(50//3)

#calcular un exponente
print(2**3)

#letras o palabras
#los signos operan
print("ola " + "mama")
#print("ola" - "sed") nos da un error o con los otros da error
print("mango " + str(5)) #funciona porque str lo hacer un tipo string

print("te " * (2**3))

#un float a un entero
my_float = 2.5 * 2
# aqui nos da 5.0 y esto es un float
print("hola" * int(my_float))
# int(my_float) esto hace que el 5.0 sea un 5 y ya no de error


#operadores comparativos
"solo sirve para decir si algo es true o flase"

print( 3 > 4 ) #3 mayor que 4
print( 3 < 4 ) #3 menor que 4
print( 3 <= 4 )#menor igual < + = 
print( 2 >= 2 )#mayor igual > + =
print( 2 == 2 )#igualdad son = + = ==
print( 2 != 6 )# distinto !+= !=

#Aqui cuenta en dorden alfavetico y no cuenta los caracteres

print( "hola" > "phython")
print( "hola" < "python" )
print( "hola " >= "python")
print( "hola" <= "zola" ) # aqui nos comprueba una ordenacion alfavetica 
print( "hola" == "hola")
print( "hola" != "python")

print( "aaa" >= "aba") #esto nos da false proque comprar cuenta en ordenacion alfavetica

#contrar caracteres
#se usa len para la logitud de una cadena de texto

print(len("hola") > len("hola")) #nos da true porque cuenta el numero de letras
print( "AAA" < "aaa")#las mayusculas influyen 
print ("AAA" > "aaa")#esto tambein influye

#operadores de logica
"""
Esto es logica boleana flase y false nos da false 
true y false nos da false
"""

print( 3 > 4 and "hola" > "python") #false y false
print( 3 > 4 or "hola" > "python") #false y false
print( 3 < 4 and "hola" < "python")#true y true es verdadero
print( 3 < 4 or "hola" < "python") #true o true es verdadero
print( 3 > 4 or "hola" > "python") #true y false false

#como hacer antees algo y ya despues lo otro, primero se agrupa con parenticis
print( 3 > 4 or ("hola" > "python" and 4 == 4))
print( 3 > 4 or "hola" < "python")

#not se usa para decir o para negaar todo la condicion
#la condicion es 3 mayor 4 falso entonces el not eso lo niega y es true
print(not( 3 > 4))












