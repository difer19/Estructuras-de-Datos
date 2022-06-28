from jerarquico.arbolAVL import ArbolAVL
from jerarquico.recorridos import *
import networkx as nx



graph = nx.DiGraph()
graph.add_node("Roma")
graph.add_node("Milan")
graph.add_node("Lyon")
graph.add_node("Toulouse")
graph.add_node("Madrid")

graph.add_edge("Roma", "Milan", 605)
graph.add_edge("Roma", "Lyon", 962)
graph.add_edge("Roma", "Toulouse", 1131)
graph.add_edge("Milan", "Toulouse", 800)
graph.add_edge("Milan", "Madrid", 1482)
graph.add_edge("Lyon", "Milan", 449)
graph.add_edge("Lyon", "Madrid", 1099)
graph.add_edge("Toulouse", "Madrid", 692)



print(nx.dijkstra_path(graph, "Madrid", "Roma"))





# myTree = ArbolAVL()
# myTree.insertar(1)
# myTree.insertar(2)
# myTree.insertar(3)
# preorden(myTree)
# print("--------------------")
# print(myTree.buscar(15))
# print("--------------------")
# print(len(myTree))
# print("--------------------")
# print(myTree.internos())
# print("--------------------")
# print(myTree.altura())
# print("--------------------")
# myTree.eliminar(1)
# preorden(myTree)

 