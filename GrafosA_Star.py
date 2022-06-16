from secuenciales.colaprioridad import *
from secuenciales.pila import Pila


class nodoGrafo:
    def __init__(self, nodo_padre, torreA, torreB, torreC):
        self.torreA = torreA
        self.torreB = torreB
        self.torreC = torreC
        self.padre = nodo_padre
        self.nivel = self.calcularNivelNodo()
        self.funcion_heuristica = self.CalcularFuncionHeurista()
    
    def calcularNivelNodo(self):
        if self.padre is not None:
            return self.padre.nivel + 1
        else:
            return 0
    
    def CalcularFuncionHeurista(self):
        valor_heuristico = 0
        iteracion = 0
        aux_disco = 0

        if len(self.torreA) > 0:
            for disco in self.torreA:
                if iteracion == 0:
                    aux_disco = disco
                    iteracion += 1
                elif aux_disco < disco:
                    valor_heuristico += 1
                    aux_disco = disco
                elif aux_disco > disco:
                    valor_heuristico -= 1000
            
            valor_heuristico += 1
        
        iteracion = 0
        if len(self.torreB) > 0:
            for disco in self.torreB:
                if iteracion == 0:
                    aux_disco = disco
                    iteracion += 1
                elif aux_disco < disco:
                    valor_heuristico += 5
                    aux_disco = disco
                elif aux_disco > disco:
                    valor_heuristico -= 1000
            
            valor_heuristico += 5

        iteracion = 0
        if len(self.torreC) > 0:          
            for disco in self.torreC:
                if iteracion == 0:
                    aux_disco = disco
                    iteracion += 1
                elif aux_disco < disco:
                    valor_heuristico += 10
                    aux_disco = disco
                elif aux_disco > disco:
                    valor_heuristico -= 1000
            
            valor_heuristico += 10

        return valor_heuristico - self.nivel
    
    def convertirEnLista(self, torre):
        auxTorre = torre
        lista = []
        if len(auxTorre) > 0:
            for disco in auxTorre:
                lista.append(disco)
                auxTorre.desapilar()
        return lista
        

    def __eq__(self, other) -> bool:
        if self.convertirEnLista(self.torreA) == self.convertirEnLista(other.torreA) and self.convertirEnLista(self.torreB) == self.convertirEnLista(other.torreB) and self.convertirEnLista(self.torreC) == self.convertirEnLista(other.torreC):
            return True
        return False

if __name__ == "__main__":
    abiertos = Colaprioridad()
    cerrados = []

    torreA = Pila()
    torreA.apilar(4)
    torreA.apilar(3)
    torreA.apilar(2)
    torreA.apilar(1)
    torreB = Pila()
    torreC = Pila()

    torreAo = Pila()
    torreBo = Pila()
    torreCo = Pila()
    torreCo.apilar(4)
    torreCo.apilar(3)
    torreCo.apilar(2)
    torreCo.apilar(1)

    estado_inicial = nodoGrafo(None, torreA, torreB, torreC)
    estado_objetivo = nodoGrafo(None, torreAo, torreBo, torreCo)
    estado_actual = estado_inicial
    while not (estado_actual.__eq__(estado_objetivo)) and len(abiertos) > 0:
        pass


        
        