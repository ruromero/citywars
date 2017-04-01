import random
import generator
import business

firstwordsblock = generator.wordlist("firstwordsblock")
lastwordsblock = generator.wordlist("lastwordsblock")

def firstname():
    return firstwordsblock[random.randint(0,len(firstwordsblock)-1)]

def lastname():
    return lastwordsblock[random.randint(0,len(lastwordsblock)-1)]


def name():
    return firstname() + " " + lastname()

class block(object):
        def __init__(self, e, x, y):
            self.e = e
            self.name = name()
            self.owner = 0
            self.business = business.business()
            self.coordinates = str(x) + "," + str(y)

        def getOwner(self):
            return self.owner

        def setOwner(self,owner):
            self.owner = owner

        def getBusiness(self):
            return self.business

        def getCoordinates(self):
            return self.coordinates
