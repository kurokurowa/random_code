Temperature1 = input("Temperature in Celsius: ")
Temperature2 = input("Temperature in Fahrenheit: ")
Temperature3 = input("Temperature in Kelvin: ")
Char_1 = len(Temperature1)
Char_2 = len(Temperature2)
Char_3 = len(Temperature3)


if float(Temperature1) < -273.15:
    print("Temperature is non-existent")
else:
    Fahrenheit = 1.8 * float(Temperature1) + 32
    print(f"Celsius to Fahrenheit: {Fahrenheit} F")
    Celsius_Kelvin = float(Temperature1) + 273.15
    print(f"Celsius to Kelvin: {Celsius_Kelvin} K")

if int(Temperature2) < -459.67:
    print("Temperature is non-existent")
elif len(Temperature2) != 0:
    Celsius = (float(Temperature2) - 32) / 1.8
    print(f"Fahrenheit to Celsius: {Celsius} C")
    Fahrenheit_Kelvin = Celsius + 273.15
    print(f"Fahrenheit to Kelvin: {Fahrenheit_Kelvin} K")
else:
    print("")

if len(Temperature3) != 0:
    Kelvin1 = float(Temperature3) - 273.15
    print(f"Kelvin  to Celsius: {Kelvin1} C")
    Kelvin2 = (Kelvin1 - 32) / 1.8
    print(f"Kelvin to Fahrenheit: {Kelvin2} F")
else:
    print("")
