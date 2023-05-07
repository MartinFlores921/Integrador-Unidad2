class Alumno:
    __dni = int
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __anio = int
    
    def __init__(self, dni, apellido, nombre, carrera, anio) :
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio = anio
    
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        return self.__carrera
    def getAnio(self):
        return self.__anio
    def __str__(self):
        cadena = str(self.__anio) +" Año" +", "+ self.__carrera +", "+ self.__nombre +" "+ self.__apellido +", "+ str(self.__dni)
        return cadena
    def mostrarAlumno(self):
        return ("Alumno: {} {}. Dni: {}. Carrera: {}. Año de cursado: {}" .format(self.__nombre,self.__apellido,self.__dni,self.__carrera,self.__anio))
    
    def __lt__ (self, otro):
        if self.getAnio() == otro.getAnio():
            return (self.getApellido(), self.getNombre()) < (self.getApellido(),self.getNombre())
        else:
            return self.getAnio() < otro.getAnio() and ((self.getApellido(), self.getNombre())  < (otro.getApellido(), otro.getNombre()))
        