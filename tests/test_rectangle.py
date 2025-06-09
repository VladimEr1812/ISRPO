import unittest
from rectangle import area, perimeter 

class RectangleTestCase(unittest.TestCase):  
    """Тесты для функций, связанных с прямоугольником."""

    def test_area_zero_mul(self): 
        """Тест площади прямоугольника при умножении на ноль."""
        self.assertEqual(area(10, 0), 0)  
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_positive_values(self):
        """Тест площади прямоугольника с положительными значениями."""
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(5, 2), 10)
        self.assertEqual(area(7.5, 2), 15.0)

    def test_area_negative_values_should_raise_error(self):
        """Тест площади прямоугольника с отрицательными значениями (ожидаем ошибку)."""
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)
        with self.assertRaises(ValueError):
            area(-5, -10)


    def test_perimeter_zero_side(self):
        """Тест периметра прямоугольника с одной нулевой стороной."""
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)


    def test_perimeter_positive_values(self):
        """Тест периметра прямоугольника с положительными значениями."""
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(7, 7), 28)
        self.assertEqual(perimeter(3.5, 4.5), 16.0)

    def test_perimeter_negative_values_should_raise_error(self):
        """Тест периметра прямоугольника с отрицательными значениями (ожидаем ошибку)."""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(5, -10)
        with self.assertRaises(ValueError):
            perimeter(-5, -10)