import re

class AnalizadorLexico:
    """
    Clase para el análisis léxico de expresiones regulares.
    Convierte una expresión regular en tokens y valida su estructura.
    """

    def __init__(self, expresion_regular: str):
        self.expresion_regular = expresion_regular
        self.tokens = []
        self.errores = []

    def tokenizar(self):
        """
        Convierte la expresión regular en tokens, separando operadores,
        literales y paréntesis.
        """
        # Definimos los tokens que queremos reconocer (literal, operador, paréntesis)
        patrones = {
            'LITERAL': r'[a-zA-Z0-9]',    # Cualquier carácter alfanumérico
            'OPERADOR': r'[.*+?|]',       # Operadores comunes de regex
            'PARENTESIS_IZQ': r'\(',
            'PARENTESIS_DER': r'\)'
        }
        
        # Combinamos los patrones en una expresión regular
        token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones.items())
        for match in re.finditer(token_regex, self.expresion_regular):
            tipo_token = match.lastgroup
            valor_token = match.group()
            self.tokens.append((tipo_token, valor_token))

    def validar_estructura(self):
        """
        Valida la estructura de la expresión regular y detecta errores comunes.
        """
        balance = 0  # Para verificar el balance de paréntesis
        prev_token = None

        for tipo, valor in self.tokens:
            # Verificamos errores de balance de paréntesis
            if tipo == 'PARENTESIS_IZQ':
                balance += 1
            elif tipo == 'PARENTESIS_DER':
                balance -= 1
                if balance < 0:
                    self.errores.append("Paréntesis de cierre sin apertura correspondiente.")
            
            # Ejemplo de verificación de doble operador (p. ej., "++" o "**")
            if prev_token == 'OPERADOR' and tipo == 'OPERADOR':
                self.errores.append(f"Operadores consecutivos '{valor}' no permitidos.")
            
            prev_token = tipo

        if balance != 0:
            self.errores.append("Paréntesis sin cerrar en la expresión.")

    def analizar(self):
        """
        Método principal para realizar el análisis léxico completo.
        """
        self.tokenizar()
        self.validar_estructura()

    def obtener_errores(self):
        """
        Retorna una lista de errores encontrados en la expresión regular.
        """
        return self.errores

    def obtener_tokens(self):
        """
        Retorna la lista de tokens generada.
        """
        return self.tokens
