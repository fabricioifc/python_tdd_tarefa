# -*- coding: utf-8 -*-
import unittest

#
# Código limpo e funcionando
#
class Calc:
    def dobro(self, num):
        return num * 2

#
# Testes
#
class MyCalcTest(unittest.TestCase):
    def testDobro(self):
        obj = Calc()
        self.assertEqual(17, obj.dobro(8))

if __name__ == '__main__':
    unittest.main()