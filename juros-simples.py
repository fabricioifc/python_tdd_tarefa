# -*- coding: utf-8 -*-
import unittest

#
# Código limpo e funcionando
#
class Juros:
    def simples(self):
        return self.capital * self.taxa * self.n_periodos

#
# Testes
#
class MyCalcTest(unittest.TestCase):
    def testSimples(self):
        calcJuros = Juros()
        calcJuros.capital    = 16000;
        calcJuros.taxa       = 0.04;
        calcJuros.n_periodos = 4;

        self.assertEqual(2560, calcJuros.simples())

if __name__ == '__main__':
    unittest.main()