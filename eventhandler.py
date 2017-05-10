import random
import gang

EVENTS_LENGTH = 10
NEWGANGFORMCHANCE = 80 ##the higher this is, the less often new gangs form
NEWMEMBERCHANCE = 12 ##the higher this is, the more appeal a gang needs to attract a new member
CHOWNBLOCKNOTORIETY = 10 ##the amount of notoriety gained from taking over a block
NEWMEMBERCOST = 10 ##Amount of appeal spent to gain a new member
NEWHEROCHANCE = 12 ##the higher this is, the more appeal the heroes need to attract a new hero
NEWHEROCOST = 10 ##Amount of appeal spent to gain a new hero

class eventhandler(object):
        def __init__(self):
            self.gangs = []
            ##generate symbols
            self.symbols = []
            i = 0
            mystr = "1234567890!@$%^&*()qwertyuiopasdfghjklzxcvbnm<>?/"
            while i < len(mystr):
                self.symbols.append(mystr[i])
                i += 1
            self.eventsqueue = []
            self.heroesactive = 0

        def step(self):
            i = 0
            while i < len(self.eventsqueue):
                print self.eventsqueue[i]
                i += 1
            if len(self.eventsqueue) > EVENTS_LENGTH:
                i = 0
                diff = len(self.eventsqueue) - EVENTS_LENGTH
                tmparray = []
                while i < EVENTS_LENGTH:
                    tmparray.append(self.eventsqueue[i + diff])
                    i += 1
                self.eventsqueue = tmparray

        def setHeroes(self,heroes):
            self.heroesactive = 1
            self.heroes = heroes

        def setForce(self,force):
            self.forceactive = 1
            self.force = force

        def setBlocks(self,blocks):
            self.blocks = blocks
            ##give each gang 1 block to start
            for gang in self.gangs:
                testblock = self.blocks[random.randint(0,len(self.blocks)-1)][random.randint(0,len(self.blocks[0])-1)]
                while type(testblock.getOwner()) != type(0):
                    testblock = self.blocks[random.randint(0,len(self.blocks)-1)][random.randint(0,len(self.blocks[0])-1)]
                testblock.setOwner(gang)
                gang.changeBlockNum(1)


        def append(self, event):
            self.eventsqueue.append(event)

        def stepGangs(self):
            for gang in self.gangs:
                for j in gang.getMembers():
                    if j.step() == 1:
                        ##60% chance to attempt to take a block; 40% chance to attempt to assassinate an opponent
                        if random.random() < 0.4:
                            targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                            while targetgang.getName() == gang.getName():
                                targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                            j.kill(targetgang)
                        else:
                            targetOwner = gang.takeBlock(self.blocks,j)
                            if type(targetOwner) != type(0):
                                targetOwner.changeBlockNum(-1)
                                if targetOwner.getBlockNum() == 0:
                                    self.destroyGang(targetOwner)
                                    j.setNotoriety(j.getNotoriety() + CHOWNBLOCKNOTORIETY)
                            gang.changeBlockNum(1)
                if gang.getAppeal() > random.randint(0,NEWMEMBERCHANCE):
                    gang.newMember()
                    self.append(gang.getMembers()[len(gang.getMembers())-1].getName() + " has joined " + gang.getName() + "!")
                    gang.setAppeal(gang.getAppeal()-NEWMEMBERCOST)

            for blockrow in self.blocks:
                for block in blockrow:
                    owner = block.getOwner()
                    if type(owner) != type(0):
                        block.getOwner().addMoney(block.getBusiness().getIncome())

            if random.randint(0,NEWGANGFORMCHANCE) == 0:
                self.newGang()
                self.append(self.gangs[len(self.gangs)-1].getName() + " has formed!")

        def newGang(self):
            randnum = random.randint(0,len(self.symbols)-1)
            self.gangs.append(gang.gang(self,self.symbols.pop(randnum)))

        def stepHeroes(self):
            if self.heroes.getActive() == 1:
                for j in self.heroes.getMembers():
                    if j.step() == 1:
                        targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                        j.kill(targetgang)
                        if len(targetgang.getMembers()) == 0:
                            self.destroyGang(targetgang)
                        if len(self.heroes.getMembers()) == 0:
                            ##random chance that the league will be reformed
                            if random.randint(0,1) == 1:
                                self.heroes.regenName()
                                self.append(self.heroes.getName() + " has reborn!")
                                i = 0
                                while i < 3:
                                    self.heroes.newMember()
                                    i += 1
                            else:
                                self.append(self.heroes.getName() + " has been disbanded!")
                                self.heroesactive = 0
                                self.heroes.setActive(0)
                if self.heroes.getAppeal() > random.randint(0,NEWHEROCHANCE):
                    self.heroes.newMember()
                    self.append(self.heroes.getMembers()[len(heroes.getMembers())-1].getName() + " has joined " + self.heroes.getName() + "!")
                    self.heroes.setAppeal(self.heroes.getAppeal()-NEWHEROCOST)

        def stepForce(self):
            if self.force.getActive() == 1:
                for j in self.force.getMembers():
                    if j.step() == 1:
                        targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                        j.kill(targetgang)
                        if len(targetgang.getMembers()) == 0:
                            self.destroyGang(targetgang)
                        if len(self.force.getMembers()) == 0:
                            self.append(self.force.getName() + " has been reorganized by the mayor!")
                            i = 0
                            while i < 3:
                                self.force.newMember()
                                i += 1
                if self.force.getAppeal() > random.randint(0,8):
                    self.force.newMember()
                    self.append(self.force.getMembers()[len(force.getMembers())-1].getName() + " has joined " + self.force.getName() + "!")
                    self.force.setAppeal(self.force.getAppeal()-15)


        def destroyGang(self,gang):
            self.append(gang.getName() + " has been disbanded!")
            self.gangs.remove(gang)
            self.wipeBlocks(gang)
            if len(self.gangs) == 1:
                print self.gangs[0].getName() + " has taken over the city!"
                self.printBlocks()
                exit()

        def printLeagues(self):
            if self.heroesactive == 1:
                print self.heroes.getName() + ", led by " + self.heroes.getLeader().getName()
                print "Members:"
                for j in self.heroes.getMembers():
                    print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
                print ""

        def printForce(self):
            if self.forceactive == 1:
                print self.force.getName() + ", led by " + self.force.getLeader().getName()
                print "Members:"
                for j in self.force.getMembers():
                    print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
                print ""

        def printGangs(self):
                for gang in self.gangs:
                    print gang.getSymbol() + " " + gang.getName() + ", Led by " + gang.getLeader().getName() + "; $" + str(gang.getMoney())
                    print "Members: "
                    for j in gang.getMembers():
                        print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
                    print ""

        def wipeBlocks(self,gang):
            i = 0
            while i < len(self.blocks):
                j = 0
                while j < len(self.blocks[i]):
                    if self.blocks[i][j].getOwner() == gang:
                        self.blocks[i][j].setOwner(0)
                    j += 1
                i += 1

        def printBlocks(self):
            ## print block map
            i = 0
            while i < len(self.blocks):
                j = 0
                line = ""
                while j < len(self.blocks[i]):
                    if self.blocks[i][j].getOwner() == 0:
                        line = line + '#'
                    else:
                        line = line + self.blocks[i][j].getOwner().getSymbol()
                    j += 1
                print line
                i += 1

