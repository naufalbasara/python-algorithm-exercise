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


def search(array, target):
    array.sort()
    return binarySearch(array, target)


array = [-1,0,3,5,9,12]
print(search(array, 100))