"""Perform temperature conversion between Fahrenheit and Celsius."""

# from converter.converter.convert import convert_fahrenheit_to_celsius

import typer


from converter import convert
from converter import units

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def converter(
    from_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.celsius,
    to_unit: units.TemperatureUnitOfMeasurement = units.TemperatureUnitOfMeasurement.fahrenheit,
    temperature: float = typer.Option(98.6, min=-130, max=140),
):
    """Convert units.from Fahrenheit to Celsius or from Celsius to Fahrenheit."""
    if from_unit == units.TemperatureUnitOfMeasurement.fahrenheit:
        converted_temperature = convert.convert_fahrenheit_to_celsius(temperature)
        print("🧮 Converting from Fahrenheit to Celsius!")
        print(
            f"\n {temperature} degrees in {from_unit} is {converted_temperature} degrees in {to_unit}"
        )
    elif from_unit == units.TemperatureUnitOfMeasurement.celsius:
        print("🧮 Converting from Celsius to Fahrenheit!")
        converted_temperature = convert.convert_celsius_to_fahrenheit(temperature)
        print(
            f"\n {temperature} degrees in {from_unit} is {converted_temperature} degrees in {to_unit}"
        )

    # create a new Console object
    # display the two input parameters provided on the command line
    # perform the conversion of the temperature from one unit to another unit
    # display an extra blank line between the two entires
    # display the original temperature and then the converted temperature, always using units
