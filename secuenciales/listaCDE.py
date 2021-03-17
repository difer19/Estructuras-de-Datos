from secuenciales.listaDE import NodoDE
from secuenciales.iterador_ListaSE import Iterador_ListaSE
from secuenciales.listaSE import ListaSE

class ListaCDE:
	"""Implementacion de la estructura de datos llamada
	Lista Circular doblemente enlazada
	"""
	def __init__(self):
		"""Metodo constructor de la clase
		"""
		self.nodo_cab = None
		self.nodo_last = None
		self.actual = None
	
	def es_vacia(self):
		"""Metodo con el que podemos saber si la lista
		esta vacia

		Returns:
			[bool]: [True si la lista esta vacia, False
			en caso contrario]
		"""
		return self.nodo_cab is None
	
	def __len__(self):
		"""Metodo que retorna la cantidad de datos que 
		estan en la lista

		Returns:
			[int]: [Cantidad de datos de la lista]
		"""
		counter = 1
		nodo_actual = self.nodo_cab.sig
		while nodo_actual is not self.nodo_cab:
			counter += 1
			nodo_actual = nodo_actual.sig
		return counter
	
	def recorrer(self):
		"""Metodo que recorre la lista e imprime los datos
		"""
		print(self.nodo_cab.dato)
		nodo_actual = self.nodo_cab.sig
		while nodo_actual is not self.nodo_cab:
			print(nodo_actual.dato)
			nodo_actual = nodo_actual.sig

	def adicionar(self, nuevo_dato):
		"""Metodo que adiciona un dato al final de la lista

		Args:
			nuevo_dato (Object): [Dato que se va a adicionar
			en la lista]

		Returns:
			[bool]: [True si el dato se pudo adicionar, False
			caso contrario]
		"""
		if self.es_vacia():
			self.nodo_cab = self.nodo_last = NodoDE(nuevo_dato)
			self.actual = self.nodo_cab
			return True
		elif type(self.nodo_cab.dato) == type(nuevo_dato):
			aux = self.nodo_last
			nuevo_nodo = NodoDE(nuevo_dato)
			self.nodo_last = nuevo_nodo
			self.nodo_last.ant = aux
			aux.sig = self.nodo_last
			self.nodo_last.sig = self.nodo_cab
			self.nodo_cab.ant = self.nodo_last
			return True
		return False
	
	def buscar(self, dato_buscar):
		"""Metodo que busca un dato dentro de la lista

		Args:
			dato_buscar (Object): [Dato a buscar]

		Returns:
			[Object]: [El dato si se pudo encontrar, None
			en caso contrario]
		"""
		if type(dato_buscar) != type(self.nodo_cab.dato):
			return None
		elif dato_buscar == self.nodo_cab.dato:
			return self.nodo_cab.dato
		else:
			nodo_actual = self.nodo_cab.sig
			while nodo_actual is not self.nodo_cab:
				if dato_buscar == nodo_actual.dato:
					return nodo_actual.dato
				nodo_actual = nodo_actual.sig
		return None

	def borrar(self, item, por_pos = True):
		"""Metodo que elimina un dato de la lista, la eliminacion se
		hace por posicion o por dato, si la eliminacion se hace por
		dato se eliminaran todas las coincidencias

		Args:
			item (int o Object): [posicion a eliminar o dato a eliminar]
			por_pos (bool, optional): [True si la eliminacion se hace por
			posicion, False si se hace por dato]. Defaults to True.

		Returns:
			[bool]: [True si se pudo eliminar, False en caso contrario]
		"""
		if por_pos:
			if type(item) != int and item < 0:
				return False
			counter = 0
			nodo_actual = self.nodo_cab
			while counter < item:
				nodo_actual = nodo_actual.sig
				counter += 1
			if nodo_actual is self.nodo_cab:
				self.nodo_cab = self.nodo_cab.sig
				self.nodo_cab.ant = self.nodo_last
				self.nodo_last.sig = self.nodo_cab
				return True
			elif nodo_actual == self.nodo_last:
				self.nodo_last = self.nodo_last.ant
				self.nodo_last.sig = self.nodo_cab
				self.nodo_cab.ant = self.nodo_last
				return True
			else:
				counter = 1
				nodo_actual = self.nodo_cab.sig
				while counter < item:
					nodo_actual = nodo_actual.sig
					counter += 1
				nodo_actual.ant.sig = nodo_actual.sig
				nodo_actual.sig.ant = nodo_actual.ant
				return True
		else:
			counter = 0
			flag = 0
			for i in self:
				if i == item:
					self.borrar(counter - flag)
					flag += 1
				counter += 1
			if flag == 0:
				return False
			else:
				return True
	
	def __iter__(self):
		"""Metodo que retorna el iterador de la listaCDE

		Returns:
			[iter]: [Iterador de la lista]
		"""
		ListaS = ListaSE()
		ListaS.adicionar(self.nodo_cab.dato)
		nodo_actual = self.nodo_cab.sig
		while nodo_actual is not self.nodo_cab:
			ListaS.adicionar(nodo_actual.dato)
			nodo_actual = nodo_actual.sig
		return Iterador_ListaSE(ListaS)

	def __str__(self):
		"""Metodo que retorna un str de presentacion con
		los datos de la lista

		Returns:
			[str]: [str de presentacion de la lista]
		"""
		a = ""
		counter = 0
		for dato in self:
			if counter == 0:
				a += "<="+str(dato)
			elif counter == len(self) - 1:
				a += "<=>"+str(dato)+"=>"
			else:
				a += "<=>"+str(dato)
			counter += 1
		return a
	
	def insertar(self, pos, nuevo_dato):
		"""Metodo que permite insertar un dato en una posicion
		dentro de la lista

		Args:
			pos (int): [Posicion en la que se va insertar el dato]
			nuevo_dato (Object): [Dato a insertar]

		Returns:
			[bool]: [True si el dato se pudo insertar, False en caso
			contrario]
		"""
		if type(pos) != int and pos < 0 and type(nuevo_dato) != type(self.nodo_cab.dato):
			return False
		counter = 0
		nodo_actual = self.nodo_cab
		while counter < pos:
			nodo_actual = nodo_actual.sig
			counter += 1
		if nodo_actual is self.nodo_cab:
			aux = self.nodo_cab
			self.nodo_cab = NodoDE(nuevo_dato)
			self.nodo_cab.sig = aux
			self.nodo_cab.ant = self.nodo_last
			self.nodo_last.sig = self.nodo_cab
			return True
		elif nodo_actual == self.nodo_last:
			nuevo_nodo = NodoDE(nuevo_dato)
			self.nodo_last.ant.sig = nuevo_nodo
			nuevo_nodo.ant = self.nodo_last.ant
			nuevo_nodo.sig = self.nodo_last
			self.nodo_last.ant = nuevo_nodo
			return True
		else:
			nuevo_nodo = NodoDE(nuevo_dato)
			nodo_actual.ant.sig = nuevo_nodo
			nuevo_nodo.ant = nodo_actual.ant
			nuevo_nodo.sig = nodo_actual
			nodo_actual.ant = nuevo_nodo
			return True
	
	def adelante(self):
		"""Metodo que permite recorrer la lista nodo por nodo
        hacia adelante

		Returns:
			[Object]: [nodo siguiente al original]
		"""
		if self.es_vacia():
			return None
		else:
			self.actual = self.actual.sig
			return self.actual

	def atras(self):
		"""Metodo que permite recorrer la lista nodo por nodo
        hacia atras

		Returns:
			[Object]: [nodo anterior al original]
		"""
		if self.es_vacia():
			return None
		else:
			self.actual = self.actual.ant
			return self.actual