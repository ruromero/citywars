from __future__ import division
import random
import hero
import generator
from group import group

firstwordsleague = generator.wordlist("firstwordsleague")
lastwordsleague = generator.wordlist("lastwordsleague")

def firstname():
    return firstwordsleague[random.randint(0,len(firstwordsleague)-1)]

def lastname():
    return lastwordsleague[random.randint(0,len(lastwordsleague)-1)]

def name():
    return firstname() + " " + lastname()

class league(group):
    def __init__(self,e):
        group.__init__(self,e)
        self.name = self.genName()
        self.leader = hero.hero(self.e,self)
        self.active = 1
        self.members = [self.leader]
        i = 0
        j = random.randint(3,4)
        while i < j:
            self.members.append(hero.hero(self.e,self))
            i += 1

    def getActive(self):
        return self.active

    def setActive(self,state):
        self.active = state

    def newMember(self):
        self.members.append(hero.hero(self.e,self))

    def genName(self):
        self.firstn = firstname()
        self.lastn = lastname()
        return self.firstn + " " + self.lastn
    
    def regenName(self):
        self.firstn = firstname()
        self.name = self.firstn + " " + self.lastn
