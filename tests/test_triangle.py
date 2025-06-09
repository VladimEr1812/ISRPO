import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для функций, связанных с треугольником."""

    def test_area_zero_values(self):
        """Тест площади треугольника при нулевом основании или высоте."""
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_positive_values(self):
        """Тест площади треугольника с положительными значениями."""
        self.assertEqual(area(6, 4), 12.0)
        self.assertEqual(area(7, 2), 7.0)
        self.assertEqual(area(5.5, 2), 5.5)

    def test_area_negative_values_should_raise_error(self):
        """Тест площади треугольника с отрицательными значениями (ожидаем ошибку ValueError)."""
        with self.assertRaises(ValueError):
            area(-6, 4)
        with self.assertRaises(ValueError):
            area(6, -4)
        with self.assertRaises(ValueError):
            area(-6, -4)

    def test_perimeter_positive_values(self):
        """Тест периметра треугольника с положительными сторонами."""
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10, 10, 10), 30)
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4), 10.0) # assertAlmostEqual для float

    def test_perimeter_invalid_triangle(self):
        """Тест периметра для некорректного треугольника (не выполняется неравенство треугольника)."""
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10) # 1+2 < 10
        with self.assertRaises(ValueError):
            perimeter(1, 9, 10) # 1+9 = 10 (граничный случай, часто считается некорректным)
        with self.assertRaises(ValueError):
            perimeter(10, 2, 7) # 2+7 < 10

    def test_perimeter_negative_side(self):
        """Тест периметра треугольника с отрицательной стороной (ожидаем ошибку ValueError)."""
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5) # Все стороны отрицательны
