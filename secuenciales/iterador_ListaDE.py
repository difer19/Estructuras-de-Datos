class Iterador_ListaDE:
    """
    Clase que genera un objeto Iterable de una Lista
    doblemente Enlazada
    """
    def __init__(self, List):
        """Metodo Constructor de la clase Iterador, recibe una Lista
        y hace una referencia al nodo cabecera de esa Lista

        Args:
            List [ListaDE]: [Objeto de la clase ListaDE]
        """
        self.nodo_actual = List.nodo_cab
    
    def __next__(self):
        """Metodo que retorna el dato correspondiente a cada iteracion

        Raises:
            StopIteration: [Detiene la iteracion en el caso de que la lista
            este vacia o ya se pasara por todos los elementos de la lista]

        Returns:
            [Dato]: [Dato correspondiente a cada iteracion]
        """
        if self.nodo_actual == None:
            raise StopIteration
        dato = self.nodo_actual.dato
        self.nodo_actual = self.nodo_actual.sig
        return dato
    
    def __iter__(self):
        """ Metodo que retorna el iterador de la ListaDE pasada como argumento

        Returns:
            [Iterador]: [Iterador de la ListaDE]
        """
        return self

