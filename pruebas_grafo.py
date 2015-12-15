from grafos import Grafo
import math
import unittest
def visitar(vertice,padre,grafo,visitados):
    peso=0
    if not vertice in visitados:
        visitados.append(vertice)
        peso_total=grafo.obtener_info_arista(vertice,padre)
        for adyacentes in grafo.adyacentes(vertice):
            peso_total+=visitar(adyacente,vertice,grafo,visitados)
    return peso_total
def contar_pesos(grafo,vertices):
    peso_total=0;
    visitados=[]
    for vertice in vertices:
        if not  vertice in visitados:
            peso_total=visitar(vertice)

class PruebaGrafo(unittest.TestCase):
    def test_grafo_vacio(self):
        grafo=Grafo()
        vertice1="vertice1"
        vertice2="vertice2"
        self.assertFalse(grafo.pertenece_vertice(vertice1))
        self.assertFalse(grafo.existe_arista(vertice1,vertice2))
        self.assertTrue(grafo.obtener_info_arista(vertice1,vertice2)==float("inf"))
        #self.assertRaises(LookupError,grafo.borrar_arista(vertice1,vertice2))
        with self.assertRaises(LookupError):
            grafo.borrar_arista(vertice1,vertice2)
    def test_grafo_agregar_vertices(self):
        grafo=Grafo()
        vertices=[]
        pesos=range(20)
        for i in xrange(0,10):
            vertices.append(str(i))
            grafo.agregar_vertice(vertices[i])
        for i in xrange(10):
            self.assertTrue(grafo.pertenece_vertice(vertices[i]))
        for i in range(9,-1,-1):
            grafo.borrar_vertice(vertices[i])
            self.assertTrue(grafo.cant_vertices()==i)
            self.assertFalse(grafo.pertenece_vertice(vertices[i]))
        self.assertTrue(grafo.cant_vertices()==0)
    def test_grafo_agregar_aristas(self):
        grafo=Grafo()
        vertices=[]
        pesos=range(20)
        for i in xrange(0,10):
            vertices.append(str(i))
            grafo.agregar_vertice(vertices[i])
        for i in xrange(10):
            self.assertTrue(grafo.pertenece_vertice(vertices[i]))
        for i in range(10):
            for j in range(10):
                grafo.agregar_arista(vertices[i],vertices[j],pesos[j],str(i+j))
                self.assertTrue(grafo.cant_aristas()==10*(i)+j+1)
                self.assertTrue(grafo.existe_arista(vertices[i],vertices[j]))
                self.assertTrue(grafo.obtener_info_arista(vertices[i],vertices[j])==pesos[j])
        self.assertTrue(grafo.cant_aristas()==100)
    def test_prim(self):
        grafo=Grafo()
        vertices=["uno","dos","tres","cuatro","cinco"]
        for vertice in vertices:
            grafo.agregar_vertice(vertice)
        for i in range(3):
            grafo.agregar_arista(vertices[4],vertices[i],1,str(i))
        for i in range(2):
            grafo.agregar_arista(vertices[i],vertices[i+1],i+1,str(i))
        tendido_minimo=grafo.prim(vertices[0])
        self.assertTrue(tendido_minimo.cant_vertices()==5)
        self.assertTrue(tendido_minimo.cant_aristas()==5)
        self.assertTrue(contar_pesos(tendido_minimo,vertices)==4)




if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PruebaGrafo)
    unittest.TextTestRunner(verbosity=2).run(suite)
