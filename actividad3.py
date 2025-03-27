'''
Actividad 3 :
Escribir un programa
que calcule el salario neto 
de un trabbajador 
despues de descuentos 
y bonificaciones 

=> INICIALMETE, el programa 
debe solicitar un tipo de 
trabajador entre los siguientes:
a - contrato a termino indefinido
b - contrato por prestacion de servicios
c - contrato de aprendizaje 
d - jornal
=> jornal:
    se debe solicitar:
    - el tipo de unidad a pagar 
    - el numero de uniades hechas 
    - el valor de la unidad
    el salario neto se calcula como 
    el valor_unidad  *numero_unidades
    si el numero de unidades es mayor a 100
    se le da una bonificacion de el 10%
    => contrato de aprendizaje
    el salario neto es
    
    
    => contrato por prestacion de servicios:
    se debe solicitar:
    -el valor del contrato
    -el numero de meses trabajados
    -antiguedad en la empresa
    se calcula dividiendo el valor del contrato
    entre el numero de meses trabajados
    bonificaciones por antigueda:
    -si la antiguedad es menos a 2 años
    se le aumenta el 2% al salario mensual
    -si la antiguedad esta entre 2 y 5 años 
    se le aumenta el 5% al salario mensual
    -si la antiguedad es mayor a 5 años
    se le aumenta el 10% al salario mensual
    Descuentos de ley
    -8% de salud 
    -10% de pension 
    -1% de caja de compensacion 
    => contratro a termino indefinido
    el salario mensual se calcula 
    con base en la siguiente tabla:
    de escalafones o grados:
    - 1: 1.5 veces el SMLV
    - 2: 1.7 veces el SMLV
    - 3: 2 veces el SMLV
    - 4: 2.5 veces el SMLV 
    - 5: 3 veces el SMLV 
    el programa debe solicitar 
    el grado o escalafon
    del empleado
    -las bonificaciones y 
    descuentos de ley son las mismas 
    que en el caso b 
    
'''
#variable global:
#variable que puede ser rconocida
#y asignada en cualquier parte del
#programa
#NOTA: se recomienda inicializar 
#definir y dar valor inicial a las 
#variables globales al principio
#del programa 
#Ejemplo de esto son las variables
#para almacenar resultados finales 


salario_neto = 0

tipo_empleado = input ("Ingrese el tipo de empleado (a/b/c/d): ")
if tipo_empleado == "a":
    print("ha ingresado a termino indefinido")
    SMLV = int (input("ingrese SMLV:"))
    escalafon = int(input("ingrese el escalafon:"))
    antiguedad = int(input("ingrese la amtiguedad de la empresa:"))
    if escalafon == 1:
        salario_mensual = 1.5 * SMLV
    elif escalafon ==2:
        salario_mensual = 1.7 * SMLV
    elif escalafon ==3:
        salario_mensual = 2 * SMLV
    elif escalafon ==4:
        salario_mensual = 2.5 * SMLV
    elif escalafon ==5:
        salario_mensual = 3 * SMLV
    salario_neto = salario_mensual
    bonificacion = 0
    if antiguedad < 2:
            bonificacion = salario_mensual *0.02
    elif antiguedad >= 2 and antiguedad <= 5:
            bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
            bonificacion = salario_mensual * 0.10
    salario_mensual += bonificacion
        #refactorizacion
    salario_mensual = salario_mensual + bonificacion
        #descuentos 
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja= salario_mensual * 0.01
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion 
    
    
elif tipo_empleado == "b":
        print("ha ingresado prestacion de servicios")
        valor_contrato = int(input("ingrese el valor del contrato:"))
        numero_meses = int (input("ingrese el numero de meses trabajados:"))
        antiguedad = int(input("ingrese la amtiguedad de la empresa:"))
        salario_mensual = valor_contrato / numero_meses
        #bonificaciones: elif anidados
        bonificacion = 0
        if antiguedad < 2:
            bonificacion = salario_mensual *0.02
        elif antiguedad >= 2 and antiguedad <= 5:
            bonificacion = salario_mensual * 0.05
        elif antiguedad > 5:
            bonificacion = salario_mensual * 0.10
        salario_mensual += bonificacion
        #refactorizacion
        salario_mensual = salario_mensual + bonificacion
        #descuentos 
        descuento_salud = salario_mensual * 0.08
        descuento_pension = salario_mensual * 0.10
        descuento_caja= salario_mensual * 0.01
        salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion 
        
        
elif tipo_empleado == "c":
        print("ha ingresado contrato de aprendizaje")
        salario_minimo= int(input("ingrese salario minimo:"))
        descuento = salario_minimo * 0.25
        salario_neto = salario_minimo - descuento
        
        
        
elif tipo_empleado == "d":
        print("ha ingresado jornal")
        #variables locales 
        #variables que solo pueden ser 
        #reconocidas y asignadas en un bloque 
        #de codigo especifico
        tipo_unidad = input ("ingrese el tipo de unidades:")
        numero_unidades = int (input("ingrese el numero de" + tipo_unidad +"hechas:"))
        valor_unidad = int (input("ingrese el valor de "+ tipo_unidad))
        salario_neto= numero_unidades * valor_unidad
        
else:
    print("Tipo de empleado invalido")
    #mostrar salario neto 
print("salario neto  es: ", salario_neto)
print("fin del programa")

        