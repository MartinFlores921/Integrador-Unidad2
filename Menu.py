#from ManejadorAlumno import ManejadorAlumno
#from ManejadorMaterias import ManenejadorMateria


def menu(MA, MM):
    print('1 - Informar promedio con aplazos y sin aplazos de un alumno')
    print('2 - Informar los alumnos que promocionaron en una materia')
    print('3 - Obtener listado de alumnos ordenado por año que cursan y alfabeticamente')
    print('4 - Salir del programa')
    op = int(input('Ingrese opcion:'))
    while op != 4:
        if op == 1:
            dni = int (input("Ingrese Dni del Alumno: \n"))
            print("El Promedio sin Aplazos del dni {} es de: {}".format(dni, MM.InformarPromedioSinAplazos(dni)))
            print("El promedio con Aplazos del dni {} es de {}:".format(dni,MM.InformarPromedioConAplazos(dni) ))
            #MM.InformarPromedio(dni)
        elif op ==2:
            materia= input("Ingrese el Nombre de la Materia: \n")
            MA.InformarPromocional(materia,MM)
        elif op ==3:
            alumnosOrdenados= MA.listaOrdenada()
            MA.mostrarAlumnos(alumnosOrdenados)
            """MA.crearorden()"""
        op = int(input('Ingrese una opcion'))
          
    