# Importing text file data
numbers = []
with open('input_dgrcode_20_1000000.txt', 'r') as IntegerArray:
  for number in IntegerArray:
    numbers.append(int(number.strip()))

# Function to perform quicksort swaps given an array
'''
Input: Array, start index, length of array
Output: Sorted array, number of comparisons and index of split
'''
def quickSortSwaps(array, firstIndex, lengthOfArray):

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

