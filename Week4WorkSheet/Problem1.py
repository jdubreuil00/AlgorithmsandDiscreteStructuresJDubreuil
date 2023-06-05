import math
numbers = [1,2,3,4,5,6,7,8,9,10]

def logproblem(num):
    for number in num:
        print(round(math.log2(number)))

def squareRootProblem(num):
    for number in num:
        print(round(math.sqrt(number)))

def nlogproblem(num):
    for number in num:
        print(round(number * math.log2(number)))

def exponentProblem(num, exp):
    for number in num:
        print(round(number ** exp))

def exponentProblem2(num):
    for number in num:
        print(round(2 ** number))

def factorialProblem(num):
    for number in num:
        print(round(math.factorial(number)))

print('====== lg(n)')
logproblem(numbers)
print('====== sqrt(n)')
squareRootProblem(numbers)
print('====== nlg(n)')
nlogproblem(numbers)
print('====== n^2')
exponentProblem(numbers, 2)
print('====== n^3')
exponentProblem(numbers, 3)
print('====== 2^n')
exponentProblem2(numbers)
print('====== n!')
factorialProblem(numbers)
print('======')

