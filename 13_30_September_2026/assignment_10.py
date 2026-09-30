import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("First 5:", arr[:5])
print("Last 5:", arr[5:])
print("Elements 3 to 7:", arr[2:7])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5

print("After Broadcasting:", arr)