import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class ManejadorDeErrores:
    """
    Clase para capturar y gestionar errores durante el procesamiento de
    expresiones regulares y validación de cadenas.
    """

    def __init__(self):
        # Almacena una lista de errores detectados
        self.errores = []

    def agregar_error(self, mensaje: str):
        """
        Agrega un mensaje de error a la lista de errores.
        """
        self.errores.append(mensaje)

    def obtener_errores(self):
        """
        Retorna todos los errores almacenados.
        """
        return self.errores

    def limpiar_errores(self):
        """
        Limpia todos los errores almacenados.
        """
        self.errores.clear()

    def hay_errores(self):
        """
        Retorna True si hay errores, False en caso contrario.
        """
        return len(self.errores) > 0

    def manejar_excepcion(self, excepcion: Exception):
        """
        Agrega un mensaje de error basado en una excepción capturada.
        """
        mensaje_error = f"Error: {str(excepcion)}"
        self.agregar_error(mensaje_error)
