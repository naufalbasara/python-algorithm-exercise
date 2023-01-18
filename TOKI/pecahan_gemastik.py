def pecahan(arr1, arr2):
    a, b = [int(x) for x in arr1]
    c, d = [int(x) for x in arr2]

    if (a / b) < (c / d):
        return ('lebih kecil')
    elif (a / b) > (c / d):
        return ('lebih besar')
    else:
        return ('sama')


if __name__ == '__main__':
    arr1 = input().split()
    arr2 = input().split()
    print(pecahan(arr1, arr2))