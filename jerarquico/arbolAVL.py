from jerarquico.recorridos import *


class NodoArbolAVL:
    def __init__(self, clave):
        self.clave = clave
        self.height = 1
        self.izq = None
        self.der = None
    
    def __str__(self):
        return str(self.clave)
    
    def tiene_hijos(self):
        return self.izq is None and self.der is None
    
class ArbolAVL:
    def __init__(self):
        self.raiz = None
    
    def __getAltura(self, sub_arbol):
        if sub_arbol is None: 
            return 0
        return sub_arbol.height
    
    def insertar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolAVL(nueva_clave)
        elif type(nueva_clave) == type(sub_arbol.clave):
            if nueva_clave < sub_arbol.clave:
                sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
            elif nueva_clave > sub_arbol.clave:
                sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)    
        
        sub_arbol.height = 1 + 1 + max(self.__getAltura(sub_arbol.izq), self.__getAltura(sub_arbol.der))

        balance = self.getBalance(sub_arbol)

        if balance > 1 and nueva_clave < sub_arbol.izq.clave:
            return self.rotacionDerecha(sub_arbol)
        elif balance < -1 and nueva_clave > sub_arbol.der.clave:
            return self.rotacionIzquierda(sub_arbol)
        elif balance > 1 and nueva_clave > sub_arbol.izq.clave:
            sub_arbol.izq = self.rotacionIzquierda(sub_arbol.izq)
            return self.rotacionDerecha(sub_arbol)
        elif balance < -1 and nueva_clave < sub_arbol.der.clave:
            sub_arbol.der = self.rotacionDerecha(sub_arbol.der)
            return self.rotacionIzquierda(sub_arbol)
        return sub_arbol
    
    def minimo(self, sub_arbol): 
        if sub_arbol is None or sub_arbol.izq is None: 
            return sub_arbol
        return self.minimo(sub_arbol.izq) 
    
    def eliminar(self, clave_eliminar):
        return self.__eliminar(self.raiz, clave_eliminar)

    def __eliminar(self, sub_arbol, clave_eliminar): 
        if sub_arbol is None: 
            return sub_arbol
        elif clave_eliminar < sub_arbol.clave: 
            sub_arbol.izq = self.__eliminar(sub_arbol.izq, clave_eliminar) 
        elif clave_eliminar > sub_arbol.clave: 
            sub_arbol.der = self.__eliminar(sub_arbol.der, clave_eliminar) 
        else: 
            if sub_arbol.izq is None: 
                temp = sub_arbol.der 
                sub_arbol = None
                return temp 
            elif sub_arbol.der is None: 
                temp = sub_arbol.izq
                sub_arbol = None
                return temp 
            temp = self.minimo(sub_arbol.der) 
            sub_arbol.clave = temp.clave 
            sub_arbol.der = self.__eliminar(sub_arbol.der, temp.clave) 

        if sub_arbol is None: 
            return sub_arbol 
  
        sub_arbol.height = 1 + max(self.__getAltura(sub_arbol.izq), self.__getAltura(sub_arbol.der)) 
  
        balance = self.getBalance(sub_arbol) 
  
        if balance > 1 and self.getBalance(sub_arbol.izq) >= 0: 
            return self.rotacionDerecha(sub_arbol)
        if balance < -1 and self.getBalance(sub_arbol.der) <= 0: 
            return self.rotacionIzquierda(sub_arbol) 
        if balance > 1 and self.getBalance(sub_arbol.izq) < 0: 
            sub_arbol.izq = self.rotacionIzquierda(sub_arbol.izq) 
            return self.rotacionDerecha(sub_arbol) 
        if balance < -1 and self.getBalance(sub_arbol.der) > 0: 
            sub_arbol.der = self.rotacionDerecha(sub_arbol.der) 
            return self.rotacionIzquierda(sub_arbol) 
        return sub_arbol

    def getBalance(self, sub_arbol):
        if sub_arbol is not self.raiz:
            return 0
        return self.__getAltura(sub_arbol.izq) - self.__getAltura(sub_arbol.der)      
    
    def rotacionDerecha(self, sub_arbol):
        aux1 = sub_arbol.izq
        aux2 = aux1.der
        aux1.der = sub_arbol
        sub_arbol.izq = aux2
        sub_arbol.height = 1 + max(self.__getAltura(sub_arbol.izq), self.__getAltura(sub_arbol.der))
        aux1.height = 1 + max(self.__getAltura(aux1.izq), self.__getAltura(aux1.der))
        return aux1

    def rotacionIzquierda(self, sub_arbol):
        aux1 = sub_arbol.der
        aux2 = aux1.izq
        aux1.izq = sub_arbol
        sub_arbol.der = aux2
        sub_arbol.height = 1 + max(self.__getAltura(sub_arbol.izq), self.__getAltura(sub_arbol.der))
        aux1.height = 1 + max(self.__getAltura(aux1.izq), self.__getAltura(aux1.der))
        return aux1
    
    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)
    
    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if clave_buscar == sub_arbol.clave:
                return sub_arbol.clave
            elif clave_buscar < sub_arbol.clave:
                return self.__buscar(sub_arbol.izq, clave_buscar)
            else:
                return self.__buscar(sub_arbol.der, clave_buscar)
        return None
    
    def __len__(self):
        return self.__numero_nodos(self.raiz) 
    
    def __numero_nodos(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + 
                self.__numero_nodos(sub_arbol.izq) +
                self.__numero_nodos(sub_arbol.der))
        return 0
    
    def hojas(self):
        return self.__numero_hojas(self.raiz)
    
    def __numero_hojas(self, sub_arbol):
        ctr_hojas = 0
        if sub_arbol is not None:
            if (sub_arbol.izq is None and sub_arbol.der is None):
                return 1 
            else:
                if sub_arbol.izq is not None:
                    ctr_hojas += self.__numero_hojas(sub_arbol.izq)   
                if sub_arbol.der is not None:
                    ctr_hojas += self.__numero_hojas(sub_arbol.der) 
        return ctr_hojas

    def internos(self):
        return self.__numero_internos(self.raiz)

    def __numero_internos(self, sub_arbol):
        ctr_internos = 0
        if sub_arbol is not None:
            if sub_arbol.izq is not None:
                ctr_internos += self.__numero_internos(sub_arbol.izq)
            if sub_arbol.der is not None:
                ctr_internos += self.__numero_internos(sub_arbol.der)
            if (sub_arbol.izq is None and sub_arbol.der is not None):
                return (ctr_internos + 1)
            elif (sub_arbol.izq is not None and sub_arbol.der is None):
                return (ctr_internos + 1)
            elif (sub_arbol.izq is not None and sub_arbol.der is not None):
                return (ctr_internos + 1)        
        return ctr_internos
    
    def altura(self):
        return self.__altura(self.raiz)

    def __altura(self, sub_arbol):
        if sub_arbol is None:
            return 0
        else:
            return (1 + max(self.__altura(sub_arbol.izq), self.__altura(sub_arbol.der)))