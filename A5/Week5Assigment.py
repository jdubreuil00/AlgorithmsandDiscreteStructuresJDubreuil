# List of example values from Programming Assignment 5
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]


def swap(A,i,j):
    """
    Takes the list and two locations of the values 
    to be sorted and the swaps their position at 
    that location.

    Parameters:
        A: The list being sorted
        i: The lacation that needs to be swapped
        j: The location that it is being swapped with.
    
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def selectionsort(A):
    """
    The selection sort repeatedly selects the smallest 
    element from the unsorted portion and swaps 
    it with the element at the beginning of the 
    unsorted portion. This process continues 
    until the entire list is sorted.

    Parameters:
        A: The list to be sorted.
    
    Returns:
        A: The list sorted using selection sort.
    """
    print("^^^^^^^^^^")
    for i in range(len(A)):
        counterSwapped = 0
        counterCompared = 0
        m=i
        for j in range(len(A)-1):
            counterCompared +=1
            if A[j] > A[m]:
                m = j
                counterSwapped += 1
            swap(A,i,m)
            
        print(f"Numbers Compared {counterCompared}")
        print(f"Numbers Swapped {counterSwapped}")
        print(f"Partially Sorted Array {A}")

    return A


def bubblesort(A):
    """
    Bubble sort function that repeatedly steps through a list A,
    compares adjacent elements, 
    and swaps them if they are 
    in the wrong order.

    Parameters:
        A: List of elements to sort

    Returns:
        A: The list sorted in ascending order.
    """
    print("^^^^^^^^^^")
    for i in range(len(A)-1):
        counterSwapped = 0
        counterCompared = 0
        for j in range(len(A)-i-1):
            counterCompared += 1
            if A[j+1] < A[j]:
                swap(A, j+1, j)
                counterSwapped += 1
        print(f"Numbers Compared {counterCompared}")
        print(f"Numbers Swapped {counterSwapped}")
        if counterSwapped == 0:
            print("Array sorted exiting early.")
            return A
        print(f"Partially Sorted Array {A}")
    return A

# Example Array of Polynomial values from Problem 3
polyArray = [12.3,40.7,-9.1,7.7,6.4,0,8.9]

def power(x,p):
    """
    Calculated the number:x raised to the power p.

    Parameters:
        x: The value to be raised by the power p
        p: The exponential value to raise x to.
    
    Returns:
        product: The value of  x raised to p.
    """
    if p<0:
        print("Please enter a positive exponent.")
        return
    product = x
    for i in range(p-1):
        product *= x
    return product



def evaluate(A,x):
    """
    Uses the power function to evaluate the polynimial.

    Parameters: 
        A: List of values representing values in a polunomial.
        x: The known value used to solve the polunimial
    
    Returns:
        totalvalue: The total value of the evaluated polynomial.
    """
    print("^^^^^^^^^^")
    totalvalue = 0
    for i in range(len(A)):
        num = 0
        if i == 0:
            num = A[i]
        else:
            num = power(x,i) #Time complexity if O(n)
            num = A[i] * num
        totalvalue += num
    return totalvalue




if __name__=="__main__":
    # Runs and prints the outcome of the selection sort for Problem 1
    print(f"Final Selection Sorted Array Ascending Order{selectionsort(A1)}")
    print(f"Final Selection Sorted Array Ascending Order{selectionsort(A2)}")
    print(f"Final Selection Sorted Array Ascending Order{selectionsort(A3)}")
    # Runs and prints the outcome of the bubble sort for Problem 2
    print(f"Final Bubble Sorted Array Ascending Order{bubblesort(A4)}")
    print(f"Final Bubble Sorted Array Ascending Order{bubblesort(A5)}")
    print(f"Final Bubble Sorted Array Ascending Order{bubblesort(A6)}")
    # Runs and prints the evaluate function for Problem 3
    print(f"Evaluated polynomiial from Problem 3 {evaluate(polyArray,5.4)}")
    print("Time complexity of evaluate function is O(n^2)")
