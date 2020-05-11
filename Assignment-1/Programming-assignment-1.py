'''
Program to multiply 2 numbers using Karastuba Algorithm
'''

# Importing math module
import math


# Function to mulitply to numbers using Karastuba algorithm
def karastubaMultiplication(x, y):

  xStr = str(x)
  yStr = str(y)

  if (x < 10) or (y < 10):

    return x * y

  else:

    # if len(xStr) % 2 != 0:
    #   xStr = '0' + xStr

    # if len(yStr) % 2 != 0:
    #   yStr = '0' + yStr

    mx = len(xStr)
    my = len(yStr)

    if mx > my:
      yStr = '0' * (mx - my) + yStr

    else:
      xStr = '0' * (my - mx) + xStr


    length = len(xStr)
    splitPosition = math.floor(length / 2)

    high1, low1 = int(xStr[: - splitPosition]), int(xStr[-splitPosition:])
    high2, low2 = int(yStr[: - splitPosition]), int(yStr[-splitPosition:])

    z0 = karastubaMultiplication(low1, low2)
    z1 = karastubaMultiplication((low1 + high1), (low2 + high2))
    z2 = karastubaMultiplication(high1, high2)

    return (z2*10**(2*splitPosition)) + ((z1-z2-z0)*10**(splitPosition))+ z0




if __name__ == "__main__":

  x = int(input("Input first number:"))
  y = int(input("Input second number:"))

  # print(getNumDigits((x)))
  # print(getPartDigits(x))

  print(karastubaMultiplication(x,y))