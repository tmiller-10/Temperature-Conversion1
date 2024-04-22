# Temperature Conversion

After cloning this repository to your computer, please take the following steps:

- Use the `cd` command to change into the directory for this repository.
- Change into the program directory by typing `cd converter`.
- Install the dependencies for the project by typing `poetry install`
- Run the program in its two different modes by typing:
  - `poetry run converter --from-unit Celsius --to-unit Fahrenheit --temperature 22`
  - `poetry run converter --from-unit Fahrenheit --to-unit Celsius --temperature 71.6`

When running the program of this command you will get this result

``poetry run converter --from-unit Celsius --to-unit Fahrenheit --temperature 22``

```
🧮 Converting from Celsius to Fahrenheit!

 22.0 degrees in Celsius is 71.6 degrees in Fahrenheit
```

`poetry run converter --from-unit Fahrenheit --to-unit Celsius --temperature 71.6`
```
🧮 Converting from Fahrenheit to Celsius!

 71.6 degrees in Fahrenheit is 22.0 degrees in Celsius
```
