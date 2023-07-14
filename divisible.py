def countDivisible(test_case):
    # Loop over test case
    answer = []
    for case in range(1, test_case+1):
        inputted = []
        numOfDivisible = 0

        for _ in range(3):
            try:
                inputted.append(int(input()))
            except:
                print("input must be integer more than 1 and less than 10000")

        a, b, k = inputted

        arr = [True for num in range(a, b+1) if num % k==0]
        numOfDivisible = sum(arr)
        answer.append((case, numOfDivisible))

    for case in answer:
        print(f"Case {case[0]}: {case[1]}")

if __name__ == '__main__':
    test_case = int(input())
    countDivisible(test_case)