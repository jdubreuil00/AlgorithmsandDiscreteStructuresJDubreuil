def finddiff(A,B):
    """
    Takes two Arrays (A and B) and compares A to B. If a value
    in A does not exist in B it adds the value that does not exist
    in B into and array C. Once the algorithm is complete the values that
    do not exsist in B are returned.

    Parameters:
        A: The values we are checking to see if they are in Array B
        B: The Values we are checking agaist A.
    
    Returns:
        C: The list of values from A that do not exist in B
    """
    C =[]
    for i in range(len(A)):
        inarray = False
        for j in range(len(B)):
            if A[i] == B[j]:
                inarray = True
                
        if not inarray:
            C.append(A[i])
    return C

A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
B = [35, 45, 55, 60, 50, 40]

print(finddiff(A,B))


