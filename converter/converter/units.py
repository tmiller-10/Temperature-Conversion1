"""Create a module with an enumeration class for the units of measurement in temperature."""

from enum import Enum


class TemperatureUnitOfMeasurement(str, Enum):
    """Define an enumeration of the types of measurement units for temperature."""

    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
