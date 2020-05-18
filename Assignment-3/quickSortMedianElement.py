# Importing numpy module
from numpy import median

# Importing text file data
numbers = []
with open('QuickSort.txt', 'r') as IntegerArray:
  for number in IntegerArray:
    numbers.append(int(number.strip()))

# Function to perform quicksort swaps given an array
# using median of first, last and middle element as pivot.
'''
Input: Array, start index, length of array
Output: Sorted array, number of comparisons and index of split
'''
def quickSortSwaps(array, firstIndex, lengthOfArray):

  # Find the middle index of the array
  if lengthOfArray % 2 == 0:
    middleIndex = int(lengthOfArray/2) - 1
  else:
    middleIndex = lengthOfArray // 2

  # Find the median element amongst first, last and middle element
  medianElement = median([array[firstIndex], array[middleIndex], array[-1]])

  # Swap first element with the pivot element
  if medianElement == array[middleIndex]:
    array[firstIndex], array[middleIndex] = array[middleIndex], array[firstIndex]
  elif medianElement == array[-1]:
    array[firstIndex], array[lengthOfArray - 1] = array[lengthOfArray - 1], array[firstIndex]

  pivotElement = array[firstIndex]
  partitionBoundary = firstIndex + 1

  for processedElementsBoundary in range(firstIndex + 1, lengthOfArray):
    if array[processedElementsBoundary] < pivotElement:
      array[partitionBoundary], array[processedElementsBoundary] = array[processedElementsBoundary], array[partitionBoundary]
      partitionBoundary += 1

  array[partitionBoundary - 1], array[firstIndex] = array[firstIndex], array[partitionBoundary - 1]
  splitIndex = partitionBoundary - 1

  return array, splitIndex, lengthOfArray - 1


# Function to count total number of swaps while performing quick sort
'''
Input: Array
Output: Total number of comparisons
'''
def countNumberOfComparisons(array):

  lengthArray = len(array)
  # Base case
  if lengthArray <= 1:
    return (array, 0)
  else:
    array, splitIndex, comparisons = quickSortSwaps(array, 0, lengthArray)
    array[:splitIndex], leftComparisons = countNumberOfComparisons(array[:splitIndex])
    array[splitIndex + 1:], rightComparisons = countNumberOfComparisons((array[splitIndex + 1:]))

    totalComparisons = comparisons + leftComparisons + rightComparisons

  return (array, totalComparisons)




if __name__ == "__main__":
  print(countNumberOfComparisons(numbers)[1])

