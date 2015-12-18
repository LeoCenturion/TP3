''' para promediar que camino conectar energia electrica
	el criterio que yó personalmente tomaria es cuanta cantidad de gente
	es favorecida con esto + el largo de la ruta.
	La idea es conseguir largos de ruta mas cortos pero con varias poblaciones.
	'''
import csv
import ciudades

def cargar_ciudades(archivo_ciudades):
	"""recibe el nombre del archivo de ciudades y devuelve un dict que tiene
	como clave el nombre de la ciudad y como valor un objeto ciudad con los
	correspondientes datos. O(n)"""
	with open(archivo_ciudades) as archivo:
			archivo_csv = csv.reader(archivo)
			ciudades = {}
			for id, nombre, long, lat, prov, hab in archivo_csv:
				ciudad = CIUDAD(id, nombre, long, lat, prov, hab)
				ciudades[ciudad.nombre]=ciudad

	return ciudades

def cargar_rutas(archivo_rutas):
	"""recibe el nombre del archivo de rutas y devuelve una lista con objetos de
	tipo ruta. O(n)"""
	with open(archivo_rutas) as archivo:
		archivo_csv = csv.reader(archivo)
		rutas=[]
		for	id_ciudad_1, id_ciudad_2 ,puntaje ,distancia in archivo_csv:
			ruta = Ruta(id_ciudad_1, id_ciudad_2, puntaje, distancia)
			rutas.append(ruta)
	return rutas
def main(void):
	archivo_rutas=raw_input("Ingrese el archivo de rutas: ")
	acrhivo_ciudades=raw_input("Ingrese el archivo de ciudades: ")

	rutas=cargar_rutas(archivo_rutas)
	ciudades=cargar_ciudades(archivo_ciudades)
	mapa=crear_mapa(ciudades,rutas[:])
	escribir_kml(grafo,ciudades,"mapa")
	red_electrica=mapa.prim(ciudades.keys()[0])
	escribir_kml(red_electrica,ciudades,"tendido")

	ciudad_1=raw_input("Ingrese el id de la ciudad inicial: ")
	ciudad_2=raw_input("Igrese el id de la ciudad destino: ")

	ruta=mapa.camino_optimo(ciudad_1,ciudad_2)
	escribir_kml(ruta)

	# https://en.wikipedia.org/wiki/Haversine_formula La fórmula para calcular la distancia entre 2 puntos, va a servir demasiado.
	# ó , ( x² + y² )^0.5
