import unittest

class Calc:
    def dobro(self, num):
        return num * 2

class MyCalcTest(unittest.TestCase):
    def testDobro(self):
        obj = Calc()
        self.assertEqual(17, obj.dobro(8))

if __name__ == '__main__':
    unittest.main()
