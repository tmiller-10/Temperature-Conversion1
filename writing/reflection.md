# Temperature Conversion

## Tyler Miller

## Program Output

### What is the output from running the following commands?

Use a fenced code block to provide the output for this command.

- `poetry run converter --from-unit Celsius --to-unit Fahrenheit --temperature 22`

```python
🧮 Converting from Celsius to Fahrenheit!

 22.0 degrees in Celsius is 71.6 degrees in Fahrenheit
 ```

Use a fenced code block to provide the output for this command.

- `poetry run converter --from-unit Fahrenheit --to-unit Celsius --temperature 71.6`

```python
🧮 Converting from Fahrenheit to Celsius!

 71.6 degrees in Fahrenheit is 22.0 degrees in Celsius
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A class declaration for the different units of measurement

```python
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
```

The following source code segments explain how to declare the different units of measurement. This causes you to go from one unit to another unit within the application of conversion.
We first start off with identifying the different units of measurement of temperature and from unit and to unit. These are important to understand because they are crucial for the conversion.
Conversion_temperature is first Identified with 0. You need to start at a certain point of the unit of temperature. Next we have an if statement that is saying from the unit value of celsius and to unit of the value of fahrenheit.
This means that it is saying it is defining the two functions or the two units of measurement.Then we have an else if statement that is also calling the fahrenheit unit to celsius unit. It's the same thing as above, just converting the other unit basically.
After that we return the function called converted_temperature and get output.

#### Declaration of the function called `convert_celsius_to_fahrenheit`

```python
def convert_celsius_to_fahrenheit(temperature: float) -> float:
    """Convert the provided temperature from Celsius to Fahrenheit."""
    converted_temperature = 0
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = (temperature * (9 / 5)) + 32
    return round(converted_temperature, 1)
```

The following example is declaring the function called convert_celsius_to_fahrenheit.The function takes the function and defines the unit with converted_temperature equals zero. It is crucial that it has a starting value of zero(0).
The next line takes it from units.TemperatureUnitOfMeasurement.celsius which means its starting at the value of the conversion from celsius to Fahrenheit. This is also a huge part of the conversion because you need to specify where you are at and where you need to go to.
In the next code line we are saying we are going to the to_unit value. This is the same thing but just saying on where you are going to in the unit of measurement. This is crucial because you need to say where you are going.
The next source code segment is defining the equation of how to do the calculation of where to go with the math of to get the temperature needed to get the expected output.
Next we return the conversion of temperature. I added a round to round the output to the next place value.

#### Invocation of the function called `convert_celsius_to_fahrenheit`

```python
converted_temperature = 0
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = (temperature * (9 / 5)) + 32
    return round(converted_temperature, 1)
```

This part of the convert celsius to fahrenheit defines it with the starting the conversion of the temperature. This statement is necessary because within temperature you have a place value so in coding you need to have it start out as something.
from and to units are crucial because when you are having these functions being converted you have to make sure you set them up so they can be iterated for the equation of the temperature and the conversion of the temperature.
In the next convert segment. The equation of the temperature is the how you get from one unit to another. When stating this is has to be write or you will not get the necessary output of the function.
Returning the function of the conversion is crucial because this gives you the output of how to get that conversion between celsius to fahrenheit.

#### Test case for the function called `convert_celsius_to_fahrenheit`

```python
def test_convert_celsius_to_fahrenheit():
    """Check to ensure that Celsius to Fahrenheit conversion works."""
    temperature = 0
    converted_temperature = convert.convert_celsius_to_fahrenheit(temperature)
    assert converted_temperature == 32
```

In the following test suite for the function called `convert_celsius_to_fahrenheit. What happens is this is to see if the function checks to ensure that that Celsius to Fahrenheit conversion works.
In the first line it has the temperature that is set to equal zero like in the convert.py function. This checks to see if that lines up with the other function.
The line below it makes it convert the temperature from celsius to fahrenheit.
After that it asserts to convert the temperature to 32.

#### Execute trace of the `converter` program

- `poetry run converter --from-unit Celsius --to-unit Fahrenheit --temperature 22`

```python
def convert_celsius_to_fahrenheit(temperature: float) -> float:
    """Convert the provided temperature from Celsius to Fahrenheit."""
    converted_temperature = 0
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = (temperature * (9 / 5)) + 32
    return round(converted_temperature, 1)
```

The functions run the code that converts the provided temperature from Celsius to Fahrenheit. They have the necessary tools to go from the convert celsius to Fahrenheit in the converter file to the main file. These functions are called in each of the files and then go from the converter to the main file.
These work as they go from the converter file and do the conversion of the equations necessary to go back into the main file. Its important it works this way because it needs to be called in one file to be called in a conversion to go through data for the temperature conversion.
This is how you get the necessary conversion while having to go from convert to main then returns to the convert in the main.

## Professional Assessment

### Based on your experiences so far this semester, what is the area in which you've had the greatest improvement?

When going through experiences of the semester, I think the greatest improvement of the semester was just knowledge of coding. I felt like last semester I wasn't able to get the key details of coding.
I have seeked the attention of Technical Leaders of the class for more knowledge and I feel like they have done that. Even when asking questions to other people in the class at my table it makes it so much better to understand what is really going on.
These concepts make it better so that I can gain more knowledge for the degree of computer science.

### Based on your experiences with this project, what is one way in which you want to improve?

The one way I would improve the project would be to have different iterations of the equation within how to get to the necessary output.
I might be wrong and there might only be one way but it would be interesting if there was other ways to find the answer of converting from temperature to temperature of the units at hand.
Overall It would just be a cool conversion to have and experiment with at hand. That is my experiences with this project.
