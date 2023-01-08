class Temperature:
    """Класс преобразования температуры."""
    def __init__(self, celsius: int, fahrenheit: float, kelvin: float):
        """Инициализация температур."""
        self.celsius = celsius
        self.fahrenheit = fahrenheit
        self.kelvin = kelvin

    def celsius_kelvin(self) -> str:
        """Преобразование температуры из цельсия в кельвин и назад."""
        kelvin = self.celsius + 273.15
        celsius = self.kelvin - 273.15
        return f"{kelvin} K, {celsius:.1f} C"

    def fahrenheit_celsius(self) -> str:
        """Преобразование температуры из фаренгейта в цельсия и назад."""
        celsius = (self.fahrenheit - 32) * 5/9
        fahrenheit = (self.celsius * 9/5) + 32
        return f"{celsius} C, {fahrenheit:.1f} F"

    def kelvin_fahrenheit(self) -> str:
        """Преобразование температуры из фаренгейта в кельвин и назад."""
        kelvin = (self.fahrenheit - 32) * 5/9 + 273.15
        fahrenheit = (self.kelvin - 273.15) * 9/5 + 32
        return f"{kelvin} K, {fahrenheit:.1f} F."


t = Temperature(40, 140.0, 293.15)
print(t.celsius_kelvin())
print(t.fahrenheit_celsius())
print(t.kelvin_fahrenheit())