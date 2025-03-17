'''
Estrucutura de control if:
se utiliza para tomar decisiones 
basadas en expresiones condicionales
'''
#Ejemplo 1: IF SIMPLE
edad = int (input("ingresa tu edad:"))
documento = (input("tienes documento?(si/no);"))
#condicional: si la edad es mayor o igual a 18
if edad >= 18 and documento=='si':
    #codigo para vuando es mayor a 18
    print("Eres mayor de edad y tienes documento, puedes votar") 
else:
    #codigo para cuando no es menor de edad o no tienes documento 
    print("Eres menor de edad o no tienes documento, no puedes votar ")
#codigo que se ejecuta siempre
print ("fin del programa")

