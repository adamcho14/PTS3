import math
from random import randint

import team

teams = ()

class round:

    teams = []
    games = {}

    def __init__(self):
        pass

    def __init__(self, teams):
        for team in teams:
            self.teams.append(team)

    def addTeam(self, team):
        self.teams.append(team)

    def status(self, team):
        return (1 - team.getRanking/len(self.teams))*100 + team.balance

    def rPG(self, a, b):  #randPresudoGaussian
        return a * math.e ** (- ((randint(0,10) - b) ** 2) / 2)

    def match(self, team1, team2):
        s1 = self.status(team1)
        s2 = self.status(team2)

        res1 = math.ceil(self.rPG(s1, s2))
        res2 = math.ceil(self.rPG(s2, s1))

        if res1 > res2:
            team1.balance += 2
        if res2 > res1:
            team2.balance += 2
        else:
            team1.balance += 1
            team2.balance += 1

        self.games[(team1, team2)] = (res1, res2)

    def play(self):

        for team1 in self.teams:
            for team2 in self.teams:
                if team1 != team2:
                    self.match(team1, team2)
                    self.match(team2, team1)

    def getGames(self):
        for team1 in self.teams:
            for team2 in self.teams:
                if team1 != team2:
                    print(team1.getName(), team2.getName(), ":", self.games[(team1, team2)][0], ":", self.games[(team1, team2)][1])







