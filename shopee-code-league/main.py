# # 2021
def highestMountain():
    test_case = int(input())

    result = []
    for i in range(test_case):
        length = int(input())
        sequence = list(map(int, input().split(" ")))
        print(sequence)

    def highMountain():
        height = 0
        index = 0
        return height, index


# 2022
# Money Transfer
def transfer():
    case = list(map(int, input().split()))
    username, transaction = case[0], case[1]
    userData = {}

    # input user balance
    for i in range(username):
        userBalance = input().split(" ")
        name, balance = userBalance[0], int(userBalance[1])
        userData.update({name: balance})

    # begin transaction
    for i in range(transaction):
        userTransaction = input().split(" ")
        sender, receiver, amount = userTransaction[0], userTransaction[1], int(userTransaction[2])
        if userData[sender] < amount:
            continue
        else:
            userData[sender], userData[receiver] = userData[sender] - amount, userData[receiver] + amount
    
    # print result
    for x in userData:
        print(x, userData[x])


# # Installation of a Shopee Billboard
def installation():
    case = int(input())
    barLength = list(map(int, input().split(" ")))
    if len(barLength) != case:
        raise Exception("Error")

    lastNum = barLength[len(barLength)-1]
    total = 0
    for i in range(len(barLength)-1):
        total += barLength[i]
    
    # checking
    if lastNum != total:
        return 0
    else:
        return total

# fireworks festival


if __name__ == "__main__":
    transfer()