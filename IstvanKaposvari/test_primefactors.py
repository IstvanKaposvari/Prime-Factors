import unittest
from primefactors import primeFactors

class Test(unittest.TestCase):

    def testNormalNumbers(self):
        self.assertEqual(primeFactors(2), [2])
        self.assertEqual(primeFactors(975579), [3,11,17,37,47])
        self.assertEqual(primeFactors(189738650192950919), [53,101,577,991,1879,3299])
        
        
    def testNoneFactorisableNumbers(self):    
        self.assertEqual(primeFactors(1), [])
        self.assertEqual(primeFactors(0), [])
        self.assertEqual(primeFactors(-1), [])
        
    def testNegativeNumbers(self):
        self.assertEqual(primeFactors(-2), [2])
        self.assertEqual(primeFactors(-975579), [3,11,17,37,47])
        self.assertEqual(primeFactors(-18973865019295091), [53,101,577,991,1879,3299])


if __name__ == "__main__":
    unittest.main()