# @alonzi
# main program for calculating entropy of draft table
# 2022-07-28
# classes for draft entropy calculator

from math import comb,log

NU = 80
NUpp = 3
NC = 101
NCpp = 10

class pack():

    def __init__(self):
        self.nu=NUpp
        self.nc=NCpp
        self.seen = False

    def getEntropy(self):
        if self.seen: 
            E = log( self.nu+self.nc ,2 )
        else:
            E = log( comb(NU,self.nu) * comb(NC,self.nc),2 )
        return E

    def getSeen(self):
        return self.seen
    
    def setSeen(self):
        self.seen = True
        return True




class tbl():

    def __init__(self):
        self.packs = []
        for i in range(8): self.packs.append(pack())
        # place in packs is location at draft table [0] is the you
        # create pools
        
    def getEntropy(self):
        E=0
        for pack in self.packs: E+=pack.getEntropy()
        print("\nI am",self,"this is my entropy",E)

