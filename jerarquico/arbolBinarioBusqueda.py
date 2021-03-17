from jerarquico.nodoArbolBinario import NodoArbolBinario


class ArbolBinarioBusqueda:
    """
    Implementacion de la estructura de datos llamada Arbol Binario
    de Busqueda
    """
    def __init__(self):
        """Método constructor de la clase ArbolBinarioBusqueda(ABB)
        """

        self.raiz = None

    def adicionar(self, nueva_clave):
        """Método que llama a un método recursivo para que realice 
        la función de adicionar nodos con su correspondiente clave 
        al ABB. 

        Se evalúa la homogeneidad con los nodos posteriores al 
        primero.

        Los nodos se van añadiendo según dos posibles casos:
            
            1. Si la clave del nuevo nodo es menor que la clave
            del sub_arbol, el nodo es añadido por izquierda,
            es decir, al sub_arbol.izq

            2. Si la clave del nuevo nodo es mayor que la clave
            del sub_arbol, el nodo es añadido por derecha, 
            es decir, al sub_arbol.der     

        Args:
            nueva_clave (Object): Dato que se almacena en el nodo
        """
        
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        else:
            if type(nueva_clave) == type(sub_arbol.clave):
                if nueva_clave < sub_arbol.clave:
                    sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
                elif nueva_clave > sub_arbol.clave:
                    sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)    
        return sub_arbol    

    def buscar(self, clave_buscar):
        """Método que llama a un método recursivo para que realice
        la función de buscar un nodo del ABB por su dato

        Args:
            clave_buscar (Object): Dato a buscar

        Returns:
            Object: El dato del nodo, si encuentra el dato
            NoneType: None, si no encuentra el dato
        """

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

    def buscar_minimo(self):
        """Método que llama a un método recursivo para que realice
        la función de buscar un nodo del ABB por su dato. Retornará 
        el dato con menor valor del ABB

        Returns:
            Object: Dato con el menor valor del ABB
            NoneType: None, si el árbol está vacío
        """

        return self.__buscar_minimo(self.raiz)

    def __buscar_minimo(self, sub_arbol):
        if sub_arbol is not None:
            if sub_arbol.izq is not None:
                return self.__buscar_minimo(sub_arbol.izq)                 
            return sub_arbol.clave
        return None

    def buscar_maximo(self):
        """Método que llama a un método recursivo para que realice
        la función de buscar un nodo del ABB por su dato. Retornará 
        el dato con mayor valor del ABB

        Returns:
            Object: Dato con el mayor valor del ABB
            NoneType: None, si el árbol está vacío 
        """

        return self.__buscar_maximo(self.raiz)

    def __buscar_maximo(self, sub_arbol):
        if sub_arbol is not None:
            if sub_arbol.der is not None:
                return self.__buscar_maximo(sub_arbol.der)                 
            return sub_arbol.clave
        return None

    def __len__(self):
        """Método que llama a un método recursivo para que realice
        la función de calcular la cantidad de nodos del ABB y 
        retornar dicha cantidad

        Returns:
            int: Cantidad de nodos del ABB
        """

        return self.__numero_nodos(self.raiz)     

    def __numero_nodos(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + 
                self.__numero_nodos(sub_arbol.izq) +
                self.__numero_nodos(sub_arbol.der))
        return 0

    def hojas(self):
        """Método que llama a un método recursivo para que realice
        la función de calcular la cantidad de nodos hojas (Nodos que 
        no tienen hijos) del ABB y retornar dicha cantidad

        Returns:
            int: Cantidad de nodos hijos del ABB
        """

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
        """Método que llama a un método recursivo para que realice
        la función de calcular la cantidad de nodos internos (Nodos 
        que tienen por lo menos un hijo) del ABB y retornar dicha 
        cantidad

        Returns:
            int: Cantidad de nodos internos del ABB
        """

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
        """Método que llama a un método recursivo para que realice
        la función de calcular la cantidad de nodos que van desde
        el nodo raíz hasta la hoja más profunda bajo él

        Returns:
            int: Cantidad que refleja la altura del árbol
        """

        return self.__altura(self.raiz)

    def __altura(self, sub_arbol):
        if sub_arbol is None:
            return 0
        else:
            return (1 + max(self.__altura(sub_arbol.izq), self.__altura(sub_arbol.der)))        

    def borrar(self, clave_borrar):
        """Método que llama a un método recursivo para que realice
        la función de buscar y reemplazar el nodo a borrar por el 
        Mayor de los menores.

        Mayor de los menores: Es el nodo con mayor valor de la rama
        izquierda del nodo el cual se va a borrar 

        Args:
            clave_borrar (Object): Dato que se va a borrar
        """

        return self.__borrar(self.raiz, clave_borrar)

    def __borrar(self, sub_arbol, clave_borrar):
        if sub_arbol is None:
            return None
        elif clave_borrar == self.raiz.clave and (sub_arbol.izq is None or sub_arbol.der is None):
            if sub_arbol.izq is None and sub_arbol.der is None:
                self.raiz = None
                return sub_arbol
            elif sub_arbol.izq is None or sub_arbol.der is not None:
                self.raiz = sub_arbol.der
                return sub_arbol
            elif sub_arbol.izq is not None or sub_arbol.der is None:
                a = self.__buscar_maximo(sub_arbol.izq)
                self.__borrar(sub_arbol, a)
                self.raiz.clave = a
        elif clave_borrar < sub_arbol.clave:
            nodo_izq = self.__borrar(sub_arbol.izq, clave_borrar)
            sub_arbol.izq = nodo_izq
        elif clave_borrar > sub_arbol.clave:
            nodo_der = self.__borrar(sub_arbol.der, clave_borrar)
            sub_arbol.der = nodo_der
        else:
            nodo_aux = sub_arbol
            if nodo_aux.der is None:
                sub_arbol = nodo_aux.izq
            elif nodo_aux.izq is None:
                sub_arbol = nodo_aux.der
            else:
                nodo_aux = self.__reemplazar(nodo_aux)
            nodo_aux = None
        return sub_arbol

    def __reemplazar(self, sub_arbol):
        """Método privado que su función es la de reemplazar el 
        nodo a borrar por el Mayor de los menores 

        Args:
            sub_arbol (Object): Nodo que se va a reemplazar

        Returns:
            Object: Nodo que reemplaza  
        """

        nodo_aux = sub_arbol
        nodo_aux_izq = sub_arbol.izq
        while(nodo_aux_izq.der is not None):
            nodo_aux = nodo_aux_izq
            nodo_aux_izq = nodo_aux_izq.der
        sub_arbol.clave = nodo_aux_izq.clave
        if(nodo_aux == sub_arbol):
            nodo_aux.izq = nodo_aux_izq.izq
        else:
            nodo_aux.der = nodo_aux_izq.izq
        return nodo_aux_izq