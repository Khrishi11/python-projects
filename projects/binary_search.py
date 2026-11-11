# Project 2: Binary Search Algorithm
# You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.


# Setting up the binary search function
def binarySearch(arr, targetVal):
  # Initialize the left and right pointers
  left = 0
  right = len(arr) - 1
  # Implementing the binary search algorithm
  while left <= right:
    mid = (left + right) // 2
    # Check if the target value is present at mid
    if arr[mid] == targetVal:
      return mid
    # If the target value is greater, ignore the left half
    if arr[mid] < targetVal:
      left = mid + 1
    # If the target value is smaller, ignore the right half
    else:
      right = mid - 1

  return -1

# These are the test cases to check the implementation of the binary search algorithm.
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

# Output the result of the binary search
if result != -1:
  print("Found at index", result)
else:
  print("Not found")