## ---------------- Program to count inversions ---------------- ##

import math

# Importing text file data
numbers = []
with open('IntegerArray.txt', 'r') as IntegerArray:
  for number in IntegerArray:
    numbers.append(number)

numbers = list(map(int, numbers))

# Function to merge two arrays in sorted manner and count inversions
'''
Input: 2 arrays
Output: Merged array in sorted order and counted numbers of inversions
'''
def mergeCountInversions(numbers):

  lengthArray = len(numbers)
  # Base case
  if lengthArray <= 1:
    return (numbers, 0)
  else:
    middlePoint = math.floor(lengthArray / 2)
    leftArray = numbers[:middlePoint]
    rightArray = numbers[middlePoint:]

    leftArray, leftInversions = mergeCountInversions(leftArray)
    rightArray, rightInversions = mergeCountInversions(rightArray)
    inversions = 0 + leftInversions + rightInversions
    sortedArray, leftIndex, rightIndex = [], 0, 0

    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
      if leftArray[leftIndex] < rightArray[rightIndex]:
        sortedArray.append(leftArray[leftIndex])
        leftIndex += 1
      else:
        sortedArray.append(rightArray[rightIndex])
        inversions += len(leftArray) - leftIndex
        rightIndex += 1

    sortedArray += leftArray[leftIndex:]
    sortedArray += rightArray[rightIndex:]

    return (sortedArray, inversions)



if __name__ == "__main__":

  print(mergeCountInversions(numbers)[1])


