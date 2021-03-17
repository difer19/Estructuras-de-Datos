from secuenciales.iterador_ListaSE import Iterador_ListaSE


class NodoLSE:
    """
    Clase que almacena una referencia a un dato y a otro NodoLSE
    se utiliza en la creacion de Listas
    """
    def __init__(self, Dato):
        """Metodo Constructor de la clase NodoLSE, permite 
        instanciar la clase  

        Args:
            Dato [Dato]: Cualquier tipo de dato u objeto;
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
    
class ListaSE:
    """
    Implementacion de la estructura de datos llamada Lista
    Simplemente Enlazada
    """
    def __init__(self):
        """
        Metodo Constructor de la clase ListaSE, crea un
        nodo cabecera que hace referencia a None
        """
        self.nodo_cab = None
    
    def es_vacia(self):
        """Metodo que identifica si la lista esta vacia

        Returns:
            [bool]: [True si la lista esta vacia, False
            en caso contrario]
        """
        return self.nodo_cab is None
    
    def adicionar(self, nuevo_dato):
        """Metodo que adiciona un nuevo dato al final de la
        lista si el dato es del mismo tipo que el primer dato

        Args:
            nuevo_dato [Dato]: [Dato a ingresar en la lista]

        Returns:
            [bool]: [True si el elemento se pudo adicionar,
            False en caso contrario]
        """
        if self.es_vacia():
            self.nodo_cab = NodoLSE(nuevo_dato)
            return True
        else:
            if type(nuevo_dato) == type(self.nodo_cab.dato):
                nodo_actual = self.nodo_cab
                while nodo_actual.sig is not None:
                    nodo_actual = nodo_actual.sig
                nodo_actual.sig = NodoLSE(nuevo_dato)
                return True
            else:
                return False

    def recorrer(self):
        """
        Metodo que recorre e imprime los elementos de la Lista
        """
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.sig

    def buscar(self, dato_buscar):
        """Metodo que permite identificar si un dato
        esta en la lista

        Args:
            dato_buscar [Dato] : [Dato a buscar en la lista]

        Returns:
            [Dato]: [devuelve el dato en caso de haberlo
            encontrado, None en caso contrario]
        """
        nodo_actual = self.nodo_cab
        if type(dato_buscar) == type(self.nodo_cab.dato):
            while nodo_actual is not None:
                if(dato_buscar == nodo_actual.dato):
                    return nodo_actual.dato
                nodo_actual = nodo_actual.sig
        return None
    
    def localizar(self, pos):
        """ Metodo que permite identificar el dato que
        esta en cierta posicion

        Args:
            pos (int): [Posicion a buscar]

        Returns:
            [Dato]: [el dato en caso de que la
            posicion sea valida, None en caso contrario]
        """
        nodo_actual = self.nodo_cab
        count = 0
        if pos >= 0:
            while count <= pos and nodo_actual is not None:
                if count == pos:
                    return nodo_actual.dato 
                else:
                    count+=1
                    nodo_actual = nodo_actual.sig
        return None

    def __len__(self):
        """Metodo que identifica la cantidad de datos en
        la lista

        Returns:
            [int]: [Entero correspndiente a la cantidad de
            datos en la lista]
        """
        counter = 0
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            counter += 1
            nodo_actual = nodo_actual.sig
        return counter

    def insertar(self, dato_instertar, pos):
        """Metodo que inserta un dato en una posicion
        de la lista

        Args:
            dato_instertar (Dato): [Dato a insertar]
            pos (int): [Posicion en la que insertar el dato]

        Returns:
            [bool]: [True en caso de que se pueda insertar
            el dato, False en caso contrario]
        """
        if pos > 0 and pos < self.__len__():
            nodo_actual = self.nodo_cab
            nodo_new = NodoLSE(dato_instertar)
            counter = 1
            while counter < pos:
                nodo_actual = nodo_actual.sig
                counter += 1
            nodo_new.sig = nodo_actual.sig
            nodo_actual.sig = nodo_new
            return True
        if pos == 0:
            nodo_new = NodoLSE(dato_instertar)
            nodo_new.sig = self.nodo_cab
            self.nodo_cab = nodo_new
        return False

    def borrar(self, item, por_pos = True):  
        """Metodo que permite borrar nodos de la lista ya sea
        por posicion o todos los nodos con el dato

        Args:
            por_pos (bool, optional): [si es True elimina nodos por 
            posicion, elimina nodos por dato en caso contrario]. Defaults to True.
            item (int): [Posicion a eliminar]
            item (Dato): [Dato a eliminar]

        Returns:
            [bool]: [True si se pudo eliminar, False en caso contrario]
        """
        if por_pos:
            nodo_actual = self.nodo_cab
            nodo_anterior = None
            cr_pos = 0
            if item >= len(self) or item < 0:
                return False

            if item == 0:
                self.nodo_cab = self.nodo_cab.sig
                return True

            while cr_pos <= item:
                if cr_pos == item:
                    break
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
                cr_pos += 1
            nodo_anterior.sig = nodo_actual.sig
            return True
        
        else:
            counter = 0
            flag = 0
            for i in self:
                if i == item:
                    self.borrar(counter - flag,True)
                    flag += 1
                counter += 1
            if flag == 0:
                return False
            else:
                return True
            
    def __str__(self):
        """Metodo que devuelve una cadena con todos
        los datos de la lista

        Returns:
            [str]: [Cadena con los datos de la lista en
            una sola linea]
        """
        nodo_actual = self.nodo_cab
        a = ""
        while nodo_actual is not None:
            if nodo_actual.sig == None:
                a += " {"+ nodo_actual.__str__() + "}"
            else:
                a += " {"+ nodo_actual.__str__() + "} -"
            nodo_actual = nodo_actual.sig
        return a

    def __iter__(self):
        """Metodo que devuelve el iterador de la lista

        Returns:
            [Iterador]: [iterador de la lista]
        """
        return Iterador_ListaSE(self)

    
    
