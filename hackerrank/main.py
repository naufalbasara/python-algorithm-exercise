import math

# Barunastra Coding Test 2021
# Nala 10
number = input().split(" ")

# loop
n = 1
for i in range(int(number[0])):
    n *= int(number[1])
    print(n)

# iteration
def power(n, t):
    result = 1
    if n>1:
        power(n-1, t)
        print(t**n)
        return
    else:
        print(t*result)
        return

print(power(int(number[0]), int(number[1])))


# BANDITS
trials = int(input())

scores = []
for i in range(trials):
    scores.append(int(input()))
    scores.sort()

for i in range(len(scores)):
    print(scores[i])


# Holen The Cable Inspector
length = int(input())

segments = list(map(int, input().split(" ")))
taken = int(input())

def leftInspect(length, segments, taken):
    if len(segments) != length:
        return 0
    else:
        best = 0
        index = 0
        for i in range(len(segments)-taken):
            if best<=sum(segments[i:i+taken]):
                index = i
            else:
                continue
        return index

# Mekari mockup test
arr = [3, 5, -1, 8, 12]

def ArrayAddition(arr):
    # code goes here
    arr.sort()
    largest = arr[-1]
    del arr[0]

    total = 0
    for i in range(len(arr) - 1):
        total += arr[i]
    if total < largest:
        print(arr)
        print(len(arr) - 1)
        return "false"
    else:
        print(len(arr)-1)
        return "true"

# keep this function call here
print(ArrayAddition(arr))

def print_formatted(number):
    width = len("{:b}".format(number))
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
    return


# designer door mat hackerrank
def center(length, string, separator):
    return print(separator* int((length - len(string))/2), separator* int((length - len(string))/2), sep=string)

n, m = map(int, input().split(" "))

def designer_door_mat(n, m):
    init = 1
    for i in range(1, n+1):
        if i < math.ceil(n / 2):
            # run normal triangle
            center(m, init*".|.", "-")
            init +=2
        elif i == math.ceil(n/2):
            center(m, "WELCOME", "-")
        else:
            # run upside down triangle
            init -= 2
            center(m, init * ".|.", "-")
    return