import unittest
from procesador import validar_expresion

class TestValidacionRegex(unittest.TestCase):
    
    def test_ssn(self):
        self.assertTrue(validar_expresion(r'\d{3}-\d{2}-\d{4}', '123-45-6789'))
        self.assertFalse(validar_expresion(r'\d{3}-\d{2}-\d{4}', '123-45-678'))

    def test_letras(self):
        self.assertTrue(validar_expresion(r'^[a-zA-Z]+$', 'Hola'))
        self.assertFalse(validar_expresion(r'^[a-zA-Z]+$', 'Hola123'))

    def test_consonante_vocal(self):
        self.assertTrue(validar_expresion(r'^[^aeiou].*[aeiou]$', 'gato'))
        self.assertFalse(validar_expresion(r'^[^aeiou].*[aeiou]$', 'manzana'))

    def test_email(self):
        self.assertTrue(validar_expresion(r'^.+@.+\..+$', 'ejemplo@dominio.com'))
        self.assertFalse(validar_expresion(r'^.+@.+\..+$', 'ejemplo@'))

if __name__ == '__main__':
    unittest.main()
