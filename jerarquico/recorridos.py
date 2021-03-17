def preorden(arbol_bin):
    """Método que realiza un print de cada objeto del ABB, en 
    PreOrden, es decir, en el siguiente orden:

    Nodo --> Sub Árbol Izquierdo --> Sub Árbol Derecho

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda   
    """

    __preorden(arbol_bin.raiz)

def __preorden(sub_arbol):
    if sub_arbol is not None:
        print(sub_arbol.clave)
        __preorden(sub_arbol.izq)
        __preorden(sub_arbol.der)
        
def cad_preorden(arbol_bin, sep="^"):
    """Método que retorna una cadena con los objetos del ABB, en 
    PreOrden, utilizando un separador entre ellos. Para el caso del 
    separador por defecto quedaría:
    
    "clave1^clave2^clave3^...claveN"

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda  
        sep (str, optional): Separador que va entre cada uno de los 
            objetos del ABB. Defaults to "^".

    Returns:
        str: Cadena con los objetos del ABB
    """
    cad_final = str(__cad_preorden(arbol_bin.raiz, sep))
    return cad_final.rstrip(sep)

def __cad_preorden(sub_arbol, sep):
    cad_final = ""
    if sub_arbol is not None:
        cad_final += (str(sub_arbol.clave))+sep
        cad_final += (str(__cad_preorden(sub_arbol.izq, sep)))
        cad_final += (str(__cad_preorden(sub_arbol.der, sep)))
    return cad_final

def inorden(arbol_bin):
    """Método que realiza un print de cada objeto del ABB, en 
    InOrden, es decir, en el siguiente orden:

    Sub Árbol Izquierdo --> Nodo --> Sub Árbol Derecho

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda
    """

    __inorden(arbol_bin.raiz)

def __inorden(sub_arbol):
    if sub_arbol is not None:
        __inorden(sub_arbol.izq)
        print(sub_arbol.clave)
        __inorden(sub_arbol.der)

def cad_inorden(arbol_bin, sep="-"):
    """Método que retorna una cadena con los objetos del ABB, en 
    InOrden, utilizando un separador entre ellos. Para el caso del 
    separador por defecto quedaría:
    
    "clave1-clave2-clave3-...claveN"

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda
        sep (str, optional): Separador que va entre cada uno de los 
            objetos del ABB. Defaults to "-".

    Returns:
        str: Cadena con los objetos del ABB
    """

    cad_final = str(__cad_inorder(arbol_bin.raiz, sep))
    return cad_final.rstrip(sep)

def __cad_inorder(sub_arbol, sep):
    cad_final = ""
    if sub_arbol is not None:
        cad_final += (str(__cad_inorder(sub_arbol.izq, sep)))
        cad_final += (str(sub_arbol.clave))+sep
        cad_final += (str(__cad_inorder(sub_arbol.der, sep)))
    return cad_final

def postorden(arbol_bin):
    """Método que realiza un print de cada objeto del ABB, en 
    PostOrden, es decir, en el siguiente orden:

    Sub Árbol Izquierdo --> Sub Árbol Derecho --> Nodo

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda
    """

    __postorden(arbol_bin.raiz)

def __postorden(sub_arbol):
    if sub_arbol is not None:
        __postorden(sub_arbol.izq)
        __postorden(sub_arbol.der)
        print(sub_arbol.clave)

def cad_postorden(arbol_bin, sep="\\"):
    """Método que retorna una cadena con los objetos del ABB, en 
    PostOrden, utilizando un separador entre ellos. Para el caso del 
    separador por defecto quedaría:
    
    "clave1\clave2\clave3\...claveN"

    Args:
        arbol_bin (ABB): Árbol Binario de Búsqueda
        sep (str, optional): Separador que va entre cada uno de los 
            objetos del ABB. Defaults to "\".

    Returns:
        str: Cadena con los objetos del ABB
    """

    cad_final = str(__cad_postorden(arbol_bin.raiz, sep))
    return cad_final.rstrip(sep)

def __cad_postorden(sub_arbol, sep):
    cad_final = ""
    if sub_arbol is not None:
        cad_final += (str(__cad_postorden(sub_arbol.izq, sep)))
        cad_final += (str(__cad_postorden(sub_arbol.der, sep)))
        cad_final += (str(sub_arbol.clave))+sep
    return cad_final