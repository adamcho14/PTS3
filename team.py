class team:

    def __init__(self, name, ranking):
        self.ranking = ranking
        self.balance = 0
        self.name = name

    def changeBalance(self, inc):
        self.balance += inc

    def getRanking(self):
        return self.ranking

    def getBalance(self):
        return self.balance

    def setRanking(self, ranking):
        self.ranking = ranking

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
