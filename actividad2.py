# Descripcion: Actividad 2
'''
Elabore un programa en python 
que determine si usted puede:
a) casarse
b) comprometerse
c) QUEDARSE SOLTERO
con base en las siguientes 
caracteristicas(variables)
-estado civil(string=
        "soltero", "casado", "comprometido")
-edad (int)
-temperamento(string =
        "mal geniado/a", "contento/a", "serio/a)
-fisico(string = "lindo/a", "feo/a")


'''
stado_civil = input("ingresa tu estado civil:(soltero/casado/comprometido)" )
edad = int(input("ingresa tu edad:"))
temperamento = input("ingresa tu temperamento:(buena persona/mala persona)")
fisico = input("ingresa tu fisico:(lindo/a/feo/a)")
salario= float (input("Ingresa tu salario: "))


if estado_civil == "casado" or estado_civil == "comprometido":
    print("no puedes acercarte a esta persona, porque ya tiene compromiso")
elif edad < 18:
    print("no puedes acercarte a esa persona, porque no tiene la edad suficiente")
elif temperamento == "mala persona":
    print("no puedes acercarte a esta persona, porque te genera stress")
elif fisico == "feo":
        print("no puedes casarte con esa persona, porque no te atrae fisicamente")
elif salario < 200.000 :
        print("no puedes casarte con esa persona, porque no tiene suficiente dinero")

else:
    print("puedes casarte con esa persona")
print("fin del pograma")
