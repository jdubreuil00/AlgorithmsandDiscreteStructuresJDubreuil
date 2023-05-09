"""
Worksheet 1 part 1 "Is It Cold In Canada Today?"
Jordan Dubreuil
5/8/2023
This Program asks the user for a number representing the temperature
a Canadian would consider to be cold in Celcius. It then asks for the current 
temperature in Fahrenheit and makes a comparison with the Celsius value 
converted to Fahrenheit. If it is not cold for the Canadian the program prints 
"The Canadian does not think it is cold today.". If it is too cold the program 
prints "Brr... the Canadian thinks it is cold outside."

"""

while True:
    try:
        # Asks the Canadian for the temperature i  Celsius
        celsius = float(input('What is the threshold for cold in Canada? '))
    except ValueError:
        #Validate input
        print('Sorry please try a valid temperature...')
        continue
    else:
        # Exits the while loop because input is valid.
        break

# Converts the Canadian's response to Fahrenheit.
fahrenheit = (celsius * 9/5) + 32
# Print to the user the temperture converted to Fahrenheit.
print(f'The Canadian thinks this is cold {fahrenheit} in Fahrenheit!')

while True:
    try:
        # Asks the user what the current temperature is today.
        prompt = float(input("What is today's temperature in Fahrenheit "))
    except ValueError:
        #Validate input
        print('Sorry please try a valid temperature...')
        continue
    else:
        # Exits the while loop because input is valid.
        break


if(prompt > fahrenheit):
    # If the temperature is greater than the Canadian's converted threshold.
    print("The Canadian does not think it is cold today.")
else:
    # If the temperature is less than the Canadian's converted threshold.
    print("Brr... the Canadian thinks it is cold outside.")
