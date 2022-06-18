from typing_extensions import Self
from secuenciales.colaprioridad import *
from secuenciales.pila import Pila
import copy


class nodoGrafo:
    def __init__(self, nodo_padre, torreA, torreB, torreC):
        self.torreA = torreA
        self.torreB = torreB
        self.torreC = torreC
        self.padre = nodo_padre
        self.nivel = self.calcularNivelNodo()
        self.funcion_heuristica = self.CalcularFuncionHeuristica()
    
    def calcularNivelNodo(self):
        if self.padre is not None:
            return self.padre.nivel + 1
        else:
            return 0
    
    def CalcularFuncionHeuristica(self):
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
        
        #if self.nivel > 15:
        #    valor_heuristico -= 15

        return valor_heuristico - self.nivel
    
    def convertirEnLista(self, torre):
        auxTorre = copy.deepcopy(torre)
        lista = []
        if len(auxTorre) > 0:
            for disco in auxTorre:
                lista.append(disco)
                auxTorre.desapilar()
        return lista
    
    def generarEstadosSucesores(self):
        lista_sucesores = []
        if not (self.torreA.cima() is None):
            lista_sucesores += self.generarSucesores("A")
        if not (self.torreB.cima() is None):
            lista_sucesores += self.generarSucesores("B")
        if not (self.torreC.cima() is None):
            lista_sucesores += self.generarSucesores("C")
        return lista_sucesores
    
    def generarSucesores(self, idTorre):
        if idTorre == "A":
            lista_sucesoresA = []
            copia_estado1 = copy.deepcopy(self)
            copia_estado2 = copy.deepcopy(self)
            copia_estado1.torreB.apilar(copia_estado1.torreA.cima())
            copia_estado1.torreA.desapilar()
            self.recalcularParametros(copia_estado1)
            lista_sucesoresA.append(copia_estado1)
            copia_estado2.torreC.apilar(copia_estado2.torreA.cima())
            copia_estado2.torreA.desapilar()
            self.recalcularParametros(copia_estado2)
            lista_sucesoresA.append(copia_estado2)
            return lista_sucesoresA
        if idTorre == "B":
            lista_sucesoresB = []
            copia_estado1 = copy.deepcopy(self)
            copia_estado2 = copy.deepcopy(self)
            copia_estado1.torreA.apilar(copia_estado1.torreB.cima())
            copia_estado1.torreB.desapilar()
            self.recalcularParametros(copia_estado1)
            lista_sucesoresB.append(copia_estado1)
            copia_estado2.torreC.apilar(copia_estado2.torreB.cima())
            copia_estado2.torreB.desapilar()
            self.recalcularParametros(copia_estado2)
            lista_sucesoresB.append(copia_estado2)
            return lista_sucesoresB
        if idTorre == "C":
            lista_sucesoresC = []
            copia_estado1 = copy.deepcopy(self)
            copia_estado2 = copy.deepcopy(self)
            copia_estado1.torreB.apilar(copia_estado1.torreC.cima())
            copia_estado1.torreC.desapilar()
            self.recalcularParametros(copia_estado1)
            lista_sucesoresC.append(copia_estado1)
            copia_estado2.torreA.apilar(copia_estado2.torreC.cima())
            copia_estado2.torreC.desapilar()
            self.recalcularParametros(copia_estado2)
            lista_sucesoresC.append(copia_estado2)
            return lista_sucesoresC
    
    def recalcularParametros(self, estado):
        estado.padre = self
        estado.nivel = estado.calcularNivelNodo()
        estado.funcion_heuristica = estado.CalcularFuncionHeuristica()

    def __eq__(self, other) -> bool:
        if self.convertirEnLista(self.torreA) == self.convertirEnLista(other.torreA) and self.convertirEnLista(self.torreB) == self.convertirEnLista(other.torreB) and self.convertirEnLista(self.torreC) == self.convertirEnLista(other.torreC):
            return True
        return False
    
    def __str__(self) -> str:
        estado = ""
        for disco in reversed(self.convertirEnLista(self.torreA)):
            estado += str(disco) + " "
        estado += "\n"
        for disco in reversed(self.convertirEnLista(self.torreB)):
            estado += str(disco) + " "
        estado += "\n"
        for disco in reversed(self.convertirEnLista(self.torreC)):
            estado += str(disco) + " "
        estado += "\n"
        estado += "FH = " + str(self.funcion_heuristica)
        return estado

def inAbiertos(abiertos, estado):
    flag = False
    for abierto in abiertos:
        if abierto.__eq__(estado):
            flag = True
            break
    return flag
    

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
    abiertos.encolar(estado_inicial, estado_inicial.funcion_heuristica)
    estado_actual = estado_inicial
    contador = 0
    while not (estado_actual.__eq__(estado_objetivo)) and len(abiertos) > 0:
        estado_actual = abiertos.desencolar().dato
        print(estado_actual)
        print("=======================")
        if estado_actual not in cerrados:
            sucesores = estado_actual.generarEstadosSucesores()
            for estado in sucesores:
                if (inAbiertos(abiertos, estado)) or len(abiertos) == 0:
                    abiertos.encolar(estado, estado.funcion_heuristica)
        cerrados.append(estado_actual)
        contador += 1
    if estado_actual.__eq__(estado_objetivo):
        print("Exito")
        print(estado_actual.nivel)
        print(contador)

        
        