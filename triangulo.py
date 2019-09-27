# -*- coding: utf-8 -*-
import unittest

#
# Classe que representa um triângulo
#
class Triangulo:

    #
    # Confirma se as medidas compõem um triângulo
    #
    def ehTriangulo(self):
        if self.a < (self.b + self.c):
            if self.b < (self.a + self.c):
                if self.c < (self.a + self.b):
                    return True

    #
    # Confirma se o triângulo é escaleno
    #
    def ehEscaleno(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return True
        else:
            return False

    #
    # Confirma se o triângulo é isosceles
    #
    def ehIsosceles(self):
        if self.a == self.b:
            return True
        elif self.a == self.c:
            return True
        elif self.b == self.c:
            return True
        else:
            return False

    #
    # Confirma se o triângulo é equilátero
    #
    def ehEquilatero(self):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return True
        else:
            return False

#
# Testes
#
class MyCalcTest(unittest.TestCase):

    def testEhTriangulo(self):
        tri = Triangulo()
        tri.a = 3
        tri.b = 4
        tri.c = 5
        self.assertTrue(tri.ehTriangulo())

    def testEhEquilatero(self):
        tri = Triangulo()
        tri.a = 4
        tri.b = 4
        tri.c = 4
        self.assertTrue(tri.ehEquilatero())

    def testEhIsosceles(self):
        tri = Triangulo()

        tri.a = 3
        tri.b = 3
        tri.c = 5
        self.assertTrue(tri.ehIsosceles())

        tri.a = 3
        tri.b = 5
        tri.c = 3
        self.assertTrue(tri.ehIsosceles())

        tri.a = 5
        tri.b = 3
        tri.c = 3
        self.assertTrue(tri.ehIsosceles())

    def testEhEscaleno(self):
        tri = Triangulo()
        tri.a = 3
        tri.b = 4
        tri.c = 5
        self.assertTrue(tri.ehEscaleno())

if __name__ == '__main__':
    unittest.main()