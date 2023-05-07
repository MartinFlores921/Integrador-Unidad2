#from datetime import date
import csv
from ClaseAlumno import Alumno
from ManejadorAlumno import ManejadorAlumno
from ClaseMateriasAprobadas import Materia
class ManenejadorMateria:
    __lista: list
    
    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo= open("materiasAprobadas.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            dni= int(fila[0])
            nombre= fila[1]
            fecha = (fila[2])
            nota= int(fila[3])
            aprobacion = fila[4]
            instancia = Materia (dni, nombre, fecha, nota, aprobacion)
            self.__lista.append(instancia)
    def InformarPromedioSinAplazos(self, dni):
        acumNota=0
        c=0
        for i in range (len(self.__lista)):
            if self.__lista[i].getDni() == dni:
                if self.__lista[i].getNota() >= 4 :
                    acumNota += self.__lista[i].getNota()
                    c = c+1
        if c==0:
            promedio= 0
        else:
            promedio= (acumNota/c)
        return promedio
    def InformarPromedioConAplazos(self, dni):
        acum_nota = 0
        c=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni() == dni:
                if self.__lista[i].getNota() < 4:
                    acum_nota += self.__lista[i].getNota()
                    c = c + 1
        if c ==0:
          prom=0
        else:
           prom= (acum_nota/c)
        return prom
 
    def InformarPromocional(self, materia):
        conAlum= ManejadorAlumno(3,10)
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next (reader)
        i = len(list(reader))
        conAlum= ManejadorAlumno(i, i*2)
        conAlum.cargarArreglo()
        for i in range(len(self.__lista)):
            if materia == self.__lista[i].getNombre:
                if self.__lista[i].getAprobacion == "P":
                    print(f"{self.__lista[i].getdni() :<20} {conAlum.getAlumno(self.__lista[i].getdni()).getAyN():<30} {self.__lista[i].getfecha():<15} {self.__lista[i].getnota():<4}")
        
    
    
    
        