from graphviz import Digraph

class Nodo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.transiciones = []  # Lista de transiciones (conexiones a otros nodos)

    def agregar_transicion(self, destino, simbolo):
        """
        Agrega una transición desde este nodo hacia otro.
        """
        self.transiciones.append((simbolo, destino))


class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario de nodos (nombre -> Nodo)
        self.estado_inicial = None
        self.estado_final = None

    def agregar_nodo(self, nombre):
        """
        Agrega un nodo al grafo, si no existe ya.
        """
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)
        return self.nodos[nombre]

    def conectar(self, origen, destino, simbolo):
        """
        Crea una transición desde un nodo de origen hacia uno de destino.
        """
        if origen not in self.nodos or destino not in self.nodos:
            raise ValueError("El nodo de origen o destino no existe.")
        self.nodos[origen].agregar_transicion(self.nodos[destino], simbolo)

    def set_estado_inicial(self, nombre):
        """
        Establece el estado inicial del grafo.
        """
        self.estado_inicial = self.agregar_nodo(nombre)

    def set_estado_final(self, nombre):
        """
        Establece el estado final del grafo.
        """
        self.estado_final = self.agregar_nodo(nombre)

    def mostrar(self):
        """
        Muestra las transiciones del grafo.
        """
        for nombre, nodo in self.nodos.items():
            for simbolo, destino in nodo.transiciones:
                print(f"{nombre} --{simbolo}--> {destino.nombre}")
    

    def visualizar(self):
        """
        Genera una representación visual del grafo utilizando graphviz.
        """
        dot = Digraph()
        dot.attr(rankdir="LR")

        # Estado inicial
        if self.estado_inicial:
            dot.node("", shape="none")
            dot.edge("", str(self.estado_inicial.nombre))

        # Agregar nodos
        for nombre, nodo in self.nodos.items():
            if nodo == self.estado_final:
                dot.node(str(nombre), shape="doublecircle")
            else:
                dot.node(str(nombre), shape="circle")

        # Agregar transiciones
        for nombre, nodo in self.nodos.items():
            for simbolo, destino in nodo.transiciones:
                dot.edge(str(nombre), str(destino.nombre), label=simbolo)

        return dot
