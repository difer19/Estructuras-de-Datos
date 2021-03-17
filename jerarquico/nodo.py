class NodoArbolBinario:

    def __init__(self, clave):
        """Método constructor de la clase NodoArbolBinario

        Args:
            clave (Object): Dato que se almacena en el nodo
        """
        self.clave = clave
        self.izq = None
        self.der = None

    def __str__(self):
        """Metodo que devuelve una cadena que muestra el dato 
        de cada nodo

        Returns:
            str: Cadena que continene el dato del nodo
        """
        return str(self.clave)

    def tiene_hijos(self):
        """Método que devuelve un valor booleano dependiendo de 
        si encuentra o no, un hijo por izquierda o por derecha 

        Returns:
            bool: True si el nodo tiene algún hijo. False en
                caso de que no tenga hijos
        """
        return self.izq is not None or self.der is not None