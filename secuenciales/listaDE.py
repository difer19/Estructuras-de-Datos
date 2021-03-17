from secuenciales.iterador_ListaDE import Iterador_ListaDE


class NodoDE:
    """
    Clase que representa el nodo de una lista
    doblemente enlazada
    """
    def __init__(self, Dato):
        """Metodo constructor de la clase
        Args:
            Dato ([Object]): [Dato que se almacena en el nodo]
        """
        self.dato = Dato
        self.sig = None
        self.ant = None
    
    def __str__(self):
        """Metodo que retorna una cadena con la presentacion 
        del nodo

        Returns:
            [str]: [Cadena con la presentacion del nodo]
        """
        return str(self.dato)

class ListaDE:
    """
    Implementacion de la estructura de datos llamada Lista
    Doblemente Enlazada
    """
    def __init__(self):
        """
        Metodo constructor de la clase
        """
        self.nodo_cab = None
        self.nodo_last = None
        self.valor = False
        self.pointer = None
        self.pointer_flag = False
        self.pointer_pos = 0

    def es_vacia(self):
        """Metodo que identifica si la lista esta vacia
        
        Returns:
            [bool]: [True si la lista esta vacia, False en caso
            contrario]
        """
        return self.nodo_cab is None

    def __len__(self):
        """Metodo que retorna un entero con la cantidad de nodos
        en la lista
        
        Returns:
            [int]: [Entero con la cantidad de datos de la lista]
        """
        nodo_actual = self.nodo_cab
        counter = 0
        while nodo_actual is not None:
            counter += 1
            nodo_actual = nodo_actual.sig
        return counter
    
    def adicionar(self, nuevo_dato):
        """Metodo que adiciona un nuevo dato al final de la
        lista

        Args:
            nuevo_dato ([Object]): [Objeto a ingresar en la lista]

        Returns:
            [bool]: [True si el dato se pudo adicionar, False en 
            caso contrario]
        """
        if self.es_vacia():
            self.nodo_cab = self.nodo_last = NodoDE(nuevo_dato)
        elif type(nuevo_dato) == type(self.nodo_cab.dato):        
            aux = self.nodo_last
            self.nodo_last = aux.sig = NodoDE(nuevo_dato)
            self.nodo_last.ant = aux
            return True
        return False

    def poner_inverso(self, valor = True):
        """Metodo que cambia el orden en el que la cadena del metodo
        __str__ muestra los datos

        Args:
            valor (bool, optional): [True para cambiar
            el orden de presentacion, False para volver a la forma de
            presentacion original]. Defaults to True.
        """
        self.valor = valor
        
    def __str__(self):
        """Metodo que retorna una cadena con la presentacion de los
        datos de la lista

        Returns:
            [str]: [cadena con la presentacion de los datos de la lista]
        """
        a = ""
        if self.valor is False:
            nodo_actual = self.nodo_cab
            while nodo_actual is not None:
                if nodo_actual.sig is None:
                    a += str(nodo_actual)
                else:
                    a += str(nodo_actual) + "<=>"
                nodo_actual = nodo_actual.sig
            return a
        else:
            nodo_actual = self.nodo_last
            while nodo_actual is not None:
                if nodo_actual.ant is None:
                    a += str(nodo_actual)
                else:
                    a += str(nodo_actual) + "<=>"
                nodo_actual = nodo_actual.ant
            return a
    
    def buscar(self, item, por_pos = True):
        """Metodo que retorna el nodo de una posicion de la lista
        o el nodo cuyo dato coincide con aquel que se envie como parametro 

        Args:
            item ([Object or int]): [Object si se busca por dato, int si se
            busca por posicion]
            por_pos (bool, optional): [True si se va a buscar por
            posicion, False si se busca por dato]. Defaults to True.

        Returns:
            [Object]: [El dato encontrado o None en caso de no haber coincidencias]
        """
        if por_pos:
            if item >= len(self) or item < 0:
                return None
            else:
                nodo_actual = self.nodo_cab
                counter = 0
                while counter < len(self):
                    if counter == item:
                        return nodo_actual.dato
                    counter += 1
                    nodo_actual = nodo_actual.sig
            return None
        else:
            nodo_actual = self.nodo_cab
            while nodo_actual is not None:
                if item == nodo_actual.dato:
                    return nodo_actual.dato
                nodo_actual = nodo_actual.sig
            return None
    
    def insertar(self, nuevo_dato, pos = 0):
        """Metodo que inserta un dato en cualquier posicion de
        la lista

        Args:
            nuevo_dato ([Object]): [Dato a insertar]
            pos (int, optional): [posicion en la que insertar el dato]. Defaults to 0.

        Returns:
            [bool]: [True en caso de insertar el dato con exito, False en caso contrario]
        """
        if len(self) == 0 or type(nuevo_dato) != type(self.nodo_cab.dato):
            return False
        elif pos > 0 and pos < len(self):
            nodo_actual = self.nodo_cab
            nodo_new = NodoDE(nuevo_dato)
            counter = 1
            while counter <= pos:
                nodo_actual = nodo_actual.sig
                counter += 1
            nodo_new.ant = nodo_actual.ant
            nodo_actual.ant.sig = nodo_new
            nodo_new.sig = nodo_actual
            nodo_actual.ant = nodo_new
            if self.pointer_pos == pos and self.pointer_flag is True:
                self.pointer_pos += 1
            return True
        elif pos == 0:
            nodo_new = NodoDE(nuevo_dato)
            nodo_actual = self.nodo_cab
            nodo_new.sig = nodo_actual
            nodo_actual.ant = nodo_new
            self.nodo_cab = nodo_new
            if self.pointer_pos == pos and self.pointer_flag is True:
                self.pointer_pos += 1
            return True
        elif pos == len(self):
            self.adicionar(nuevo_dato)
            return True
        return False
    
    def borrar(self, dato_borrar):
        """Metodo que elimina todos los nodos cuyos datos coincidan con
        el parametro dado como entrada

        Args:
            dato_borrar ([Object]): [Dato a eliminar]

        Returns:
            [bool]: [True en caso de que se elimine al menos un solo
            dato, False en caso contrario]
        """
        counter = 0
        flag = 0
        for i in self:
            if i == dato_borrar:
                self.borrar_pos(counter - flag)
                flag += 1
            counter += 1
        if flag == 0:
            return False
        else:
            return True
    
    def borrar_pos(self, pos):
        """Metodo que elimina el nodo correspondiente a una posicion
        dada como parametro

        Args:
            pos ([int]): [Posicion a eliminar]

        Returns:
            [bool]: [True en caso de eliminar el nodo de la posicion
            con exito, False en caso contrario]
        """
        nodo_actual = self.nodo_cab
        counter = 0
        if pos == 0:
            self.__ajustar(pos)
            if len(self) == 0:
                return False
            if self.nodo_cab.sig == None:
                self.nodo_cab = self.nodo_last = None
                return True
            self.nodo_cab = self.nodo_cab.sig
            self.nodo_cab.ant = None
            return True
        if pos == len(self) - 1:
            self.__ajustar(pos)
            if len(self) == 0:
                return False
            if self.nodo_cab.sig == None:
                self.nodo_cab = self.nodo_last = None
                return True
            self.nodo_last = self.nodo_last.ant
            self.nodo_last.sig = None
            return True
        if pos > 0 and pos < len(self):
            self.__ajustar(pos)
            while nodo_actual is not None and counter != pos:
                if counter == pos:
                    break
                nodo_actual = nodo_actual.sig
                counter += 1
            nodo_actual.ant.sig = nodo_actual.sig
            nodo_actual.sig.ant = nodo_actual.ant
            return True
        else:
            return False
        
    def adelante(self):
        """Metodo que permite recorrer la lista nodo por nodo
        hacia adelante

        Returns:
            [Object]: [nodo siguiente al original]
        """
        if self.pointer_flag == False:
            self.pointer = self.nodo_cab
            self.pointer_flag = True
            return self.pointer
        else:
            if self.pointer.sig is None:
                return self.pointer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            self.pointer = self.pointer.sig
            self.pointer_pos += 1
            return self.pointer
    
    def atras(self):
        """Metodo que permite recorrer la lista nodo por nodo
        hacia atras

        Returns:
            [Object]: [nodo anterior al original]
        """
        if self.pointer_flag == False:
            return None
        else:
            if self.pointer.ant is None:
                return self.pointer
            self.pointer = self.pointer.ant
            self.pointer_pos -= 1
            return self.pointer

    def __iter__(self):
        """Metodo que retorna el iterador de la lista
        Returns:
            [Iterador_ListaDe]: [Iterador de la lista]
        """
        return Iterador_ListaDE(self)
    
    def __ajustar(self, pos):
        """Metodo privado que ajusta las variables de la clase cuando
        se borra un dato y el pointer se encuentra en ese nodo, permite 
        recorrer adecuadamente la lista

        Args:
            pos ([int]): [Posicion en la que se desea ajustar
            las variables de la clase]
        """
        if self.pointer_pos == pos and self.pointer_flag is True:
            nodo_actual = self.nodo_cab
            counter = 0
            while counter < pos:
                counter += 1
                nodo_actual = nodo_actual.sig
            
            if nodo_actual.ant is None:
                self.pointer = self.pointer.sig
                self.pointer_pos += 1
            elif nodo_actual.ant is None and nodo_actual.sig is None:
                self.pointer = None
                self.pointer_flag = False
                self.pointer_pos = 0
            else:
                self.pointer_pos -= 1
                self.pointer = self.pointer.ant




