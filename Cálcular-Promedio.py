# Programa para calcular el promedio de un estudiante

act1 = float(input("Ingrese calificación para Actividad 1: "))
if 100 >= act1 and act1 >= 0:
    act1 = act1 * .08
    ex1 = float(input("Ingrese calificación para Examen 1: "))
    if 100 >= ex1 and ex1 >= 0:
        ex1 = ex1 * .15
        act2 = float(input("Ingrese calificación para Actividad 2: "))
        if 100 >= act2 and act2 >= 0:
            act2 = act2 * .08
            ex2 = float(input("Ingrese calificación para Examen 2: "))
            if 100 >= ex2 and ex2 >= 0:
                ex2 = ex2 * .15
                act3 = float(input("Ingrese calificación para Actividad 3: "))
                if 100 >= act3 and act3 >= 0:
                    act3 = act3 * .09
                    ex3 = float(input("Ingrese calificación para Examen 3: "))
                    if 100 >= ex3 and ex3 >= 0:
                        ex3 = ex3 * .20
                        tf = float(input("Ingrese calificación para Trabajo Final: "))
                        if 100 >= tf and tf >= 0:
                            tf = tf * .25
                        else:
                            print("try again")
                    else:
                        print("try again")
                else:
                    print("try again")
            else:
                print("try again")
        else:
            print("try again")
    else:
        print("try again")
    prom = act1 + ex1 + act2 + ex2 + act3 + ex3 + tf
    if 100 >= prom and prom >= 0:
        if prom == 100: 
            print("felicidades sacaste 100")
        else:
            print(prom)
    else:
        print("try again")
    print("Gracias por utilizar el programa")
    print("Realizado por Mariel G.")
    print("stan loona")
else:
    print("try again")
input()