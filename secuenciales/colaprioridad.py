from ed.secuenciales.listaSE import ListaSE
from ed.secuenciales.cola import Cola
from ed.secuenciales.iterador_ListaSE import Iterador_ListaSE


class ItemColadeprioridad:
    """
    Clase que representa un item para una cola de
    prioridad
    """
    def __init__(self, dato, prioridad):
        """Metodo Constructor de la clase que representa
        un item de una cola de prioridad
        
        Args:
            dato (Object): [Elemento que representa el dato a almacenar]
            prioridad (int): [entero que representa la prioridad del
            elemento, va desde 1 a n ]
        """
        self.dato = dato
        self.prioridad = prioridad

    def __str__(self):
        """Metodo que retorna una cadena que representa el dato guardado
        
        Returns:
            [str]: [Cadena con la presentacion del dato]
        """
        return str(self.dato)

class Colaprioridad:
    """
    Clase que representa la estructura de datos llamada
    cola de prioridad usando como base una lista de colas
    """
    def __init__(self):
        self.Listp = ListaSE()
        self.d_href = None 
    
    def encolar(self, nuevo_dato, prioridad):
        """Metodo que adiciona un elemento al extremo final
        de una cola segun su prioridad

        Args:
            nuevo_dato (Object): [Dato a encolar]
            prioridad (int): [Entero que representa la prioridad
            del dato]

        Returns:
            [bool]: [True si el dato se pudo encolar, False en caso
            contrario]
        """
        if type(prioridad) is not int:
            return False
        if prioridad < 0:
            return False
        if self.Listp.es_vacia():
            c = Cola()
            I = ItemColadeprioridad(nuevo_dato, prioridad)
            c.encolar(I)
            self.d_href = nuevo_dato
            return(self.Listp.adicionar(c))
        elif type(nuevo_dato) is type(self.d_href):
            flag = 0
            for a in self.Listp:
                if a.frente().dato.prioridad == prioridad:
                    I = ItemColadeprioridad(nuevo_dato, prioridad)
                    a.encolar(I)
                    return True
            if flag == 0:
                c = Cola()
                I = ItemColadeprioridad(nuevo_dato, prioridad)
                c.encolar(I)
                self.Listp.adicionar(c)
            return True
        else:
            return False
    
    def desencolar(self):
        """Metodo que sacara el frente de la cola con la prioridad
        mas baja y lo retornara
        
        Returns:
            [Object]: [Dato del frente si existe al menos un elemento, None
            si la cola de prioridad esta vacia]
        """
        if self.Listp.es_vacia():
            return None
        else:
            it = 0
            pri = 0
            des = None
            for a in self.Listp:
                if it == 0:
                    pri = a.frente().dato.prioridad
                    it = 1
                else:
                    if pri > a.frente().dato.prioridad:
                        pri = a.frente().dato.prioridad
            for a in self.Listp:
                if a.frente().dato.prioridad == pri:
                    des = a.desencolar()
                    if a.es_vacia() is True:
                        self.Listp.borrar(a, False)
                    break
            if self.Listp.es_vacia():
                self.d_href = None
            return des

    def frente(self):
        """Metodo que retornara el frente de la cola con la
        prioridad mas baja sin sacarlo

        Returns:
            [Object]: [Elemento que esta en el frente de la 
            cola de prioridad]
        """
        if self.Listp.es_vacia():
            return None
        else:
            it = 0
            pri = 0
            for a in self.Listp:
                if it == 0:
                    pri = a.frente().dato.prioridad
                    it = 1
                else:
                    if pri > a.frente().dato.prioridad:
                        pri = a.frente().dato.prioridad
            for a in self.Listp:
                if a.frente().dato.prioridad == pri:
                    return a.frente().dato
    
    def __len__(self):
        """Metodo que retorna la cantidad de elementos en la
        cola de prioridad

        Returns:
            [int]: [Cantidad de datos de la cola de prioridad]
        """
        size = 0
        for a in self.Listp:
            size += len(a)
        return size
    
    def es_vacia(self):
        """Metodo que identifica si la cola de prioridad esta
        vacia

        Returns:
            [bool]: [True si la cola esta vacia, False en caso
            contrario]
        """
        if len(self) == 0:
            return True
        else:
            return False
    
    def __iter__(self):
        """Metodo que retorna el iterador de la cola de prioridad
        en orden de prioridad, para generar el iterador se utiliza
        el iterador de una lista simplemente enlazada.

        Returns:
            [Iterador_ListaSE]: [Iterador de la cola de prioridad]
        """
        ListI = ListaSE()
        ListD = ListaSE()
        pri = 0
        it = 0
        for a in self.Listp:
            nodo_actual = a.nodo_cab
            while nodo_actual is not None:
                v = nodo_actual.dato
                ListI.adicionar(v)
                nodo_actual = nodo_actual.sig
        for b in ListI:
            if it == 0:
                pri = b.prioridad
                it = 1
            elif b.prioridad > pri:
                pri = b.prioridad
        sel = 1
        while sel <= pri:
            for c in ListI:
                if c.prioridad == sel:
                    ListD.adicionar(c)
            sel += 1   
        return Iterador_ListaSE(ListD)
