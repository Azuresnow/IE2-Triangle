import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):
    def test_invalid_triangle(self):
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-5, 3, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, -4, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 4, -3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 4, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 4), Triangle.Type.INVALID)

    def test_Scalene(self):
        self.assertEqual(Triangle.classify(10, 8, 9), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(10, 9, 6), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(5, 9, 8), Triangle.Type.SCALENE)

    def test_Eq(self):
        self.assertEqual(Triangle.classify(8, 8, 8), Triangle.Type.EQUILATERAL)

    def test_Isosceles(self):
        self.assertEqual(Triangle.classify(4, 5, 4), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(4, 4, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)

    def test_EdgeCase(self):
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(0, 1, 8), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(8, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 1, 1), Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()