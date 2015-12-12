import sys

import heapq

class GRAFOS:
	peso_arista = 0
	nombre_arista = 1
	def __init__( self ):
		'''Inicializacion del grafo'''
		self.grafo = { }
			
	def imprimir_vertices( self ):
		''' Imprime toda la arista '''
		for w in self.grafo.keys():
			print('{}:{}\n'.format(w, self.grafo[ w ] ))
	
	def pertenece_vertice( self , vertice ):
		''' Dado un vertice devolvera true o false en caso de que pertenezca o no '''
		return ( v in self.matriz.keys( ) )
	
	def agregar_vertice( self, vertice ):
		''' Crea un nuevo vertice en un grafo '''
		self.grafo[ vertice ] = { }
	
	def agregar_arista(self, vertice1, vertice2, peso, nombre )
		''' conectamos vertice 1 con vertice 2
			asociando a esa conexión su respectivo peso y nombre '''
		if pertenece_vertice( self, vertice1 ) and pertenece_vertice( self, vertice2 ):
			self.grafo[ vertice1 ][ vertice2 ] = (peso, nombre)
			self.grafo[ vertice2 ][ vertice1 ] = (peso, nombre)
			
			
		#Comentarios, la idea es que cada diccionario tenga internamente un subdiccionario
		#que contiene la información cruzada de la arista la cual la conecta
	
	def obtener_info_arista( self, vertice1, vertice2, tipo_de_informacion=0 )
		''' devolvemos la informacion de la arista deseada
		el parametro tipo_de_informacion denota el tipo de informacion recibida
		== 0 mostramos el peso de la arista
		!= 0 mostramos EL NOMBRE de la arista '''
		return self.grafo[ vertice1 ][ vertice2 ][ nombre_arista if tipo_de_informacion else peso_arista ]
		
	def borrar_arista( self, vertice1, vertice2 )
		''' debemos borrar la informacion guardada en los vertices
			dados'''
		if self.existe_arista(vertice1, vertice2):
			self.grafo.pop( vertice1, None )
			self.grafo.pop( vertice2, None )
		
		#nota ,no estoy seguro del 100% sí pop es algo eficaz, leí por ahí tambien usar 'del' pero no aseguré nada.
		
	def borrar_vertice( self, vertice )
		''' eliminamos el vertice PERO tambien hay que borrar la arista asociada que contiene ! '''
		for aristas in self.grafo.keys( ):
			if aristas.has_key( vertice ):
				aristas.pop(vertice, None)
		
		self.grafos.pop(vertice, None)
	
	def existe_arista(self, vertice1, vertice2)
		''' mas claro imposible, verifica sí 2 vertices estan conectados '''
		return (vertice1 in self.grafos[ vertice2 ])
	
	def obtener_adyacentes(self, vertice)
		''' dado un vertice, devolvemos sus adyacentes '''
		if self.pertenece_vertice( vertice )
			return self.grafos[ vertice ]
		else
			return None
		
	def algoritmo_prim(self, inicio):
		pesos_aristas = dict( [ (aristas, sys.maxint) for aristas in self.grafos.keys( ) ] )
		pesos_aristas[ inicio ] = 0
		
		heap = [ ]
		
		heappush(heap, (aristas, peso_aristas[aristas]) for aristas in self.grafos.keys( ) ] )
		
		while len(heap):
			actual_vertice = heap[0]
			
			for vertices_siguientes in obtener_adyacentes(self, actual_vertice):
				peso = pesos_aristas[actual_vertice]
			
				if vertices_siguientes in heap and peso < pesos_aristas[vertices_siguientes]
					pesos_aritas[vertices_siguientes] = peso
					heappop(vertices_siguientes, peso)
					
	def algoritmo_a_estrella(self, inicio):
		''' http://www.redblobgames.com/pathfinding/a-star/introduction.html '''
		'''heap = []
		heappush(heap, inicio)
		donde_vienen = {}
		donde_vienen[inicio] = None
		
		while len(heap):
			actual = heap'''
			
