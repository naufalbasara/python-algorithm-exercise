def foo(arr, a, b, i, j):
    k = j
    ct =0

    while k > i-1:
        if arr[k] <= b and not arr[k]<=a:
            ct+=1

        k-=1
    
    return ct

print(1750/8000)