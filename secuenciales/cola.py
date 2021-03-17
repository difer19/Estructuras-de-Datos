class Nodo_Cola:
    def __init__(self, Dato):
        """Metodo Constructor de la clase Nodo_Cola

        Args:
            Dato [Object]: Dato que se almacena en el nodo;
        """
        self.dato = Dato
        self.sig = None
    
    def __str__(self):
        """Metodo que devuelve un str que muestra el dato 
        de cada nodo

        Returns:
            [str]: [cadena que contiene el dato del nodo]
        """
        return str(self.dato)

class Cola:
    """
    Implementacion de la estructura de datos llamada Cola
    """
    def __init__(self):
        """Metodo constructor de la clase Cola
        """
        self.nodo_cab = None
        self.nodo_fin = None
        self.size = 0
    
    def __len__(self):
        """Metodo que retorna un entero que representa la
        cantidad de nodos en la Cola

        Returns:
            [int]: [entero con la cantidad de nodos en la
            Cola]
        """
        return self.size
    
    def frente(self):
        """Metodo que retorna el nodo que esta en el frente
        de la Cola sin quitarlo

        Returns:
            [Object]: [Elemento que esta en el frente de la
            Cola]
        """
        return self.nodo_cab.dato
    
    def es_vacia(self):
        """Metodo que identifica si la Cola esta vacia

        Returns:
            [bool]: [True si la Cola no tiene elementos,
            False en caso contrario]
        """
        if self.size == 0:
            return True
        else:
            return False

    def encolar(self, dato):
        """Metodo que adiciona un elemento en el extremo
        final de la Cola

        Args:
            dato (Object): [Dato que contendra el nodo que
            se adicionara]

        Returns:
            [bool]: [True si se adiciona el nodo con exito,
            False en caso contrario]
        """
        nodo_new = Nodo_Cola(dato)
        if self.es_vacia() is True:
            self.nodo_cab = nodo_new
            self.nodo_fin = self.nodo_cab
            self.size += 1
        else:
            if type(dato) != type(self.nodo_cab.dato):
                return False
            self.nodo_fin.sig = nodo_new
            self.nodo_fin = self.nodo_fin.sig
            self.size += 1
        return True

    def desencolar(self):
        """Metodo que eliminara un nodo por el frente y
        retornara el dato que contenia dicho nodo

        Returns:
            [Object]: [Dato que contenia el nodo eliminado]
        """
        if self.es_vacia() is True:
            return None
        else:
            dato = self.nodo_cab.dato
            self.nodo_cab = self.nodo_cab.sig
            self.size -= 1
            if self.nodo_cab is None:
                self.nodo_fin = None
        return dato
    
    def buscarDato(self, dato_buscar):
        """Metodo que permite saber si un dato esta en la
        Cola

        Args:
            dato_buscar (Object): [Dato a buscar]

        Returns:
            [bool]: [True si el dato se encuentra en la
            cola, False en caso contrario]
        """
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            if nodo_actual.dato == dato_buscar:
                return True
            nodo_actual = nodo_actual.sig
        return False
    
    def __iter__(self):
        """Metodo que retorna el itereador de la cola

        Returns:
            [iter]: [Iterador de la colas]
        """
        ListDatos = []
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            ListDatos.append(nodo_actual)
            nodo_actual = nodo_actual.sig
        return iter(ListDatos)

        


