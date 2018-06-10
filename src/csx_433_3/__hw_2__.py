# 1. Include a section with your name

"""
Name : Sanatan Das
Email : sanatanonline@gmail.com
GitHub URL : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_3/__hw_2__.py

"""

from numpy import random, matrix, dot, absolute
from sys import getsizeof

# 2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)

# Create the vector
A = random.random(15)
# Reshape it
A = A.reshape(3, 5)
# Convert to matrix
A = matrix(A)
# Print the type of A
print(type(A))

# 3. Find the size and length of matrix A

# Find the size of A
A_SIZE = A.size
print("Size of A is:")
print(A_SIZE)
# Find the length of A
A_LENGTH = len(A)
print("Length of A is:")
print(A_LENGTH)
# Find the total size
print("Total size of A is:")
A_TOTAL_SIZE = getsizeof(A)
print(A_TOTAL_SIZE)
# Find the item size
print("Item size of A is:")
A_ITEM_SIZE = A.itemsize
print(A_ITEM_SIZE)

# 4. Resize (crop/slice) matrix A to size (3,4)

# Cannot reshape(3,4) for the array size 15 using reshape
# A.reshape(3,4)
# So,using A[:,:4]
A = A[:, :4]
print("Reshaped A:")
print(A.shape)

# 5. Find the transpose of matrix A and assign it to B

B = A.T
print("B is transpose of A. B is:")
print(B)

# 6. Find the minimum value in column 1 of matrix B (check the properties of a matrix – ‘B.min()’)

B_MIN = min(B[:, 1])
print("Min value of B is:")
print(B_MIN)

# 7. Find the minimum and maximum values for the entire matrix A

A_MIN = A.min()
print("Min value of A is:")
print(A_MIN)
A_MAX = A.max()
print("Max values of A is:")
print(A_MAX)

# 8. Create vector X (an array) with 4 random numbers

X = random.random(4)
print(X)

# 9. Create a function and pass vector X and matrix A in it
# 10. In the new function multiply vector X with matrix A and assign the result to D


def mul_func(x, a):
    print('X is: ', x)
    print('A is: ', a)
    # Shapes X (1,4) and A (3,4) are not aligned: 4 != 3
    # D = dot(X,A.T) or X*A.T gives same result as dot(A,X.T)
    # But A*X.T doesn't work as X is a vector so shape(X.T)=shape(X) i.e. (1,4).
    # If X was a matrix, then A*X.T would work too.
    d = dot(x, a.T)
    return d


# Call the function mul_func
D = mul_func(X, A)
print('D is : ', D)


# 11. Create a complex number Z with absolute and real parts != 0

Z = complex(3, 4)

# 12. Show its real and imaginary parts as well as it’s absolute value

# Print real part
Z_REAL = Z.real
print(Z_REAL)
# Print imaginary part
Z_IMAGINE = Z.imag
print(Z_REAL)
# Print the absolute value
Z_ABS = absolute(Z)
print(Z_ABS)

# 13. Multiply result D with the absolute value of Z and record it to C

C = D * Z_ABS
print(D)

# 14. Convert matrix B from a matrix to a string and overwrite B

B = B.tolist()
B = [str(x) for x in B]
print(B)

# Display a text on the screen: ‘Your Name is done with HW2‘

print(input('Name:') + ' is done with HW2')
# Name:Sanatan
# Sanatan is done with HW2






