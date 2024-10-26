import re

class MotorDeValidacion:
    """
    Clase para validar cadenas contra una expresión regular.
    """
    
    def __init__(self, expresion_regular: str):
        self.expresion_regular = expresion_regular
        self.regex = None
        self.errores = []
        
        self.compilar_expresion()
    
    def compilar_expresion(self):
        """
        Compila la expresión regular para su uso en validación.
        Maneja errores de sintaxis en la expresión.
        """
        try:
            self.regex = re.compile(self.expresion_regular)
        except re.error as e:
            self.errores.append(f"Error en la expresión regular: {e}")
    
    def validar_cadena(self, cadena: str) -> bool:
        """
        Valida si una cadena cumple con la expresión regular.
        """
        if self.regex is None:
            self.errores.append("La expresión regular es inválida.")
            return False
        
        # Retorna True si la cadena cumple la expresión, False si no
        return bool(self.regex.fullmatch(cadena))
    
    def validar_multiples_cadenas(self, cadenas: list) -> dict:
        """
        Valida múltiples cadenas y retorna un diccionario con los resultados.
        """
        resultados = {}
        for cadena in cadenas:
            resultados[cadena] = self.validar_cadena(cadena)
        return resultados
    
    def obtener_errores(self):
        """
        Retorna la lista de errores.
        """
        return self.errores
