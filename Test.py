from jerarquico.arbolAVL import ArbolAVL
from jerarquico.recorridos import *


myTree = ArbolAVL()
myTree.insertar(30)
myTree.insertar(20)
myTree.insertar(25)
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
myTree.eliminar(30)
preorden(myTree)

 