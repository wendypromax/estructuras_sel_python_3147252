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

#ejemplo 6: operadores aritmeticos, 
#relacionales y logicos
y = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2
print("el resultado de operar con aritmeticos, relacionales y logicos es",y)

#ejemplo 7: con parentesis
y = (3 + 5 != 2*3 and 4==4 or not 3 < 2)
print("el resultado de operar con parentesis es",y)

#Ejemplo 8: todo junto 
y = 4**2 * 3 < 6 / (7 -5) and 7 * 2 + 1 == 14 or not 3 + 5 < 2
print("el resultado de operar todo junto es",y)