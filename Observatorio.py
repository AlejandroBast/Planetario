from Planeta import Planeta

class Observatorio:
    def __init__(self):
        self.CANTIDAD_PLANETAS = 8
        self.Planetas = []
        
        self.agregados = 0
        
    def getNombrePlanetas(self):
        for planeta in self.Planetas:
            print(planeta.getNombre())
    
    def getSateliteNatural(self, nombre):
        for planeta in self.Planetas:
            return planeta.buscarSatelite(nombre)
    
    def getPlanetaPorDistancia(self, distancia):
        for planeta in self.Planetas:
            if planeta.getDistanciaMediaSol() == distancia:
                return planeta
    
    def getPlanetaPorInclinacion(self, inclinacion):
        for planeta in self.Planetas:
            if planeta.getInclinacion() == inclinacion:
                return planeta
            
    def agregarSateliteNatural(self, planetaDelSatelite, satelite):
        for planeta in self.Planetas:
            if planeta.getNombre() == planetaDelSatelite:
                planeta.agregarSatelite(satelite)
    
    def eliminarSatelite(self, palentaDelSatelite, sateliteRemover):
        for planeta in self.Planetas:
            if planeta.getNombre() == palentaDelSatelite:
                planeta.eliminarSatelite(sateliteRemover)
     
    def editarSatelite(nombrePlaneta, nombreSatelite, valor_a_Modificar, nuevoValor):
        for planeta in self.Planetas:
            if planeta.getNombre() == nombrePlaneta:
                planeta.editarSatelite(nombreSatelite, valor_a_Modificar, nuevoValor)
                
    def agregarPlaneta(self, Planeta):
        if self.agregados < self.CANTIDAD_PLANETAS:
            self.Planetas.append(Planeta)
            self.agregados += 1
        else:
            print("No se puede agregar mas planetas")
    
    def eliminarPlaneta(self, planeta):
        for planeta in self.Planetas:
            if planeta.getNombre() == planeta:
                self.Planetas.pop(planeta)