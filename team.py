class team:

    def __init__(self, ranking):
        self.ranking = ranking
        self.balance = 0

    def changeBalance(self, inc):
        self.balance += inc

    def getRanking(self):
        return self.ranking

    def getBalance(self):
        return self.balance
