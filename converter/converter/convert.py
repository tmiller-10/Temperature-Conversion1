"""Convert from Celsius to Fahrenheit and from Fahrenheit to Celsius."""

from converter import units


def convert_celsius_to_fahrenheit(temperature: float) -> float:
    """Convert the provided temperature from Celsius to Fahrenheit."""
    converted_temperature = 0
    converted_temperature = (temperature * (9 / 5)) + 32
    return converted_temperature


def convert_fahrenheit_to_celsius(temperature: float) -> float:
    """Convert the provided temperature from Fahrenheit to Celsius."""
    converted_temperature = 0
    converted_temperature = (temperature - 32) * (5 / 9)
    return converted_temperature


def convert_temperature(
    temperature: float,
    from_unit: units.TemperatureUnitOfMeasurement,
    to_unit: units.TemperatureUnitOfMeasurement,
):
    """Convert a temperature given the from_unit and the to_unit."""
    converted_temperature = 0
    # the requested temperature conversion is Celsius --> Fahrenheit
    if from_unit.value == "Celsius" and to_unit.value == "Fahrenheit":
        converted_temperature = convert_celsius_to_fahrenheit(temperature)
        # call the function that will convert from Celsius to Fahrenheit
    # the requested temperature conversion is Fahrenheit --> Celsius
    elif from_unit.value == "Fahrenheit" and to_unit.value == "Celsius":
        converted_temperature = convert_fahrenheit_to_celsius(temperature)
        # call the function that will convert from Celsius to Fahrenheit
    return converted_temperature
