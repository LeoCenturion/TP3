import grafo
import math
#d = π * r / 90 * arc sen ( sqrt ( sen^2 (( φ2 – φ1)/2) + cos φ2 * cos φ1 * sen^2 ((λ2 – λ1)/2))
def haversine(ciudad_a,ciudad_b):
	R=6351 #radio de la tierra
	latitud_a=ciudad_a.latitud()
	latitud_b=ciudad_b.latitud()
	dLongitud=ciudad_b.longitud()-ciudad_a.longitud()
	dLatitud=ciudad_b.latitud()-ciudad_a.latitud()
	aux = 2*R*math.asin(math.sqrt(math.sqrt(math.sin(dLatitud))+math.cos(latitud_a)*math.cos(latitud_b)*math.sqrt(math.sin(dLatitud/2))))
	return aux
class Ciudad:
	def __init__(self, id, nombre, longitud, latitud, provincia, habitantes):
		self.id=id
		self.nombre = nombre
		self.coordenadas=(latitud,longitud)
		self.provincia = provincia
		self.habitantes = habitantes
		self.mapa = GRAFO()
		self.conectada=False

	def nombre(self):
		return self.nombre
	def longitud(self):
		return self.coordenadas[1]
	def latitud(self):
		return self.coordenadas[0]
	def coordenadas(self):
		return self.coordenadas
	def provincia(self):
		return self.provincia
	def habitantes(self):
		return self.habitantes


class Ruta:
	def __init_(self,ciudad_a,ciudad_b,puntaje,distancia):
		self.distancia=distancia
		self.ciudades_unidas=(ciudad_a,ciudad_b)
		self.puntaje=puntaje
	def ciudades_unidas(self):
		return self.ciudades_unidas
	def distancia(self):
		return self.distancia
	def puntaje(self):
		return self.puntaje
	def __cmp__(self,otro):
		"""compara las rutas segun el putaje de las ciudades que une.
		 No se toma en cuenta la distancia porque la
		consigna asegura un presupuesto ilimitado"""
		return self.puntaje()-otro.puntaje()
