"""
Worksheet 1 part 2 zigzag
Jordan Dubreuil
5/8/2023
"""
def zigzag(a,b,c):
    """
    The zigzag funtion takes in three numeric values and checks to see if the
    cobmination of values is ascending to decending or decending to ascending.

    Parameters:
        a: number
        b: number
        c: number
    
    Returns:
        True: The combination of values are either ascending to decending or decending to ascending.
        True: The combination of values are not ascending to decending or decending to ascending.
    
    """
    if a<b>c or a>b<c:
        return True
    else:
        return False


# Test functions below will only be called if this is the main calling class. 
if __name__ == "__main__":
    print(zigzag(1,2,3))
    print(zigzag(3,1,4))
    print(zigzag(8,2,7))
    print(zigzag(10,7,6))
    print(zigzag(21,25,17))
