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
estado_civil = input("ingresa tu estado civil:(soltero/casado/comprometido)" )
edad = int(input("ingresa tu edad:"))
temperamento = input("ingresa tu temperamento:(buena persona/mala persona)")
fisico = input("ingresa tu fisico:(lindo/a/feo/a)")
salario= floatestado_civil = input("Ingrese su estado civil (soltero/casado/comprometido): ").lower()
edad = int(input("Ingrese su edad: "))
temperamento = input("Ingrese su temperamento (buena persona/mala persona): ").lower()
fisico = input("Ingrese su físico (lindo/a/feo/a): ").lower()
salario = float(input("Ingrese su salario: "))

if estado_civil in ["casado", "comprometido"]:
    print("No puede acercarse a esta persona, porque ya tiene compromiso.")
elif edad < 18:
    print("No puede acercarse a esa persona, porque no tiene la edad suficiente.")
elif temperamento == "mala persona":
    print("No puede acercarse a esta persona, porque te genera stress.")
elif fisico in ["feo", "fea"]:
    print("No puede casarte con esa persona, porque no te atrae físicamente.")
elif salario < 200000:
    print("No puede casarte con esa persona, porque no tiene suficiente dinero.")
else:
    print("Puede casarte con esa persona.")

print("Fin del programa.")(input("ingresa tu salario:"))

if estado_civil == "casado" or estado_civil == "comprometido":
    print("no puedes acercarte a esta persona, porque ya tiene compromiso")
elif edad < 18:
    print("no puedes acercarte a esa persona, porque no tiene la edad suficiente")
elif temperamento == "mala persona":
    print("no puedes acercarte a esta persona, porque te genera stress")
elif fisico == "feo":
        print("no puedes casarte con esa persona, porque no te atrae fisicamente")
elif salario > 200.000 :
        print("no puedes casarte con esa persona, porque no tiene suficiente dinero")

else:
    print("puedes casarte con esa persona")
print("fin del pograma")