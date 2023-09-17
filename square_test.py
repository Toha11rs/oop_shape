import math
import unittest
from square import Circle, Triangle  

class TestCircle(unittest.TestCase):
    def test_circle_square_positive_radius(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.square(), 12.566370, places=5)

    def test_circle_square_zero_radius(self):
        circle = Circle(0)
        self.assertAlmostEqual(circle.square(), 0)

    def test_circle_square_negative_radius(self):
        circle = Circle(-2)
        expected_square = math.pi * (-2)**2
        self.assertAlmostEqual(circle.square(), expected_square)

    def test_triangle_square_positive_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.square(), 6)

    def test_triangle_square_zero_sides(self):
        triangle = Triangle(0, 0, 0)
        self.assertAlmostEqual(triangle.square(), 0)

    def test_triangle_square_negative_sides(self):
        triangle = Triangle(-1, -2, -3)
        self.assertAlmostEqual(triangle.square(), 0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.right_triangle())

if __name__ == "__main__":
    unittest.main()
