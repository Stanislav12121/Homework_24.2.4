import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    # позитивный тест метода калькулятора "Сложение"
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 1, 1) == 2

    # позитивный тест метода калькулятора "Умножение"
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # позитивный тест метода калькулятора "Деление"
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    # позитивный тест метода калькулятора "Вычитание"
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def teardown(self):
        print('Выполнение метода Teardown')