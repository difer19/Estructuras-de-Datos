from jerarquico.arbolAVL import ArbolAVL
from jerarquico.recorridos import *


myTree = ArbolAVL()
myTree.insertar(1)
myTree.insertar(2)
myTree.insertar(3)
preorden(myTree)
print("--------------------")
print(myTree.buscar(15))
print("--------------------")
print(len(myTree))
print("--------------------")
print(myTree.internos())
print("--------------------")
print(myTree.altura())
print("--------------------")
myTree.eliminar(1)
preorden(myTree)

 