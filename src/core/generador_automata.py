from .automata import Grafo
class GeneradorDeAutomatas:

    def construir_grafo_desde_tokens(self, tokens):
        """
        Construye un grafo dirigido desde una lista de tokens.
        En cada iteración se crean dos nodos y la conexión entre ellos.
        """
        grafo = Grafo()

        for i, (tipo, valor) in enumerate(tokens):
            if tipo == 'LITERAL':
                # Crear dos nodos: uno actual y uno siguiente
                estado_actual = f"q{i}"         # Nodo actual
                estado_siguiente = f"q{i+1}"   # Nodo siguiente

                # Agregar ambos nodos al grafo
                grafo.agregar_nodo(estado_actual)
                grafo.agregar_nodo(estado_siguiente)

                # Conectar el nodo actual con el siguiente usando el literal como símbolo
                grafo.conectar(estado_actual, estado_siguiente, simbolo=valor)

                # Establecer el estado inicial si es el primer token
                if i == 0:
                    grafo.set_estado_inicial(estado_actual)

                # Establecer el estado final si es el último token
                if i == len(tokens) - 1:
                    grafo.set_estado_final(estado_siguiente)

        # Mostrar las transiciones del grafo
        grafo.mostrar()
        return grafo
