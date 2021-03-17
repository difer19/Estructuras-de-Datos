class Nodo_Pila:
    def __init__(self, Dato):
        """Metodo Constructor de la clase pila, permite 
        instanciar la clase  

        Args:
            Dato [Object]: Dato que se almacena en el nodo;
        """
        self.dato = Dato
        self.sig = None
    
    def __str__(self):
        """Metodo que devuelve una cadena que muestra el dato 
        de cada nodo

        Returns:
            [str]: [cadena que contiene el dato del nodo]
        """
        return str(self.dato)

class Pila:
    """
    Implementacion de la estructura de datos llamada Pila
    """
    def __init__(self):
        """
        Metodo Constructor de la clase Pila
        """
        self.nodo_cima = None
        self.size = 0
    
    def __len__(self):
        """Metodo que retorna la cantidad de datos de la Pila

        Returns:
            [int]: [entero con la cantidad de datos de la Pila]
        """
        return self.size
    
    def es_vacia(self):
        """Metodo que identifica si la Pila no contiene datos

        Returns:
            [bool]: [True si la Pila no tiene elementos, False
            en caso contrario]
        """
        if self.size == 0:
            return True
        else:
            return False
    
    def cima(self):
        """Metodo que retorna el dato que contiene el nodo que 
        esta en la cima de la Pila

        Returns:
            [Object]: [dato del nodo que esta en la cima de la
            Pila]
        """
        if self.es_vacia() is True:
            return None
        return self.nodo_cima.dato
    
    def apilar(self, dato):
        """Metodo que inserta un nodo en la cima de la Pila

        Args:
            dato ([Object]): [Dato que contendra el nodo a
            insertar]

        Returns:
            [bool]: [True si el nodo es apilado con exito,
            False en caso contrario]
        """
        nodo_new = Nodo_Pila(dato)
        if self.es_vacia():
            self.nodo_cima = nodo_new
            self.size += 1
        else:
            if type(dato) != type(self.nodo_cima.dato):
                return False
            else:
                nodo_new.sig = self.nodo_cima
                self.nodo_cima = nodo_new
                self.size += 1
        return True
    
    def desapilar(self):
        """Metodo que retira el nodo que se encuentra en la
        cima y retorna el dato que contenia el nodo

        Returns:
            [Object]: [Dato que contenia el nodo de la cima]
        """
        if self.es_vacia():
            return None
        else:
            dato = self.nodo_cima.dato
            self.nodo_cima = self.nodo_cima.sig
            self.size -= 1
            return dato
    
    def __iter__(self):
        """Metodo que retorna el iterador de la pila

        Returns:
            [iter]: [Iterador de la pila]
        """
        P = Pila()
        ListDatos = []
        while len(self) != 0:
            cima = self.desapilar()
            P.apilar(cima)
            ListDatos.append(cima)
        while len(P) != 0:
            self.apilar(P.desapilar())
        return iter(ListDatos)