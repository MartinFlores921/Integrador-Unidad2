from ManejadorAlumno import ManejadorAlumno
from ClaseAlumno import Alumno
import csv
from ManejadorMaterias import ManenejadorMateria
from Menu import menu

if __name__ == "__main__":
    maAlumno = ManejadorAlumno(3,10)
    archivo = open("alumnos.csv")
    reader = csv.reader(archivo, delimiter=";")
    next (reader)
    i = len(list(reader))
    maAlumno = ManejadorAlumno(i, i*2)
    maAlumno.cargarArreglo()
    maMateria = ManenejadorMateria()
    maMateria.cargaLista()
    menu(maAlumno, maMateria)
    
    
    