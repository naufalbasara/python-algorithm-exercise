def wordSearch(test_case):
    for case in range(1, test_case+1):
        userInput = []
        for _ in range(4):
            userInput.append(input())
        
        n, m, grid, w = userInput


        
        
        arr = [
            ['c', 'a', 't', 't'],
            ['a', 'a', 't', 'a'],
            ['t', 'a', 't', 'c'],
        ]
        word = 'cat'

    return
    

if __name__ == '__main__':
    test_case = int(input())
    wordSearch(test_case)