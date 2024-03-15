

# HackerRank Python Challenge 1 - INTRODUCTION CHALLENGES

#  if __name__ == '__main__':
#     print('Hello, World!')



# HackerRank Python Challenge 2

# if __name__ == '__main__':
#     n = int(input().strip())
# Provided solution here
#     if 1<= n <= 100:
#         if n%2 != 0:
#             print('Weird')
#         elif n%2 == 0 and n in range(2,5):
#             print('Not Weird')
#         elif n%2 == 0 and n in range(6,21):
#             print('Weird')
#         elif n%2 == 0 and n > 20 <= 100:
#             print('Not Weird')



# HackerRank Python Challenge 3

'''
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Constrains
1<= a <= 10**10
1<= b <= 10**10
'''

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# Provided solution here
#     if 1<= a <= 10**10 and 1<= b <= 10**10:
#         print(a + b)
#         print(a - b)
#         print(a * b)



# HackerRank Python Challenge 4

"""
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     # Provided solution here
#     print(a//b)
#     print(a/b)



# HackerRank Python Challenge 5

"""
Task
The provided code stub reads and integer, n , from STDIN. For all non-negative integers,
i < n , print i**2. 

Constrains
1<= n <= 20
"""

# if __name__ == '__main__':
#     n = int(input())
#     print()
#     print()
#     # Provided solution here
#     if 1 <= n <= 20:
#         for i in range(0, n):
#             print(i**2)



# HackerRank Python Challenge 6

"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Constrains
1900 <= year <= 10**5
"""

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0:
#             leap = False
#             if year % 400 == 0:
#                 leap = True
#     else:
#         leap = False

#     return leap

# year = int(input())

# if __name__ == '__main__':
#     print(is_leap(year))



# HackerRank Python Challenge 7

"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:

123....n

Note that "...." represents the consecutive values in between.

Example

n=5
Print the string "12345".

Input Format

The first line contains an integer n.

Constrains
1 <= n <= 150
"""

# if __name__ == '__main__':
#     n = int(input())

#     # Enter your code here
#     if 1 <= n <= 150:
#         for i in range(1, n+1):
#             print(i,end='')



# HackerRank Python Challenge 8 - INTERMEDIATE CHALLENGES

"""

The zeros tool returns a new array with a given shape and type filled with 's.

import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]


The ones tool returns a new array with a given shape and type filled with 's.

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]


Task

You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, your task is to print 
an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Constraints
1<= each_integer <= 3

"""

# import numpy
# import sys

# # Creating a function that prints the matrixes using the 
# # provided input numbers, pasing them to Numpy zeros, ones, etc tools

# def build_matrixes():
#     # Accepting 3 space separated integers as string input
#     dimensions_in = input()

#     # Using split function to remove spaces, then:
#     # Converting each space separated integers and storing them back into a list
#     # ready to iterate later on
#     dimensions = []
#     for dim in dimensions_in.split():
#         if int(dim) < 1 or int(dim) > 3:
#             print('One or more of the selected values does not comply with constrains.\nPlease, enter values between 1 and 3.')
#             sys.exit()
#         else:
#             dimensions.append(int(dim))

    # """
    # Testing Point

    # print()
    # print(dimensions)
    # print(len(dimensions))
    # print()
    # """

    # """
    # Explored the option of creating dynamic variables for different Dimensions

    # # # Create a list to hold dynamically created variables
    # # dim_dyn_vars = []
    # # # Create a dictionary to map the newly created variables to the proper dim values
    # # dim_dict = {}

    # # # Create dynamic dimension variables and assign the input values in the same order
    # # # as entered to each dim_dict key
    # # for d in range(len(dimensions)):
    # #     dim_dyn_vars.append('d' + str(d+1))
    
    # # for d, num in zip(dim_dyn_vars, dimensions):
    # #     dim_dict[f'{d}'] = num

    # # print(dim_dyn_vars)
    # # print()
    # # print(dim_dict)
    # # print()

    # # Now that the dimension variables are dynamically generated,
    # # will convert the resulting dinctionary values into a LIST,
    # # to be passed into the numpy.zeros and numpy.ones functions
    # # First, we need to iterate through the dictionary values and make sure,
    # # the values are within between 1 and 3

    # # dimensions_list = []

    # # for d_number in dim_dict.values():
    # #     if 1<= d_number <= 3:
    # #         dimensions_list.append(d_number)
        
    # # print(dimensions_list)
    # """

    # # Initializing lists to hold matrixes
    # zeros_mtxs = numpy.zeros((dimensions), dtype=int)
    # ones_mtxs = numpy.ones((dimensions), dtype=int)

    # print(zeros_mtxs)
    # print(ones_mtxs)

    # """
    # Explored and tested "Stacking" Matrixes
    # # Filling lists with matrixes of 0's and 1's depending on input integers
    # # Append matrixes with zeros to the reference list
    # # for d_number in dim_dict:
    # #     if 1<= d_number <= 3:
    # #         zeros_mtxs.append(numpy.zeros((number, number), dtype=int))
    # # # Append matrixes with ones to the reference list
    # #         ones_mtxs.append(numpy.ones((number, number), dtype=int))

    # # Stack the matrixes to form 3D arrays
    # # Zeros Stack
    # # if zeros_mtxs: # Check if list is NOT empty
    # #     zero_3d = numpy.stack(zeros_mtxs)
    # #     print(zero_3d)
    # # # Ones Stack
    # # if ones_mtxs: # Check if the list is NOT empty
    # #     ones_3d = numpy.stack(ones_mtxs)
    # #     print(ones_3d)
    # """

# if __name__ == "__main__":
#     build_matrixes()



# HackerRank Python Challenge 9 - INTERMEDIATE CHALLENGES

"""
identity

The identity tool returns an identity array. An identity array is a square matrix,
with all the main diagonal elements as 1 and the rest as 0. The default type of
elements is float.

import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

eye

The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere.
The diagonal can be main, upper or lower depending on the optional parameter k.
A positive k, is for the upper diagonal, a negative k, is for the lower, and a 0 k
(default) is for the main diagonal.


import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.


Task

Your task is to print an array of size NxM with its main diagonal elements,
as 1's and 0's everywhere else.


Note

In order to get alignment correct, please insert the line:

'numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format

A single line containing the space separated values of N and M.

N denotes the rows.
M denotes the columns.

Sample Input
3 3

Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""

# import numpy as np
# np.set_printoptions(legacy='1.13')

# def build_identity_and_eye():
#     # Accepting 2 numbers as NxM format
#     # Request user for a 2 space separated numbers string, to denote N for rows and
#     # M for columns
#     NxM = input()
    
#     # Using split function to remove spaces, then:
#     # Converting each space separated numbers into integers
#     # and storing them back into a list ready to iterate later on
#     dimensions = [int(num) for num in NxM.split()]

#     # print(dimensions) # Testing Point

#     if len(dimensions) != 2: # Checking if NxM format has been provided as input
#         print('The provided input does not comply with NxM format.\nPlease enter 2 numbers.')
#     elif dimensions[0] == dimensions[1]: # Checking if NxM IS square and if so, print identity
#         print(np.identity(dimensions[0]))
#     elif dimensions[0] != dimensions[1]: # Checking if NxM is NOT square and if so, print eye
#         print(np.eye(dimensions[0], dimensions[1], k = 0)) # Print eye with main diagonal
#     else:
#         print('An Error Occured, please try again')

# if __name__ == '__main__':
#     build_identity_and_eye()



# HackerRank Python Challenge 10 - INTERMEDIATE CHALLENGES

"""
Basic mathematical functions operate element-wise on arrays.
They are available both as operator overloads and as functions in the NumPy module.

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]


Task

You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)


Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format

The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

Output Format

Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

Use // for division in Python 3.
"""

# # Import NumPy
# import numpy as np

# # Define a function that given 2 NxM integer arrays, A and B, the function will perform
# # A + B, A - B, A * B, A / B, A % B and A ** B.

# def array_calculator():
#     # Request user input for dimensions
#     N, M = map(int, input("Enter dimensions N and M separated by space: ").split()) # Remove print text for actual code submission

#     # Request user input for array A
#     # print("Enter elements of array A:")
#     A = np.array([list(map(int, input().split())) for element in range(N)])

#     # Request user input for array B
#     # print("Enter elements of array B:")
#     B = np.array([list(map(int, input().split())) for element in range(N)])

#     # Getting Matrix A dimensions
#     dimensions_A = A.shape
#     rows_A, columns_A = dimensions_A

#     # Getting Matrix B dimensions
#     dimensions_B = B.shape
#     rows_B, columns_B = dimensions_B

#     # Verify that both arrays A and B, have the same M
#     if columns_A != columns_B:
#         print('Matrixes do not have the same M value. Please enter matching M values.')
#     elif columns_A == columns_B:
#         # Perform A + B operation
#         print(A + B)
#         # Perform A - B operation
#         print(A - B)
#         # Perform A * B operation
#         print(A * B)
#         # Perform A / B operation
#         print(A // B)
#         # Perform A % B operation
#         print(A % B)
#         # Perform A ** B operation
#         print(A ** B)

# # Call the function
# if __name__ == '__main__':
#     array_calculator()



# HackerRank Python Challenge 11 - INTERMEDIATE CHALLENGES

"""

"""