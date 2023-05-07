from ClaseAlumno import Alumno
import numpy as np
import csv
class ManejadorAlumno:
    __cantidad= 0
    __dimension = 0
    __incremento = 5
    
    def __init__(self, dimension, incremento=5):
        self.__alumnos = np.empty(dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        
    def agregarAlumno(self,alum):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad] = alum
        self.__cantidad +=1
        
    def cargarArreglo(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo,delimiter=";")
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            apellido= str(fila[1])
            nombre = str(fila[2])
            carrera = str(fila[3])
            anio = int(fila[4])
            alum = Alumno(dni, apellido, nombre, carrera, anio)
            self.agregarAlumno(alum)
    def listaOrdenada(self):
        alumnosOrdenados= sorted(self.__alumnos)     
        return alumnosOrdenados
    
    
    def mostrarAlumnos(self, ordenados):
      for i in range (self.__dimension):
         print(ordenados[i])
    """" def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__alumnos[i].mostrarAlumno())
    
    def crearOrden(self):
        listaordenada = sorted(self.__alumnos, reverse=False)
        for i in range(listaordenada):
            print(listaordenada[i].mostrarAlumno())"""
            
    