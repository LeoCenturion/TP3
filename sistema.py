Esto a continuacion tranquilamente puede pertenecer a una clase llamada Sistema y metes todo el funcionamiento
del programa ahí adentro, así evitas tener multiples funciones. dejo un pseudo código
def graficar_rutas():

		coordenadas, distancia = obtener camino_optimo(idf)
		f = open( 'ruta_' + idciudad1 + '_' + id_ciudad2 + '.kml', 'w')
		f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		f.write("<Document>\n")
		f.write("	<name> EJEMPLO </name>\n").
		f.write("		<Placemark>\n")
		linea = "			<name> UBICACION 1 </name>\n".format(nombre ciudad 1)"
		f.write(linea)
		f.write("			<Point>\n")
		f.write("				<coordinates> COORDENADAS-UBICACION-1 </coordinates\n")
		f.write("			</Point>\n")
		f.write("		</Placemark>\n")

		f.write("		<Placemark>\n")
		linea = "			<name> UBICACION 2 </name>\n".format(nombre ciudad 1)"
		f.write(linea)
		f.write("			<Point>\n")
		f.write("				<coordinates> COORDENADAS-UBICACION-2 </coordinates\n")
		f.write("			</Point>\n")
		f.write("		</Placemark>\n")

		f.write("	<Placemark>\n")
		f.write("		<LineString>\n<coordinates>-58.36795, -34.61763 -58.39644, -34.58850</coordinates>") #COORDENADAS DESDE UN PUNTO A OTRO (REVISAR PDF PARA MAS INFO)
		f.write("		</LineString>\n")
		f.write("	</Placemark>\n")

		f.write("</Document>\n")
		f.write("</kml>\n")
		f.close()

def esribir_kml(grafo,ciudades,tipo):
	"""Recibe un grafo, un diccionario con ciudades, y el tipo de grafo( tendido minimo
	o el mapa completo) y crea un archivo kml con la informacion"""
	if tipo=="mapa":
    	f=open("red.kml","r")
    	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    	f.write("<Document>\n")
    	f.write("	<name> Mapa de todas la ciudades </name>\n")
	else:
    	f=open("tendido.kml","r")
    	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    	f.write("<Document>\n")
    	f.write("	<name> Mapa del tendido electrico </name>\n")
		
    for ciudad in grafo.grafo.keys():
        ciudad_obj=ciudades[ciudad]
        latitud=ciudad_obj.latitud
        longitud=ciudad_obj.longitud
        f.write("		<Placemark>\n")
		f.write("           <name> %s </name>\n",ciudad)
		f.write("			<Point>\n")
		f.write("				<coordinates> %li,%li </coordinates\n",longitud,latitud)
		f.write("			</Point>\n")
		f.write("		</Placemark>\n")
    for ciudad in grafo.grafo.keys():
        for adyacente in grafo.adyacentes(ciudad):
            ciudad_obj=ciudades[ciudad]
            adyacente_obj=ciudades[adyacente]
            longitud_1=ciudad_obj.longitud
            longitud_2=adyacente_obj.longitud
            latitud_1=ciudad_obj.latitud
            latitud_2=adyacente_obj.latitud
            f.write("	<Placemark>\n")
            f.write("      <LineString>\n")
    		f.write("	        <coordinates>%li,%li,%li,%li</coordinates>",longitud_1,latitud_1,longitud_2,latitud_2)
    		f.write("		</LineString>\n")
    		f.write("	</Placemark>\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
    f.close()
