def Maximum(A, right):
    if right == 0:
        return A[right]
    else:
        # values in each call
        print(f"Values of call {A, right - 1}")
        currentmax = Maximum(A, right - 1)
        # value returned by the call
        print(f"Values returned {currentmax}")

        # Values compared 
        print(f"Values compared {A[right], currentmax}")
        if A[right] > currentmax:
            # print result 
            print(f"Return result {A[right]}")
            return A[right]
        else:
            # print result 
            print(f"Return result {currentmax}")
            return currentmax

if __name__=="__main__":
    A = [17, 62, 49, 73, 26, 51]
    maxnumber = Maximum(A, len(A) - 1)
    print("Maximum number:", maxnumber)