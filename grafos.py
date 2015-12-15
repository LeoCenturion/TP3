#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from heapq import heappush, heappop,heapify
class vertice:
	def __init__(self,nombre):
		self.nombre=nombre
		self.padre=None
		self.adyacentes={}
	def adyacentes(self):
		return self.adyacentes
	def padre(self):
		return self.padre
	def vertice_pertenece(vertice,aristas):
		ok=False
		for i in xrange(aristas.len()):
			if(vertice==aristas[i][0]):
				ok=True
				break
		return ok
class Arista:
	def __init__(self,vertice,peso):
		self.arista=(vertice,peso)
	def __cmp__(self,otro):
		return self.arista[1]-otro.arista[1]
	def peso(self):
		return self.arista[1]
	def vertice(self):
		return self.arista[0]


class Grafo:
	peso_arista = 0
	nombre_arista = 1
	def __init__( self ):
		'''Inicializacion del grafo'''
		self.grafo = { }
		self.vertices=0
		self.aristas=0
	def cant_vertices(self):
		return self.vertices
	def cant_aristas(self):
		return self.aristas
	def imprimir_vertices( self ):
		''' Imprime toda la arista '''
		for w in self.grafo.keys():
			print('{}:{}\n'.format(w, self.grafo[ w ] ))

	def pertenece_vertice( self , vertice ):
		''' Dado un vertice devolvera true o false en caso de que pertenezca o no '''
		return ( vertice in self.grafo.keys( ) )

	def agregar_vertice( self, vertice ):
		''' Crea un nuevo vertice en un grafo '''
		self.grafo[ vertice ] = { }
		self.vertices+=1

	def agregar_arista(self, vertice1, vertice2, peso, nombre ):
		''' conectamos vertice 1 con vertice 2
			asociando a esa conexión su respectivo peso y nombre '''
		if self.pertenece_vertice(vertice1) and self.pertenece_vertice(vertice2):
			self.grafo[ vertice1 ][ vertice2 ] = (peso, nombre)
			self.grafo[ vertice2 ][ vertice1 ] = (peso, nombre)
		self.aristas+=1
		#Comentarios, la idea es que cada diccionario tenga internamente un subdiccionario
		#que contiene la informacion cruzada de la arista la cual la conecta

	def existe_arista(self, vertice1, vertice2):
		''' mas claro imposible, verifica sí 2 vertices estan conectados '''
		try:
			return (vertice1 in self.grafo[vertice2])
		except KeyError:
			return False

	def obtener_info_arista( self, vertice1, vertice2, tipo_de_informacion=0 ):
		''' devolvemos la informacion de la arista deseada
		el parametro tipo_de_informacion denota el tipo de informacion recibida
		== 0 mostramos el peso de la arista
		!= 0 mostramos EL NOMBRE de la arista '''
		nombre_arista=1
		peso_arista=0
		try:
			return self.grafo[ vertice1 ][ vertice2 ][ nombre_arista if tipo_de_informacion else peso_arista ]
		except LookupError:
			return float("inf")

		#return self.grafo[ vertice1 ][ vertice2 ][ nombre_arista if tipo_de_informacion else peso_arista ]

	"""def peso_arista(self,vertice1,vertice2):
		try:
			return self.grafo[ vertice1 ][ vertice2 ][ nombre_arista if tipo_de_informacion else peso_arista ]
		except LookupError:
			return float("inf")"""

	def borrar_arista( self, vertice1, vertice2 ):
		''' debemos borrar la informacion guardada en los vertices
			dados'''
		if self.existe_arista(vertice1, vertice2):
			self.grafo[vertice1].pop( vertice2)
			self.grafo[vertice2].pop( vertice1)
			self.aristas-=1
		else:
			raise LookupError, "Arista inexistente"

		#nota ,no estoy seguro del 100% sí pop es algo eficaz, leí por ahí tambien usar 'del' pero no aseguré nada.

	def borrar_vertice( self, vertice ):
		''' eliminamos el vertice PERO tambien hay que borrar la arista asociada que contiene ! '''
		for arista in self.grafo:
			if self.grafo[arista].has_key(vertice):
				self.grafo[arista].pop(vertice)
		self.grafo.pop(vertice)
		self.vertices-=1



	def adyacentes(self, vertice):
		''' dado un vertice, devolvemos sus adyacentes '''
		if self.pertenece_vertice( vertice ):
			return self.grafo[ vertice ]
		else:
			return None

	def prim(self, inicio):
		pesos_aristas={};
		tendido_minimo=self.__init__()
		for vertice in self.grafo.keys():
			pesos_aristas[vertice]=float("inf");
			tendido_minimo.agregar_vertice(vertice)
		pesos_aristas[inicio]=0
		heap = []
		aristas=[]
		for (vertice,peso) in pesos_aristas.items():
			nueva_arista=Arista(vertice,peso)
			aristas.append(nueva_arista)
		heapify(aristas)
		while len(aristas)!=0:
			arista=aristas.pop(0)
			for adyacente in self.adyacentes(arista.vertice()):
				peso=self.peso_arista(adyacente,arista.vertice())
				if vertice_pertenece(adyacente,aristas) and peso<pesos_aristas[vertice]:
					pesos_aristas[vertice]=peso
					if tendido_minimo.existe_arista(adyacente,arista.vector()):
						tendido_minimo.borrar_arista(adyacente,arista.vector())

				self.agregar_arista(adyacente, arista.vertice(), peso, None )
		return tendido_minimo

	def a_estrella(self, inicio):
		''' http://www.redblobgames.com/pathfinding/a-star/introduction.html '''
		heap = []
		heappush(heap, inicio)
		donde_vienen = {}
		donde_vienen[inicio] = None

		while len(heap):
			actual = heap
