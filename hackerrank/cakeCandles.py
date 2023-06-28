import os

def birthdayCakeCandles(candles):
    # Write your code here
    max = 0
    for num in candles:
        if num > max:
            max = num
    maxCount = candles.count(max)
    return maxCount

array = [3, 2, 1, 3]
print(birthdayCakeCandles(array))