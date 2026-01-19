try:
    celsius = float(input("Enter the temperature in celsius to convert : "))#Ask the user to enter the of temperature.
    unit_conversion = input("Which unit do you want to convert to (fahrenheit, rummer, kelvin)? ").lower()#Ask the user for unit to convert to.
    fahrenheit = (celsius * 9/5) + 32 #Convert Celsius to fahrenheit.
    rummer = (celsius * 4/5) # Convert Celsius to Rummer.
    kelvin = (celsius + 273) # Convert Celsius to Kelvin.
    if unit_conversion  == 'fahrenheit':
        print(f"After conversion, the temperature in fahrenheit is: {fahrenheit}")
    elif unit_conversion  == 'rummer':
        print(f"After conversion, the temperature in rummer is: {rummer}")
    elif unit_conversion  == 'kelvin':
        print(f"After conversion, the temperature in calvin is {kelvin} ")
    else:#Here if the input is not in unit_conversion show this message.
        print("Invalid unit! You can only enter (Fahrenheit, Rummer or Kelvin) in this part. ")
except ValueError:#This exception handles invalid numeric input for Celsius.
    print("Value Error! Please enter a number for the temperature, not a letter or a symbol.")

