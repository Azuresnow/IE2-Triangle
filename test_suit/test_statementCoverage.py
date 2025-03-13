import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):


    def testEq(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
 
        
    def testANegative(self):
        actual = Triangle.classify(-14, 3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def testBNegative(self):
        actual = Triangle.classify(15, -3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def testCNegative(self):
        actual = Triangle.classify(15, 10, -6)
        expected = Triangle.Type.INVALID        
        self.assertEqual(actual, expected)
   
        
    def testTrianEq0Invalid(self):
        actual = Triangle.classify(40, 14, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def testTrianEq0(self):
        actual = Triangle.classify(13, 14, 10)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)    
    def testTrianEq1(self):
        actual = Triangle.classify(10, 10, 5)
        expected = Triangle.Type.ISOSCELES    
        self.assertEqual(actual, expected)   
    def testTrianEq2(self):
        actual = Triangle.classify(10, 5, 10)
        expected = Triangle.Type.ISOSCELES    
        self.assertEqual(actual, expected)   
    def testTrianEq3(self):
        actual = Triangle.classify(5, 10, 10)
        expected = Triangle.Type.ISOSCELES    
        self.assertEqual(actual, expected)     
        
    def testLastStatement(self):
        actual = Triangle.classify(40, 5, 5)   
        expected = Triangle.Type.INVALID    
        self.assertEqual(actual, expected)  

if __name__ == '__main__':
    unittest.main()