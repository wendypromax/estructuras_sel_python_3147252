'''
if aninadados
son estructuras selectivas
que se encuentran dentro 
de otro if 
sintax:
if condicion: 
    if condicion: 
        if condicion 
            bloque de instr
    else:
    if condicion
bloque de instr
    else: 
    bloque de instr
    
else: bloque de instruciones

'''
# Ejemplo 1:
# modificacion del ejercicio de votacion,
# ahora solo puede votar si es mayor de edad
# pero si tiene documento.
# mostrar explicaciones em los otros casos 
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    documento = input("tiene documento? (si/no)")
    if documento == "si":
        print("usted puede votar")
    else:
        print("usted no puede votar")
        print("porque no tiene documento")
else:
    print("usted no puede votar")
    print("porque es menor de edad")
    
    