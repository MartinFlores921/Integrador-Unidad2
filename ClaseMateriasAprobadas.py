from datetime import date
class Materia:
    __dni = int
    __nombreMateria = ""
    __fecha = date
    __nota = 0
    __aprobacion = ""
    
    def __init__ (self, dni, nombre, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombre
        self.__fecha= fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombreMateria
    
    def getFecha(self):
        return self.__fecha
    
    def getNota(self):
        return self.__nota
    
    def getAprobacion(self):
        return self.__aprobacion
    
    def __eq__(self, otro) :
        return self.__getDni() == otro
    
    def mostrar(self):
        return print("Dni del Alumno: {}, Materia: {}, Fecha que curso: {}, Nota: {}, Aprobacion: {}".format(self.__dni, self.__nombreMateria,self.__fecha, self.__nota, self.__aprobacion))
              