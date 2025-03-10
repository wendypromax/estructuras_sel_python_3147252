'''

operadores lógicos 

aquellos que operan unicamente 
con valores booleanos (V F)

Acorde a las tablas de verdad

'''


#Ejemplo 1: operador not:
y = not True
print("el resultado de operar com not es", y)


#ejemplo 2: operador and
y = True and True
print("el resultado de operar con and es", y)

#Ejemplo 3: operador or
y = True or False
print("el resultado de operar con or es", y)

'''
jerarquia de presedencia de operadores 
(logicos inclusive)
1.         ()
2.         **
3.      *, /, %
4.         +, -
5.         >, <, >=, <=, !=, ==
6.         not 
7.         and
8.         or 
9.         =

'''
#Ejemplo 4: jerarquia de operadores 
y = False and not True or False 
print("el resultado de operar con jerarquia es",y)

#ejemplo 5: operadores relacionales y logicoa 
y = not 3 > 4 and 4 == 4 or 3 < 2
print("el resultado de operar con relacionales y logicos es", y)
