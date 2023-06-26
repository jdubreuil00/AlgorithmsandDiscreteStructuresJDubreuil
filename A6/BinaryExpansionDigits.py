def countBinaryDigits(number):
    """
    Takes a positive integer and recursively uses the 
    floor division operator to divide by 2. The number of times it
    takes to get to less than one is the number of digits in the 
    binary expansion.

    Parameters:
        number: Positive integer used to find the number of digits in a binary expansion.
    
    Returns:
        If the number is not positive,
        or the number of digits in the binary expansion.
    """
    if number < 0:
        return "Sorry, number is not a positive integer."
    if number <= 1:
        return 1
    else:
        return 1 + countBinaryDigits(number // 2)


if __name__ == "__main__":
    print(f"Number of digits: {countBinaryDigits(255)}")
    print(f"Number of digits: {countBinaryDigits(750)}")
   


def sumOfSquares(number):
    """
    Takes the given positive integer and if it is greater than one
    squares the integer and adds it to the recursive function call 
    of the positive integer minus one. When complete the fucntion
    returns the added sum of the squared integers.

    Paramerters:
        number: The supplied positive integer that is used to calculate the sum of the squared numbers.
    
    Returns:
        The sum of the squared numbers if a positive integer is supplied.
    """
    if number < 0:
        return "Sorry, number is not a positive integer."
    if number == 1:
        return 1
    if number > 1:
        return number**2 + sumOfSquares(number - 1)


if __name__=="__main__":
    print(f"Sum of the integer squared is {sumOfSquares(12)}")
    print(f"Sum of the integer squared is {sumOfSquares(20)}")