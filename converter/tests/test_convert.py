"""Test suite to ensure that each function words correctly."""

from pytest import approx

from converter import convert
from converter import units


def test_convert_celsius_to_fahrenheit():
    """Check to ensure that Celsius to Fahrenheit conversion works."""
    temperature = 0
    converted_temperature = convert.convert_celsius_to_fahrenheit(temperature)
    assert converted_temperature == 32


def test_convert_celsius_to_fahrenheit_floating_point():
    """Check to ensure that Celsius to Fahrenheit conversion works."""
    temperature = 26.667
    converted_temperature = convert.convert_celsius_to_fahrenheit(temperature)
    assert converted_temperature == approx(80, rel=1e-3)


def test_convert_celsius_to_fahrenheit_wrapper():
    """Use the wrapper to ensure that Celsius to Fahrenheit works."""
    temperature = 0
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    assert converted_temperature == 32


def test_convert_celsius_to_fahrenheit_wrapper_floating_point():
    """Use the wrapper to ensure that Fahrenheit to Celsius works."""
    temperature = 26.667
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    assert converted_temperature == approx(80, rel=1e-3)


def test_convert_fahrenheit_to_celsius():
    """Check to ensure that Celsius to Fahrenheit conversion works."""
    temperature = 32
    converted_temperature = convert.convert_fahrenheit_to_celsius(temperature)
    assert converted_temperature == 0


def test_convert_fahrenheit_to_celsius_floating_point():
    """Check to ensure that Celsius to Fahrenheit conversion works."""
    temperature = 80
    converted_temperature = convert.convert_fahrenheit_to_celsius(temperature)
    assert converted_temperature == approx(26.667, rel=1e-3)


def test_convert_fahrenheit_to_celsius_wrapper():
    """Use the wrapper to ensure that Fahrenheit to Celsius works."""
    temperature = 32
    from_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    to_unit = units.TemperatureUnitOfMeasurement.celsius
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    assert converted_temperature == 0


def test_convert_fahrenheit_to_celsius_wrapper_floating_point():
    """Use the wrapper to ensure that Fahrenheit to Celsius works."""
    temperature = 80
    from_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    to_unit = units.TemperatureUnitOfMeasurement.celsius
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    assert converted_temperature == approx(26.667, rel=1e-3)
