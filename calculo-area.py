# -*- coding: utf-8 -*-
import unittest

# Classe para abstrair
# cálculos geométricos referente a área.
class Area():

    # Retorna a área quadrada
    def quadrada(self):
        return self.lado1 * self.lado2

    # Retorna a área cúbica
    def cubica(self):
        return self.lado1 * self.lado2 * self.lado3

#
# Testes
#
class MyCalcTest(unittest.TestCase):

    def testAreaQuadrada(self):
        area = Area()
        area.lado1 = 3
        area.lado2 = 9
        self.assertEqual(27, area.quadrada())

    def testAreaCubica(self):
        area = Area()
        area.lado1 = 3
        area.lado2 = 6
        area.lado3 = 2
        self.assertEqual(36, area.cubica())

if __name__ == '__main__':
    unittest.main()