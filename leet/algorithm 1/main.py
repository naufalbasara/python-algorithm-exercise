from audioop import reverse
import math

# linear search
def linearSearch(array, target): #memory issues
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
# recursive linear search
def recursiveLinearSearch(array, target, start):
    if array[start] == target:
        return start
    else:
        return recursiveLinearSearch(array, target, start+1)


# recursive binary search
def recursiveBinarySearch(array, target, left, right):
    try:
        center = int((left + right)/2)
        if array[center] == target:
            return "{target} is in index {center} of the array".format(target = target, center=center)
        elif array[center] < target:
            return recursiveBinarySearch(array, target, center + 1, right)
        else:
            return recursiveBinarySearch(array, target, left, center-1)
    except:
        return "{target} was not found in the array".format(target = target)
# loop binary search
def binarySearch(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1


def search(array, target, type):
    array.sort()
    if type.lower() == "linear":
        return linearSearch(array, target)
    elif type.lower() == "binary":
        return binarySearch(array, target)

# First Loop Bad Version
def firstBadVersion(n):
    #isBadVersion() function is and API fetch through Leet Website 
    start = 1
    end = n

    while start <= end:
        mid = (start+end)//2
        if isBadVersion(mid) and not isBadVersion(mid-1): #if bad version and the previous is not bad, then its the first
            return mid
        elif not isBadVersion(mid): #if not bad version, check the rest next number
            start = mid + 1
        else: #if bad version and the previous is bad, then check previous
            end = mid - 1

# search insert position
def searchInsert(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return left

def recursiveSearchInsert(array, target, left, right):
    try:
        center = int((left + right)/2)
        if array[center] == target:
            return "{target} is in index {center} of the array".format(target = target, center=center)
        elif array[center] < target:
            return recursiveSearchInsert(array, target, center + 1, right)
        else:
            return recursiveSearchInsert(array, target, left, center-1)
    except:
        return left


# 977. Squares of a Sorted Array
def sortedSquares(array):
    return sorted(list(map(lambda x:x**2, array)))

# 189. Rotate Array
def rotate(array, steps): #time limit exceeded issue
    for i in range(steps):
        current = array[len(array)-1]
        array.insert(0, current)
        array.pop()
    return array

# using reverse function
def rotate(array, steps):
    # make reverse function
    def reverse(array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start+=1
            end-=1
        return array

    #if steps exceeded array length, get a modulo of steps and array length
    if steps > len(array):
        steps%=len(array)
    
    # reverse entire array
    array = reverse(array, 0, len(array)-1)
    # reverse the first element until steps-1
    array = reverse(array, 0, steps-1)
    # reverse the rest element of the array
    array = reverse(array, steps, len(array)-1)

    return array

# 283. Move Zeroes
def moveZeroes(array):
    current = 0
    end = len(array)-1

    while current < end:
        if array[current] == 0:
            array.pop(current)
            array.append(0)
            end -= 1
        else:
            current +=1
    return array

# 167. Two Sum II - Input Array Is Sorted
def twoSum(array, target): #time limit exceeded
    first = 0

    while first < len(array):
        for i in range(first+1, len(array)):
            if array[first] == array[i]:
                pass
            if array[first] + array[i] == target:
                return [first+1, i+1]
        first+=1
    return -1

def twoSum(array, target):
    first = 0
    end = len(array)-1

    while first <= end:
        sum = array[first] + array[end]
        if sum == target:
            return [first+1, end+1]
        elif sum < target:
            first+=1
        else:
            end-=1
    return [first+1, end+1]

# 344. Reverse String
def reverseString(string):
    return string[::-1]

def reverseString(string): #two pointers
    start = 0
    end = len(string)-1

    while start<end:
        string[start], string[end] = string[end], string[start]
        start+=1
        end-=1
    return string

# 557. Reverse Words in a String III
def reverseWords(string):
    string = string.split(" ")
    result = []
    for word in string:
        result.append(word[::-1])
    return " ".join(result)

def reverseWords(string): #two pointers approach
    start = 0
    end = start
    result = ""

    while end < len(string):
        if string[end] != " ":
            end +=1
            if len(string) <= end+1:
                result += string[start:end+1][::-1]
                break
        elif string[end] == " ":
            result += string[start:end][::-1]
            start = end+1
            end +=1
    return result