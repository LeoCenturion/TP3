import grafo
import sys
from heap import heapify

def ciudades_sin_conectar(grafo):
    """verifica si existen ciudades sin conectar en el grafo y, de ser
    verdadero, crea un diccionario que tiene como claves los nombres de
    las ciudades aisladas. O(V)"""
    aisladas={}
    for ciudad in grafo.grafo.keys():
        adyacentes=grafo.adyacentes(ciudad)
        if len(adyacentes)==0:
            aisladas[ciudad_1]=None
    return aisladas

def conectar_ciudades_restantes(grafo,rutas,aisladas):
    for i in range(len(rutas)/2 + 1):
        ciudad_1=rutas[i].ciudades_unidas[0]
        ciudad_2=rutas[i].ciudades_unidas[1]
        if ciudad_1 in aisladas or ciudad_2 in aisladas:
            grafo.agregar_arista(ciudad_1,ciudad_2)
            if ciudad_1 in aisladas:
                aisladas.pop(ciudad_1)
            if ciudad_2 in aisladas:
                aisladas.pop(ciudad_2)

def crear_mapa(ciudades,rutas,ciudades):
    "crea y devuelve un grafo con las ciudades unidas por las rutas"
    mapa=Grafo()
    for ciudad in ciudades.keys():
        grafo.agregar_vertice(ciudad)
    sort(rutas) #tal que la ruta mayor quede al principio
    for i in range(len/2):
        ruta=rutas[i]
        ciudad_1=ruta.ciudades_unidas[0]
        ciudad_2=ruta.ciudades_unidas[1]
        peso=ruta.puntaje
        mapa.agregar_arista(ciudad_1,ciudad_2,puntaje)
    aisladas=ciudad_sin_conectar(grafo)
    if len(aisladas)!=0:
        conectar_ciudades_restantes(grafo,rutas,aisladas)
