'''
if en cascada:
estructura de contol que permite 
evaluar varias condicones en 
cascada, es decir, si la primera 
condicion no se cumple, 
se evalua la siguiente
y asi sucesivamente.

'''
#Ejemplo 1:
#Modificar el programa dde votacion 
#para que considera la edad de 17 
#años
edad  = int (input("ingresa tu edad:")) 
if edad > 18:
    print("puedes votar")
elif edad == 18:
    print("bienvenidos ciudadanos, puedes votar con contraseña ")
elif edad == 17:
    print("bienvenidos ciudadanos, puedes votar con contraseña ")
elif edad >= 10:
    print("eres muy peque, tienes registro civil")
elif edad < 17:
    print("tienes tarjeta de identidad,no puedes votar aun")

print ("fin del programa ")

