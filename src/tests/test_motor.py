import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.motor_validacion import MotorDeValidacion

class TestMotorDeValidacion(unittest.TestCase):
    
    def test_validacion_cadena_correcta(self):
        motor = MotorDeValidacion("a*b")
        resultado = motor.validar_cadena("aab")
        self.assertTrue(resultado)  # La cadena "aab" cumple con "a*b"

    def test_validacion_cadena_incorrecta(self):
        motor = MotorDeValidacion("a*b")
        resultado = motor.validar_cadena("abc")
        self.assertFalse(resultado)  # La cadena "abc" no cumple con "a*b"

    def test_validacion_multiples_cadenas(self):
        motor = MotorDeValidacion("a*b")
        cadenas = ["aab", "b", "abc"]
        resultados_esperados = {"aab": True, "b": True, "abc": False}
        resultados = motor.validar_multiples_cadenas(cadenas)
        self.assertEqual(resultados, resultados_esperados)

    def test_expresion_invalida(self):
        motor = MotorDeValidacion("a[")
        self.assertTrue(any("Error en la expresión regular" in error for error in motor.obtener_errores()))
        resultado = motor.validar_cadena("a")
        self.assertFalse(resultado)  # La validación debe fallar con expresión inválida

if __name__ == "__main__":
    unittest.main()
