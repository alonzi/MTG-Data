# @alonzi
# main program for calculating entropy of draft table
# 2022-07-28
# classes for draft entropy calculator

from math import comb,log

NU = 80
NUpp = 3
NC = 101
NCpp = 10

class pool():
    def __init__(self):
        self.seen = False
        self.E = 0 # pass entropy into pool

    def getSeen(self):
        return self.seen
    
    def setSeen(self):
        self.seen = True
        return True

    def getEntropy(self):
        return self.E    
    
    def addEntropy(self,e):
        self.E = self.E + e
        return self.E


class pack():

    def __init__(self):
        self.nu=NUpp
        self.nc=NCpp
        self.seen = False

    def cards(self):
        return self.nu+self.nc
    
    def getEntropy(self):
        if self.seen: 
            E = log( self.nu+self.nc ,2 )
        else:
            E = log( comb(NU,self.nu) * comb(NC,self.nc),2 ) # BEFORE PACKS ARE OPENED
        return E

    def getSeen(self):
        return self.seen
    
    def setSeen(self):
        self.seen = True
        return True

    def makePick(self):

        entropyDecrease = self.getEntropy()

        if self.nu>0:
            self.nu -=1
        else:
            self.nc -=1

        entropyDecrease = entropyDecrease - self.getEntropy()

        return entropyDecrease



class tbl():

    def __init__(self):
        self.packs = []
        self.pools = []
        for i in range(8):
            self.packs.append(pack())
            self.pools.append(pool())
        # place in packs is location at draft table [0] is the you
        
        # create pools
        
    def getEntropy(self):
        E=0
        packE = []
        poolE = []

        for pack in self.packs:
            packE.append(round(pack.getEntropy(),1))
        for pool in self.pools:
            poolE.append(round(pool.getEntropy(),1))

        # look at 0 pack and pool
        packE[0]=0
        poolE[0]=0


        print("-- I am",self,"this is my entropy",sum(packE)+sum(poolE))
        print("---- Pack Entropy", packE)
        print("---- Pool Entropy", poolE)

    def makePick(self):
        for pack in enumerate(self.packs):
            self.pools[pack[0]].addEntropy( pack[1].makePick() )

    def makePass(self):
        self.packs[0].setSeen()
        self.packs.append(self.packs.pop(0))


