import numpy as np
 
print("1. CREATING ARRAYS")

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
rng = np.arange(0, 10, 2)# start, stop, step
lin = np.linspace(0, 1, 5)# 5 evenly spaced values
 
print("1D array a:", a)
print("2D array b:\n", b)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Range array:", rng)
print("Linspace array:", lin)
 
 
print("2. ARRAY PROPERTIES")
print("Shape of b:", b.shape)
print("Dimensions of b:", b.ndim)
print("Total elements in b:", b.size)
print("Data type of b:", b.dtype)
 
print("3. MATHEMATICAL OPERATIONS (element-wise)")
 
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
 
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x ** 2 =", x ** 2)
print("sqrt(x) =", np.sqrt(x))
print("exp(x) =", np.exp(x))
print("log(x) =", np.log(x))
 
print("4. AGGREGATE / STATISTICAL FUNCTIONS")
 
data = np.array([12, 45, 7, 23, 56, 89, 34])
 
print("Data:", data)
print("Sum:", data.sum())
print("Mean:", data.mean())
print("Max:", data.max())
print("Min:", data.min())
print("Standard Deviation:", data.std())
print("Variance:", data.var())
  
print("5. MATRIX OPERATIONS")
 
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
 
print("m1:\n", m1)
print("m2:\n", m2)
print("Matrix multiplication (m1 @ m2):\n", m1 @ m2)
print("Transpose of m1:\n", m1.T)
print("Determinant of m1:", np.linalg.det(m1))
print("Inverse of m1:\n", np.linalg.inv(m1))
 
print("6. INDEXING AND SLICING")

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)
print("First element:", arr[0])
print("Slice [1:4]:", arr[1:4])
print("Elements greater than 20:", arr[arr > 20])
 
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatrix:\n", matrix)
print("Element at row 0, col 1:", matrix[0, 1])
print("Entire column 1:", matrix[:, 1])
print("Entire row 1:", matrix[1, :])
 
 
print("7. MINI TASK: Custom array calculation")
 
# Create an array of 10 numbers and perform calculations
nums = np.arange(1, 11)
print("Numbers 1-10:", nums)
print("Squares:", nums ** 2)
print("Sum of squares:", np.sum(nums ** 2))
print("Average:", nums.mean())
print("Even numbers only:", nums[nums % 2 == 0])

print("RESHAPING ARRAYS")
numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)
reshaped = numbers.reshape(3, 4)
print("\nReshaped Array (3x4):",reshaped)

print("\n" + "=" * 50)
print("8. CONCATENATING ARRAYS")
print("=" * 50)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
combined = np.concatenate((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Combined Array:", combined)
