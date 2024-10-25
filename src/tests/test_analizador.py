import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.analizador import AnalizadorLexico



class TestAnalizadorLexico(unittest.TestCase):
    
    def test_tokenizacion_basica(self):
        analizador = AnalizadorLexico("a*b|c")
        analizador.analizar()
        tokens_esperados = [
            ('LITERAL', 'a'),
            ('OPERADOR', '*'),
            ('LITERAL', 'b'),
            ('OPERADOR', '|'),
            ('LITERAL', 'c')
        ]
        self.assertEqual(analizador.obtener_tokens(), tokens_esperados)

    def test_errores_parentesis(self):
        analizador = AnalizadorLexico("(a|b")
        analizador.analizar()
        errores = analizador.obtener_errores()
        self.assertIn("Paréntesis sin cerrar en la expresión.", errores)
    
    def test_operadores_consecutivos(self):
        analizador = AnalizadorLexico("a++b")
        analizador.analizar()
        errores = analizador.obtener_errores()
        self.assertIn("Operadores consecutivos '+' no permitidos.", errores)

    def test_expresion_valida_sin_errores(self):
        analizador = AnalizadorLexico("a*b+c")
        analizador.analizar()
        self.assertFalse(analizador.obtener_errores())  # No debe haber errores

if __name__ == "__main__":
    unittest.main()
