import pytest
from calculator import Calculator


class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()

    # Тесты для сложения
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (5, 0, 5),
        (-5, 10, 5),
        (2.5, 3.5, 6.0),
        (0, 0, 0),
        (1000000, 2000000, 3000000),
    ])
    def test_add(self, calc, a, b, expected):
        result = calc.add(a, b)
        assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тесты для деления
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (5, 2, 2.5),
        (0, 5, 0),
        (-10, 2, -5),
        (10, -2, -5),
        (1, 3, 1/3),
        (2.5, 0.5, 5.0),
    ])
    def test_divide_normal_cases(self, calc, a, b, expected):
        result = calc.divide(a, b)
        assert result == expected, f"Ожидалось {expected}, получено {result}"

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError) as exc_info:
            calc.divide(10, 0)
        
        assert "Деление на ноль невозможно" in str(exc_info.value)
        print("Исключение ZeroDivisionError корректно обрабатывается")

    @pytest.mark.parametrize("b", [0, 0.0, -0.0])
    def test_divide_by_zero_variations(self, calc, b):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, b)

    # Тесты для проверки является ли число простым
    @pytest.mark.parametrize("n, expected", [
        (2, True),
        (3, True),
        (17, True),
        (97, True),
        (4, False),
        (9, False),
        (15, False),
        (1, False),
        (0, False),
        (-5, False),
        (-17, False),
        (100, False),
        (49, False),
    ])
    def test_is_prime_number(self, calc, n, expected):
        result = calc.is_prime_number(n)
        assert result == expected, f"Ожидалось {expected} для числа {n}, получено {result}"

    # Дополнительные тесты для граничных случаев
    @pytest.mark.parametrize("n", [-1, 0, 1])
    def test_is_prime_number_edge_cases(self, calc, n):
        result = calc.is_prime_number(n)
        assert result is False, f"Число {n} не должно быть простым"

    # Тесты с плавающей точкой для is_prime_number
    @pytest.mark.parametrize("n", [2.5, 3.7, 10.0])
    def test_is_prime_number_with_floats(self, calc, n):
        result = calc.is_prime_number(n)
        assert result is False, f"Дробное число {n} не должно быть простым"
