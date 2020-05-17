# Importing text file data
numbers = []
with open('QuickSort.txt', 'r') as IntegerArray:
  for number in IntegerArray:
    numbers.append(number.strip())


# Function to perform quick sort swaps
'''
Input: Takes and array and index of the pivot element as input
Output: Returns partitioned array with left sub-array less than pivot
        and right sub-array greater than pivot
'''
def quickSortSwap(array):
  pivot = array[0]
  pivotIndex = 1
  numberOfComparisons = len(array)-1
  for comparisonIndex in range(1, len(array)):
    if pivot > array[comparisonIndex]:
      array[pivotIndex], array[comparisonIndex] = array[comparisonIndex], array[pivotIndex]
      pivotIndex += 1
  array[0], array[pivotIndex-1] = array[pivotIndex-1], array[0]
  return (array, pivotIndex-1, numberOfComparisons)



# Function to count number of comparison while performing quick sort
'''
Input: Takes an array of numbers
Output: Return number of total comparisons
'''
def countNumberOfComparisons(array):
  lengthArray = len(array)
  if lengthArray <= 1:
    return (array,0)
  else:
     array, splitIndex, comparisons = quickSortSwap(array)
     array[:splitIndex], leftComparisons = countNumberOfComparisons(array[:splitIndex])
     array[splitIndex+1:], rightComparisons = countNumberOfComparisons(array[splitIndex+1:])
     totalComparisons = comparisons + leftComparisons + rightComparisons

     return (array, totalComparisons)


if __name__ == "__main__":

  print(countNumberOfComparisons(numbers)[1])

