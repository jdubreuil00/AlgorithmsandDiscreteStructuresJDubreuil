"""
Worksheet 1 part 3 Loops
Jordan Dubreuil
5/8/2023
This Program asks the user for an even integer value between 9 and 21.
When input is validated the program swaps each value in pairs.

"""
while True:
    try:
        # Asks the user to input even values between 9 and 21.
        numberForVector = int(
            input('Enter an even integer between 9 and 21. '))
    except ValueError:
        # Validate input
        print('Please try a valid number...')
        continue
    # Checks for an even integer between 9 and 21.
    if numberForVector < 9 or numberForVector > 21 or numberForVector % 2 != 0:
        print("Please enter the correct value.")
        continue
    else:
        # Creates a vector for the specified range.
        vector = [i for i in range(numberForVector)]
        # Loops through the values of the vector in two steps.
        for item in range(0, len(vector), 2):
            # Copys the values for the swap.
            item1 = vector[item]
            item2 = vector[item+1]
            # Swaps the values
            vector[item] = item2
            vector[item + 1] = item1
        # Prints the vector of swapped values and exits the program.
        print(vector)
        break
