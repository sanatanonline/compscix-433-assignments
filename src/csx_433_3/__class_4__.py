import numpy as np

print(np.__version__)

arr1 = np.arange(0, 10, 1, dtype=np.int32)
print(arr1)

arr2 = np.array(np.arange(0, 10, 1, dtype=np.int32))
print(arr2)

arr3 = np.full((3, 3), True, dtype=bool)
print(arr3)

arr4 = arr1[arr1 % 2 == 1]
print(arr4)

arr1[arr1 % 2 == 1] = -1
print(arr1)


