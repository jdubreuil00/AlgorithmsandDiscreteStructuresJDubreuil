import math
"""
Programming Assignment 07 Week 7 
Jordan Dubreuil
"""


# Exercise 1 Mean of a List of Elements
Atest = [40,50,60,70,80] #5 entries
A1 = [12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102] #11 entries
A2 = [-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2] #10 entries


def Mean(A,n):
    """
    The Mean function uses a decrease by constant recursive algorithm
    to calculate a non empty array of numbers. It uses the count of 
    items in the array as a constant to calculate the mean of the array.

    Parameters: 
        A: The array of valuse to be calculated
        n: The number of items in the array that is being calculated.
    
    Returns
        The mean value of the numbers in the array.
    """
    if n>1:
        return (n-1)/n*Mean(A,n-1)+1/n*A[n-1]
    else:
        return A[0]


##### Exercise 2 Binary Search of Descended Sorted List

Atest2 = [50, 41, 27, 20, 17, 12, 5]
A3 = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]

def DescendSortBinarySearch(A,start,end,k):
    """
    This Method returns the subscript of an element in and array 
    sorted in descending order if it finds the element in the recursive search algorithm. It 
    does this by taking the number of elements in the array and dividing them in half. It uses 
    the result of that number to check the index of elements to see if it matches what is being 
    looked for. If it does it rerurns the key, if it doesn't it recursively looks for the result
    until it is found or it is determined not to be in the array.

    Parameters:
        A: The array of elements to search.
        start: The starting index of the array.
        end: the final index of the array.
        k: The element searched for in the array.
    
    Returns:
        None: The element wasnt found
        Number: Index of the found element in the array.
    """
    m = math.floor((end+start)/2)
    if start>end:
        return None
    else:
        if A[m] == k:
            return m
        elif A[m] < k:
            return DescendSortBinarySearch(A,start,m-1, k)
        else:
            return DescendSortBinarySearch(A,m+1, end, k)

# Exercise 3 Greatest Common Divisor

def GCD(m,n):
    """
    Returns the Greatest Common Divisor from two positive integers.
    Before each recursive call the function prints out the two integers
    being passed as parameters.

    Parameters:
        m: First positiver integer to be evaluated.
        n: Second positive integer to be evaluated.

    Returns:
        Greatest Common Divisor of the two integers given.

    """
    if n == 0:
        return m
    else:
        print(n, m%n)
        return GCD(n, m%n)


if __name__ == "__main__":
    # Mean function calls for the assignment.
    print("================Exercise 1=================")
    print(Mean(Atest,5))
    print(Mean(A1,11))
    print(Mean(A2,10))
    # Descend Sorted Binary search function calls for the assignment.
    print("================Exercise 2=================")
    print(DescendSortBinarySearch(Atest2, 0, len(Atest2)-1, 27))
    print(DescendSortBinarySearch(A3, 0, len(A3)-1, 87)) 
    print(DescendSortBinarySearch(A3, 0, len(A3)-1, 48))
    print(DescendSortBinarySearch(A3, 0, len(A3)-1, 33))
    print(DescendSortBinarySearch(A3, 0, len(A3)-1, 10))
    print("================Exercise 3=================")
    # GCD function calls for assignment.
    print(GCD(144,42))
    print(GCD(2468, 1357))
    print(GCD(111, 378))
    print(GCD(123456789, 987654321))



