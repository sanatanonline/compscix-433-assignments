import numpy as np
import time
from numpy import arange

a = ([1, 2, 3, 4], [5, 6, 7, 8])

s = np.shape(a)

print(s)

num1 = int(input("Please enter a number: "))

x = arange(num1)
y = range(num1)

tic = time.clock()

toc = time.clock()

print(toc - tic)


