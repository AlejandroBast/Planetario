from SateliteNatural import SateliteNatural

class Planeta:
    def __init__(self, nombre, distanciaMediaSol, excentricidad, PeriodoOrbitalSinodico, velocidadOrbital, inclinacion):
        self.__nombre = nombre
        self.__distanciaMediaSol = distanciaMediaSol
        self.__excentricidad = excentricidad
        self.__PeriodoOrbitalSinodico = PeriodoOrbitalSinodico
        self.__velocidadOrbital = velocidadOrbital
        self.__inclinacion = inclinacion
        # lista de satelites
        self.__satelites = []
        # cantidad satelites
        self.__cantidadSatelites = 0
        
    def getNombre(self):
        return self.__nombre
    
    def getDistanciaMediaSol(self):
        return self.__distanciaMediaSol
    
    def getInclinacion(self):
        return self.__inclinacion
    
    def agregarSateliteNatural(self, satelite):
        self.__satelites.append(satelite)
        self.__cantidadSatelites += 1
        
    def eliminarSatelite(self, nombre):
        for satelite in self.__satelites:
            if satelite.getNombre() == nombre:
                self.__satelites.remove(satelite)
                self.__cantidadSatelites -= 1
            break
            
    def editarSatelite(self, nombre, valorModificar, nuevoValor):
        for satelite in self.__satelites:
            if satelite.getNombre() == nombre:
                if satelite.getNombre() == valorModificar:
                    satelite.setNombre(nuevoValor)
                elif satelite.getDistanciaMediaSol() == valorModificar:
                    satelite.setDistanciaMediaSol(nuevoValor)
                elif satelite.getInclinacion() == valorModificar:
                    satelite.setInclinacion(nuevoValor)
            break
    
    def getCantidadSatelites(self):
        return self.__cantidadSatelites
    
    def getSatelites(self):
        return self.__satelites
    
    def buscarSatelite(self, nombre):
        for satelite in self.__satelites:
            if satelite.getNombre() == nombre:
                return satelite
            