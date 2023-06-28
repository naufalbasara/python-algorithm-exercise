def isMagicSquare(arr):
    isTrue = False

    if len(arr) != len(arr[0]):
        return isTrue

    rowLen = len(arr[0])
    rowSum = sum(arr[0])
    for _ in arr:
        if len(_) != rowLen:
            return isTrue
        if sum(_) != rowSum:
            return isTrue
        continue

    leftDiag = 0
    rightDiag = 0
    for i in range(len(arr)):
        rightDiag += arr[i][len(arr)-1-i]
        for j in range(len(arr[0])):
            if i == j:
                leftDiag += arr[i][j]
    if rightDiag != leftDiag:
        return isTrue
    
    isTrue = True
    
    return isTrue


def change(money):
    denom = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    for den in denom:
        if money >= den:
            amount = money//den
            print(f"A total of {amount} IDR {den}")
            return change(money%den)
    
    return

def check_id():
    arr = ["Viqi", "Shabrina", "Belva", "Celine", "Jason", "Agnes", "Arumi", "Trista", "Indriyani", "Nailah"]
    sid = input("Enter SID: ")
    try:
        sid = int(sid)
        if sid <= 0 or sid > 10:
            return print("Student unknown")
        return print(arr[sid-1])
    except:
        if type(sid) != int:
            return print("Input must be a Number")
        return print("Student Unknown")

class Candidate():
    __id = None
    __name = None
    __votes = 0

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getVotes(self):
        return self.__votes
    
    def addVotes(self):
        self.__votes += 1


class Voter():
    __id = None
    __name = None
    __hasVoted = False

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def vote(self, candidate):
        if self.__hasVoted:
            return print(f"Hello {self.getName()}, you have previously casted your vote and cannot vote again")
        self.__hasVoted = True
        print(f"Hello {self.getName()}, thank you for casting your vote")
        return candidate.addVotes()


class VotingSystems():
    __candidates = []

    def __init__(self, candidates):
        for _ in candidates:
            self.__candidates.append(_)
    
    def displayVoteCount(self):
        for i in range(len(self.__candidates)):
            print(f"{i} {self.__candidates[i].getName()} {self.__candidates[i].getVotes()}")
        return
    
    def displayWinner(self):
        maxVote = 0
        winner_name = None
        for i in range(len(self.__candidates)):
            if self.__candidates[i].getVotes() == maxVote:
                return print("the election is a tie.")
            if self.__candidates[i].getVotes() > maxVote:
                maxVote = self.__candidates[i].getVotes()
                winner_name = self.__candidates[i].getName()
        
        print(f"The winner of the election is {winner_name} with a total vote of {maxVote}.")

class Election():

    c1 = Candidate(1, "Panji-Raditya")
    c2 = Candidate(2, "Arif-Prasetyo")

    v1 = Voter(11, "Rizki")
    v2 = Voter(22, "Khoirul")
    v3 = Voter(33, "Ananta")

    vs = VotingSystems([c1, c2])
    v1.vote(c1)
    v2.vote(c2)
    v1.vote(c2)
    
    vs.displayVoteCount()
    vs.displayWinner()

    pass