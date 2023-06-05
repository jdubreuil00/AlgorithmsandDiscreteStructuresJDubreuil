"""
Programming Assignment 4 - Algorithms + Discrete Structures
Jordan Dubreuil 6/5/2023
"""

def numDivisible(a, integer):
    """
    Find the number of entries in an array of integers that are divisible 
    by a given integer. The function has two input parameters, 
    an array of integers and a positive integer – and returns an integer 
    indicating the count using a return statement.

    Parameters:
        a: Number to check array of integer are divisble by.
        integer: Attray of integers to be evaluated.

    Return:
        count: Number of integers that are divisible by a. 
    """
    # Initializes the count of divisible integers.
    count = 0
    # Loops through the number of integers in a.
    for number in a:
        # Uses modulus to see if the integer is divisible by the integer in the array.
        if number%integer == 0:
            # Increases the count of numbers divisible in the array.
            count += 1
    # Returns the count.
    return count

def smallestGap(numbers):
    """
    Given an array of real numbers, without sorting the array, 
    finds the smallest gap between all pairs of elements 
    (for an array A, the absolute value of the difference between 
    elements a[i] and b[j]). The function has one input parameter – 
    numbers whish is an array of numbers – and returns a non-negative 
    number indicating the smallest gap in the return statement.

    Parameters:
        numbers: the array of real numbers to be evaluated.

    Return:
        smallestNum: The Smallest difference between each of the numbers in the array numbers.
    """
    # Stores the smallest calculated difference between numbers.
    smallestNum = 0
    # Loops though the array numbers for a.
    for a in numbers:
        # Interioir for loop that compares the values for each number in the array excluding the one being evlauated
        for b in numbers:
            # Check that we are not evaluating the number being evaluated.
            if a != b :
                # Stores the difference betweent the two values being evaluated.
                num = abs(a-b)
                # Checks to see if smallestNum has not been set. Sets up the fiirst difference value.
                if smallestNum == 0:
                    smallestNum = num
                # If smallestNum has been set check to see which evaluation is smaller.
                elif num< smallestNum:
                    # Updates smallest num if a new smallest difference has been found.
                    smallestNum = num
    # returns the smallest gap between numbers once they have all been evaluated
    return smallestNum

def multiplyMatricies(a, matrixA, matrixB):
    """
    Given an integer n>=2 and two nxn matrices matrixA and matrixB of real numbers,
    finds the product matrixA * matrixB of the matrices. The function has
    three input parameters – a positive integer a and two nxn 
    matrices of numbers matrixA and matrixB– It returns the nxn product matrix 
    using a return statement.

    Parameters:
        a: An Integer >=2 that defines the dimentions of the results matrix.
        matrixA: The first matrix to be used to determing the product.
        matrixB: The secnd matrix to be used to determine the product.
    
    Return:
        result: The product of matrixA and matrixB nxn product matrix.
    """
    # Checks that parameter a is a valid dimension for the result matrix
    if a<2:
        print("Values >= 2 please.")
        return
    
    # Initialized the result matrix using the dimension parameter a.
    result = [[0] * a for _ in range(a)]

    # For loop that detemines the position i of the results array to access and add the product to.
    for i in range(a):
        # Interior for loop that detemines the position j of the results array to access and add the product to.
        for j in range(a):
            # Interior for loop that detemines the position k of matrixA and matrix B multiply.
            for k in range(a):
                # Does the multiplication of the proper array values and appends them to the results matrix.
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    # Returns the results matrix.
    return result


if __name__=="__main__":
    # Assignment input value for Algorithm 1
    a = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    b = [18, 54, 76, 81, 36, 48, 99]

    # Console responses for Algorithm 1
    print('Results from Algorithm 1')
    print(numDivisible(a, 7))
    print(numDivisible(b, 9))
    print('^^^^^^^^^')

    # Assignment input value for Algorithm 2
    c = [50, 120, 250, 100, 20, 300, 200]
    d = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

    # Console responses for Algorithm 2
    print('Results from Algorithm 2')
    print(smallestGap(c))
    print(smallestGap(d))
    print('^^^^^^^^^')

    # Assignment input value for Algorithm 3
    print('Results from Algorithm 3')
    size = 2
    e = [[2,7],[3,5]]
    f = [[8,-4],[6,6]]

    # Console responses for Algorithm 3
    print(multiplyMatricies(size,e,f))

    # Assignment input value for Algorithm 3
    sizeb = 3
    set1 = [[1,0,2],[3,-2,5],[6,2,-3]]
    set2 = [[.3,.25,.1], [.4,.8,.0], [-.5,.75,.6]]

    # Console responses for Algorithm 3
    print(multiplyMatricies(sizeb,set1,set2))
    print('^^^^^^^^^')