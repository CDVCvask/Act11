def Menu():
    print("Bienvenido a ordenar el menu")
    print("1.Ingresar estudiantes: ")
    print("2.Mostrar lista desordenada")
    print("3.Mostrar lista ordenada")
    print("4.Salir")
def Q_S(Students):
    if len(Students) <= 1:
        return Students
    else:

allow = False
students = []
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            number = int(input("Ingrese la cantidad de alumnos que desea ingresar: "))
            for i in range(number):
                name = input("Ingrese el nombre del alumno")
                students.append(name)
        case 2:
            print(students)
        case 3:
            print("Mostrar")
        case 4:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")