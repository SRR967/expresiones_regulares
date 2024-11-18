from .automata import Grafo

class GeneradorDeAutomatas:

    def construir_grafo_desde_tokens(self, tokens):
        """
        Construye un grafo dirigido desde una lista de tokens.
        Maneja correctamente literales, el operador de unión (|),
        el operador de cerradura positiva (+), y permite múltiples estados finales.
        """
        grafo = Grafo()
        estado_anterior = None
        valor_anterior = None
        pila = []  # Pila para manejar subexpresiones y paréntesis


        for i, (tipo, valor) in enumerate(tokens):
            #Pasa al siguiente ciclo si la ER empieza por (
            if i == 0 and valor == '(':
                valor_anterior=valor
                continue

            if tipo == 'LITERAL':
                if valor_anterior == '|':
                    # Nodo siguiente desde la unión
                    estado_siguiente = f"q{i+1}"   # Nodo siguiente
                    grafo.agregar_nodo(estado_siguiente)

                    # Conectar el estado inicial con el nuevo camino (literal)
                    grafo.conectar(grafo.estado_inicial.nombre, estado_siguiente, simbolo=valor)

                    # Actualizar el estado anterior
                    estado_anterior = estado_siguiente

                    # Actualizar el valor anterior
                    valor_anterior = valor
                    continue  # Pasar al siguiente token después de manejar la unión

                if valor_anterior == '+' or valor_anterior== '*':
                    # Nodo siguiente desde la unión
                    estado_siguiente = f"q{i+1}"   # Nodo siguiente
                    grafo.agregar_nodo(estado_siguiente)

                    # Conectar el estado inicial con el nuevo camino (literal)
                    grafo.conectar(estado_anterior, estado_siguiente, simbolo=valor)

                    # Actualizar el estado anterior
                    estado_anterior = estado_siguiente

                    # Actualizar el valor anterior
                    valor_anterior = valor
                    continue  # Pasar al siguiente token después de manejar la unión

                if valor_anterior == '(':
                    if  i !=1:
                        # Nodo siguiente desde la unión
                        estado_siguiente = f"q{i+1}"   # Nodo siguiente
                        grafo.agregar_nodo(estado_siguiente)

                        # Conectar el estado inicial con el nuevo camino (literal)
                        grafo.conectar(estado_anterior, estado_siguiente, simbolo=valor)

                        #Agregar valor a la pila
                        pila.append((estado_anterior))

                        # Actualizar el estado anterior
                        estado_anterior = estado_siguiente

                        # Actualizar el valor anterior
                        valor_anterior = valor
                        continue


                if valor_anterior == ')':
                    # Nodo siguiente desde la unión
                    estado_siguiente = f"q{i+1}"   # Nodo siguiente
                    grafo.agregar_nodo(estado_siguiente)

                    # Conectar el estado inicial con el nuevo camino (literal)
                    grafo.conectar(estado_anterior, estado_siguiente, simbolo=valor)

                    # Actualizar el estado anterior
                    estado_anterior = estado_siguiente

                    # Actualizar el valor anterior
                    valor_anterior = valor
                    #Sacar el ultimo valor de la pila
                    pila.pop()

                    continue


                # Crear dos nodos: uno actual y uno siguiente
                estado_actual = f"q{i}"         # Nodo actual
                estado_siguiente = f"q{i+1}"   # Nodo siguiente

                # Agregar ambos nodos al grafo
                grafo.agregar_nodo(estado_actual)
                grafo.agregar_nodo(estado_siguiente)

                # Conectar el nodo actual con el siguiente usando el literal como símbolo
                grafo.conectar(estado_actual, estado_siguiente, simbolo=valor)

                #Caso especial para cuando se inicia con (
                if valor_anterior== "(":
                    pila.append(estado_actual)

                # Establecer el estado inicial si es el primer token
                if estado_anterior is None:
                    grafo.set_estado_inicial(estado_actual)

            elif tipo == 'OPERADOR' and valor == '|':
                # Manejo del operador de unión (|)

                # Agregar el estado actual como estado final
                if estado_anterior is not None:
                    grafo.agregar_estado_final(estado_anterior)

            elif tipo == 'OPERADOR' and valor == '+':
                # Manejo del operador de cerradura positiva (+)
                
                if valor_anterior == ")":
                    estado_inicial_aux = pila.pop()
                    grafo.conectar(estado_anterior,estado_inicial_aux,simbolo=None)
                    valor_anterior=valor
                    continue

                # Crear una conexión desde el nodo anterior hacia sí mismo
                if estado_anterior is not None:
                    grafo.conectar(estado_anterior, estado_anterior, simbolo=valor_anterior)


            elif tipo == 'OPERADOR' and valor == '*':
                # Manejo del operador de cerradura de Kleene (*)
                if valor_anterior == ")":
                    estado_inicial_aux = pila.pop()
                    grafo.conectar(estado_anterior,estado_inicial_aux,simbolo=None)
                    estado_anterior= estado_inicial_aux
                    valor_anterior=valor
                    continue

                # Crear una conexión desde el nodo anterior hacia sí mismo
                if estado_anterior is not None:
                    grafo.conectar(estado_anterior, estado_anterior, simbolo=valor_anterior)

                # Crear una transición epsilon desde el nodo anterior al siguiente
                estado_siguiente = f"q{i+1}"   # Nodo siguiente
                grafo.agregar_nodo(estado_siguiente)
                grafo.conectar(estado_anterior, estado_siguiente, simbolo=None)

                #Editar transicion
                grafo.editar_transicion(estado_actual,estado_anterior,None)
            
            if valor== '(':
                # Agregar el estado siguiente a la pila para manejar la subexpresión
                pila.append(estado_anterior)
                continue

            #Actualizar el estado anterior
            estado_anterior = estado_siguiente

            # Actualizar el valor anterior
            valor_anterior = valor

        # Establecer el último nodo como estado final
        grafo.agregar_estado_final(estado_anterior)

        # Mostrar las transiciones del grafo
        grafo.mostrar()
        return grafo
