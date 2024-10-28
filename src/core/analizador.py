import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from core.errores import ManejadorDeErrores

class AnalizadorLexico:
    """
    Clase para el análisis léxico de expresiones regulares.
    Convierte una expresión regular en tokens y valida su estructura.
    """

    def __init__(self, expresion_regular: str):
        self.expresion_regular = expresion_regular
        self.tokens = []
        self.manejador_errores = ManejadorDeErrores()  # Instancia del manejador de errores

    def tokenizar(self):
        """
        Convierte la expresión regular en tokens, separando operadores,
        literales y paréntesis.
        """
        patrones = {
            'LITERAL': r'[a-zA-Z0-9]',    # Cualquier carácter alfanumérico
            'OPERADOR': r'[*+|]',       # Operadores 
            'PARENTESIS_IZQ': r'\(',
            'PARENTESIS_DER': r'\)'
        }
        # Crear una expresión regular combinada para todos los patrones
        token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones.items())

        # Variable para rastrear la posición actual en la expresión regular
        posicion_actual = 0

        
        while posicion_actual < len(self.expresion_regular):
            # Intenta hacer coincidir cualquier token válido desde la posición actual
            match = re.match(token_regex, self.expresion_regular[posicion_actual:])
            
            if match:
                # Si hay coincidencia, agrega el token a la lista
                tipo_token = match.lastgroup
                valor_token = match.group()
                self.tokens.append((tipo_token, valor_token))

                # Avanza la posición según la longitud del token encontrado
                posicion_actual += len(valor_token)
            else:
                # Si no hay coincidencia, el carácter actual es inválido
                caracter_invalido = self.expresion_regular[posicion_actual]
                self.manejador_errores.agregar_error(f"Token inválido encontrado: '{caracter_invalido}' en posición {posicion_actual}")
                
                # Avanza la posición para continuar analizando
                posicion_actual += 1



    def validar_estructura(self):
        """
        Valida la estructura de la expresión regular y detecta errores comunes.
        """
        balance = 0  # Para verificar el balance de paréntesis
        prev_token = None
        prev_token_valor= None

        for tipo, valor in self.tokens:
            if tipo == 'PARENTESIS_IZQ':
                balance += 1
            elif tipo == 'PARENTESIS_DER':
                balance -= 1
                if balance < 0:
                    self.manejador_errores.agregar_error("Paréntesis de cierre sin apertura correspondiente.")
            
            if prev_token == 'OPERADOR' and tipo == 'OPERADOR':
                print(prev_token_valor)
                print(valor)
                if valor != '|' or prev_token_valor== valor:
                    self.manejador_errores.agregar_error(f"Operadores consecutivos '{valor}' no permitidos.")
                        
            prev_token = tipo
            prev_token_valor=valor

        if balance != 0:
            self.manejador_errores.agregar_error("Paréntesis sin cerrar en la expresión.")

    def analizar(self):
        """
        Método principal para realizar el análisis léxico completo.
        """
        self.tokenizar()
        self.validar_estructura()

    def obtener_errores(self):
        """
        Retorna la lista de errores a través del manejador de errores.
        """
        return self.manejador_errores.obtener_errores()

    def obtener_tokens(self):
        """
        Retorna la lista de tokens generada.
        """
        return self.tokens
