# ==========================
# NumPy Basics Cheat-Sheet
# ==========================

import numpy as np  # Import NumPy

# --------------------------
# 1. Creating arrays
# --------------------------
a = np.array([1, 2, 3])          # 1D array
b = np.array([[1, 2], [3, 4]])   # 2D array (matrix)

print("=== Arrays ===")  # Section header
print("a =", a)          # Print 1D array
print("b =\n", b)        # Print 2D array with newline for readability

# --------------------------
# 2. Array information
# --------------------------
print("\n=== Array Info ===")
print("a.shape =", a.shape)  # Shape of array a
print("b.shape =", b.shape)  # Shape of array b
print("a.ndim =", a.ndim)    # Number of dimensions for a
print("b.ndim =", b.ndim)    # Number of dimensions for b
print("a.dtype =", a.dtype)  # Data type of elements in a

# --------------------------
# 3. Basic operations
# --------------------------
print("\n=== Basic Operations ===")
print("a + 1 =", a + 1)          # Add 1 to each element
print("a * 2 =", a * 2)          # Multiply each element by 2
print("b + b =\n", b + b)        # Element-wise addition of 2D arrays
print("np.dot(b, b) =\n", np.dot(b, b))  # Matrix multiplication

# --------------------------
# 4. Accessing elements
# --------------------------
print("\n=== Accessing Elements ===")
print("b[0,1] =", b[0,1])  # First row, second column
print("b[:,1] =", b[:,1])  # All rows, second column
print("b[1,:] =", b[1,:])  # Second row

# --------------------------
# 5. Useful functions
# --------------------------
print("\n=== Useful Functions ===")
print("np.sum(a) =", np.sum(a))       # Sum of elements
print("np.mean(a) =", np.mean(a))     # Mean of elements
print("np.max(a) =", np.max(a))       # Maximum value
print("np.min(a) =", np.min(a))       # Minimum value
print("np.random.rand(3) =", np.random.rand(3))  # 3 random numbers between 0 and 1
