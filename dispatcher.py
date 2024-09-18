import configparser
import os

class PackageDispatcher:
    def __init__(self, config_file='config.ini'):
        config = configparser.ConfigParser()
        config.read(config_file)

        thresholds = config['Thresholds']
        self.max_volume = float(thresholds['max_volume'])
        self.max_dimension = float(thresholds['max_dimension'])
        self.max_mass = float(thresholds['max_mass'])

    def sort(self, width, height, length, mass):
        # Input validation
        for dimension_name, dimension_value in zip(
            ['width', 'height', 'length', 'mass'],
            [width, height, length, mass]
        ):
            if not isinstance(dimension_value, (int, float)):
                raise ValueError(f"{dimension_name} must be a number.")
            if dimension_value <= 0:
                raise ValueError(f"{dimension_name} must be a positive number.")

        is_bulky = False
        is_heavy = False

        volume = width * height * length
        max_dimension = max(width, height, length)

        if volume >= self.max_volume or max_dimension >= self.max_dimension:
            is_bulky = True

        if mass >= self.max_mass:
            is_heavy = True

        if is_bulky and is_heavy:
            return "REJECTED"
        elif is_bulky or is_heavy:
            return "SPECIAL"
        else:
            return "STANDARD"

if __name__ == '__main__':
    dispatcher = PackageDispatcher()
    while True:
        try:
            width = float(input("Enter width (cm): "))
            height = float(input("Enter height (cm): "))
            length = float(input("Enter length (cm): "))
            mass = float(input("Enter mass (kg): "))

            result = dispatcher.sort(width, height, length, mass)
            print(f"The package should be placed in: {result}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
