from math import ceil, floor

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