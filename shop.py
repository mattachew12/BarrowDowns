'''
Created on Sep 17, 2012

@author: Matthew
'''
'''
Created on Nov 15,2011

@author: Matthew
'''
#!/usr/bin/env python
# attribute order: armor,attack,block,value,rarity,type
# lists and dicts are not hashable, so they can't be used as keys. hashable stuff is immutable. str,tup,int,...
barehands = [0,1,0,0,0,1]
Ontorch = [0,10,0,0,4,1]
Offtorch = [0,2,0,0,0,1]

GoldStraightSword = [0,3,4,60,5,1] 
IronStraightSword = [0,3,4,60,5,2]
SteelStraightSword = [0,3,4,60,5,3]
KinglyStraightSword = [0,3,4,60,5,4]
ElvenStraightSword = [0,3,4,60,5,5]
MithrilStraightSword = [0,3,4,60,5,6]
AuleanStraightSword = [0,3,4,60,5,8]
SS = [GoldStraightSword,IronStraightSword,SteelStraightSword,KinglyStraightSword,\
ElvenStraightSword,MithrilStraightSword,AuleanStraightSword]
SSdict = {"[0, 3, 4, 60, 5, 1]":"Gold Straight Sword","[0, 3, 4, 60, 5, 2]":"Iron Straight Sword",\
"[0, 3, 4, 60, 5, 3]":"Steel Straight Sword","[0, 3, 4, 60, 5, 4]":"Kingly Straight Sword",\
"[0, 3, 4, 60, 5, 5]":"Elven Straight Sword","[0, 3, 4, 60, 5, 6]":"Mithril Straight Sword",\
"[0, 3, 4, 60, 5, 8]":"Aulean Straight Sword"}

GoldCurvedSword = [0,2,2,30,6,1]
IronCurvedSword = [0,2,2,30,6,2]
SteelCurvedSword = [0,2,2,30,6,3]
KinglyCurvedSword = [0,2,2,30,6,4]
ElvenCurvedSword = [0,2,2,30,6,5]
MithrilCurvedSword = [0,2,2,30,6,6]
AuleanCurvedSword = [0,2,2,30,6,8]
CS = [GoldCurvedSword,IronCurvedSword,SteelCurvedSword,KinglyCurvedSword,\
ElvenCurvedSword,MithrilCurvedSword,AuleanCurvedSword]
CSdict = {"[0, 2, 2, 30, 6, 1]":"Gold Curved Sword","[0, 2, 2, 30, 6, 2]":"Iron Curved Sword",\
"[0, 2, 2, 30, 6, 3]":"Steel Curved Sword","[0, 2, 2, 30, 6, 4]":"Kingly Curved Sword",\
"[0, 2, 2, 30, 6, 5]":"Elven Curved Sword","[0, 2, 2, 30, 6, 6]":"Mithril Curved Sword",\
"[0, 2, 2, 30, 6, 8]":"Aulean Curved Sword"}

GoldAxe = [0,5,0,30,6,1]
IronAxe = [0,5,0,30,6,2]
SteelAxe = [0,5,0,30,6,3]
KinglyAxe = [0,5,0,30,6,4]
ElvenAxe = [0,5,0,30,6,5]
MithrilAxe = [0,5,0,30,6,6]
AuleanAxe = [0,5,0,30,6,8]
Axe = [GoldAxe,IronAxe,SteelAxe,KinglyAxe,ElvenAxe,MithrilAxe,AuleanAxe]
Axedict = {"[0, 5, 0, 30, 6, 1]":"Gold Axe","[0, 5, 0, 30, 6, 2]":"Iron Axe","[0, 5, 0, 30, 6, 3]":"Steel Axe",\
"[0, 5, 0, 30, 6, 4]":"Kingly Axe","[0, 5, 0, 30, 6, 5]":"Elven Axe","[0, 5, 0, 30, 6, 6]":"Mithril Axe",\
"[0, 5, 0, 30, 6, 8]":"Aulean Axe"}

GoldClub = [0,1,0,5,10,1,1]
IronClub = [0,1,0,5,10,2,1]
SteelClub = [0,1,0,5,10,3,1]
KinglyClub = [0,1,0,5,10,4,1]
ElvenClub = [0,1,0,5,10,5,1]
MithrilClub = [0,1,0,5,10,6,1]
AuleanClub = [0,1,0,5,10,8,1]
Club = [GoldClub,IronClub,SteelClub,KinglyClub,ElvenClub,MithrilClub,AuleanClub]
Clubdict = {"[0, 1, 0, 5, 10, 1, 1]":"Gold Club","[0, 1, 0, 5, 10, 2, 1]":"Iron Club","[0, 1, 0, 5, 10, 3, 1]":"Steel Club",\
"[0, 1, 0, 5, 10, 4, 1]":"Kingly Club","[0, 1, 0, 5, 10, 5, 1]":"Elven Club","[0, 1, 0, 5, 10, 6, 1]":"Mithril Club",\
"[0, 1, 0, 5, 10, 8, 1]":"Aulean Club"}

GoldKnife = [0,2,0,10,6,1,1]
IronKnife = [0,2,0,10,6,2,1]
SteelKnife = [0,2,0,10,6,3,1]
KinglyKnife = [0,2,0,10,6,4,1]
ElvenKnife = [0,2,0,10,6,5,1]
MithrilKnife = [0,2,0,10,6,6,1]
AuleanKnife = [0,2,0,10,6,8,1]
Knife = [GoldKnife,IronKnife,SteelKnife,KinglyKnife,ElvenKnife,MithrilKnife,AuleanKnife]
Knifedict = {"[0, 2, 0, 10, 6, 1, 1]":"Gold Knife","[0, 2, 0, 10, 6, 2, 1]":"Iron Knife",\
"[0, 2, 0, 10, 6, 3, 1]":"Steel Knife","[0, 2, 0, 10, 6, 4, 1]":"Kingly Knife",\
"[0, 2, 0, 10, 6, 5, 1]":"Elven Knife","[0, 2, 0, 10, 6, 6, 1]":"Mithril Knife",\
"[0, 2, 0, 10, 6, 8, 1]":"Aulean Knife"}

GoldThrowingAxe = [0,3,0,10,6,1,1]
IronThrowingAxe = [0,3,0,10,6,2,1]
SteelThrowingAxe = [0,3,0,10,6,3,1]
KinglyThrowingAxe = [0,3,0,10,6,4,1]
ElvenThrowingAxe = [0,3,0,10,6,5,1]
MithrilThrowingAxe = [0,3,0,10,6,6,1]
AuleanThrowingAxe = [0,3,0,10,6,8,1]
ThrowingAxe = [GoldThrowingAxe,IronThrowingAxe,SteelThrowingAxe,KinglyThrowingAxe,ElvenThrowingAxe,MithrilThrowingAxe,AuleanThrowingAxe]
ThrowingAxedict = {"[0, 3, 0, 10, 6, 1, 1]":"Gold Throwing Axe","[0, 3, 0, 10, 6, 2, 1]":"Iron Throwing Axe",\
"[0, 3, 0, 10, 6, 3, 1]":"Steel Throwing Axe","[0, 3, 0, 10, 6, 4, 1]":"Kingly Throwing Axe",\
"[0, 3, 0, 10, 6, 5, 1]":"Elven Throwing Axe","[0, 3, 0, 10, 6, 6, 1]":"Mithril Throwing Axe",\
"[0, 3, 0, 10, 6, 8, 1]":"Aulean Throwing Axe"}

GoldTwoHandedSword = [0,5,2,100,1,1]
IronTwoHandedSword = [0,5,2,100,1,2]
SteelTwoHandedSword = [0,5,2,100,1,3]
KinglyTwoHandedSword = [0,5,2,100,1,4]
ElvenTwoHandedSword = [0,5,2,100,1,5]
MithrilTwoHandedSword = [0,5,2,100,1,6]
AuleanTwoHandedSword = [0,5,2,100,1,8]
THS = [GoldTwoHandedSword,IronTwoHandedSword,SteelTwoHandedSword,KinglyTwoHandedSword,\
ElvenTwoHandedSword,MithrilTwoHandedSword,AuleanTwoHandedSword]
THSdict = {"[0, 5, 2, 100, 1, 1]":"Gold Two Handed Sword","[0, 5, 2, 100, 1, 2]":"Iron Two Handed Sword",\
"[0, 5, 2, 100, 1, 3]":"Steel Two Handed Sword","[0, 5, 2, 100, 1, 4]":"Kingly Two Handed Sword",\
"[0, 5, 2, 100, 1, 5]":"Elven Two Handed Sword","[0, 5, 2, 100, 1, 6]":"Mithril Two Handed Sword",\
"[0, 5, 2, 100, 1, 8]":"Aulean Two Handed Sword"}

GoldTwoHandedAxe = [0,7,1,100,1,1]
IronTwoHandedAxe = [0,7,1,100,1,2]
SteelTwoHandedAxe = [0,7,1,100,1,3]
KinglyTwoHandedAxe = [0,7,1,100,1,4]
ElvenTwoHandedAxe = [0,7,1,100,1,5]
MithrilTwoHandedAxe = [0,7,1,100,1,6]
AuleanTwoHandedAxe = [0,7,1,100,1,8]
THA = [GoldTwoHandedAxe,IronTwoHandedAxe,SteelTwoHandedAxe,KinglyTwoHandedAxe,ElvenTwoHandedAxe,\
MithrilTwoHandedAxe,AuleanTwoHandedAxe]
THAdict = {"[0, 7, 1, 100, 1, 1]":"Gold Two Handed Axe","[0, 7, 1, 100, 1, 2]":"Iron Two Handed Axe",\
"[0, 7, 1, 100, 1, 3]":"Steel Two Handed Axe","[0, 7, 1, 100, 1, 4]":"Kingly Two Handed Axe",\
"[0, 7, 1, 100, 1, 5]":"Elven Two Handed Axe","[0, 7, 1, 100, 1, 6]":"Mithril Two Handed Axe",\
"[0, 7, 1, 100, 1, 8]":"Aulean Two Handed Axe"}

GoldBow = [0,1,0,40,6,1]
IronBow = [0,1,0,40,6,2]
SteelBow = [0,1,0,40,6,3]
KinglyBow = [0,1,0,40,6,4]
ElvenBow = [0,1,0,40,6,5]
MithrilBow = [0,1,0,40,6,6]
AuleanBow = [0,1,0,40,6,8]
Bow = [GoldBow,IronBow,SteelBow,KinglyBow,ElvenBow,MithrilBow,AuleanBow]
Bowdict = {"[0, 1, 0, 40, 6, 1]":"Gold Bow","[0, 1, 0, 40, 6, 2]":"Iron Bow","[0, 1, 0, 40, 6, 3]":"Steel Bow",\
"[0, 1, 0, 40, 6, 4]":"Kingly Bow","[0, 1, 0, 40, 6, 5]":"Elven Bow","[0, 1, 0, 40, 6, 6]":"Mithril Bow",\
"[0, 1, 0, 40, 6, 8]":"Aulean Bow"}

GoldArrow = [0,3,0,10,3,1]
IronArrow = [0,3,0,10,3,2]
SteelArrow = [0,3,0,10,3,3]
KinglyArrow = [0,3,0,10,3,4]
ElvenArrow = [0,3,0,10,3,5]
MithrilArrow = [0,3,0,10,3,6]
AuleanArrow = [0,3,0,10,3,8]
Arrow = [GoldArrow,IronArrow,SteelArrow,KinglyArrow,ElvenArrow,\
MithrilArrow,AuleanArrow]
Arrowdict = {"[0, 3, 0, 10, 3, 1]":"Gold Arrow","[0, 3, 0, 10, 3, 2]":"Iron Arrow", "[0, 3, 0, 10, 3, 3]":"Steel Arrow", \
"[0, 3, 0, 10, 3, 4]":"Kingly Arrow", "[0, 3, 0, 10, 3, 5]":"Elven Arrow","[0, 3, 0, 10, 3, 6]":"Mithril Arrow",
"[0, 3, 0, 10, 3, 8]":"Aulean Arrow"}

weapons = [SS,CS,Axe,Club,Knife,ThrowingAxe,THS,THA,Bow,Arrow] 

GoldRoundShield = [3,0,5,30,6,1,1]
IronRoundShield = [3,0,5,30,6,2,1]
SteelRoundShield = [3,0,5,30,6,3,1]
KinglyRoundShield = [3,0,5,30,6,4,1]
ElvenRoundShield = [3,0,5,30,6,5,1]
MithrilRoundShield = [3,0,5,30,6,6,1]
AuleanRoundShield = [3,0,5,30,6,8,1]
RoundS = [GoldRoundShield,IronRoundShield,SteelRoundShield,KinglyRoundShield,ElvenRoundShield,\
MithrilRoundShield,AuleanRoundShield]
RoundSdict = {"[3, 0, 5, 30, 6, 1, 1]":"Gold Round Shield","[3, 0, 5, 30, 6, 2, 1]":"Iron Round Shield",\
"[3, 0, 5, 30, 6, 3, 1]":"Steel Round Shield","[3, 0, 5, 30, 6, 4, 1]":"Kingly Round Shield",\
"[3, 0, 5, 30, 6, 5, 1]":"Elven Round Shield","[3, 0, 5, 30, 6, 6, 1]":"Mithril Round Shield",\
"[3, 0, 5, 30, 6, 8, 1]":"Aulean Round Shield"}

GoldSquareShield = [2,0,4,15,8,1]
IronSquareShield = [2,0,4,15,8,2]
SteelSquareShield = [2,0,4,15,8,3]
KinglySquareShield = [2,0,4,15,8,4]
ElvenSquareShield = [2,0,4,15,8,5]
MithrilSquareShield = [2,0,4,15,8,6]
AuleanSquareShield = [2,0,4,15,8,8]
SquareS = [GoldSquareShield,IronSquareShield,SteelSquareShield,KinglySquareShield,ElvenSquareShield,\
MithrilSquareShield,AuleanSquareShield]
SquareSdict = {"[2, 0, 4, 15, 8, 1]":"Gold Square Shield","[2, 0, 4, 15, 8, 2]":"Iron Square Shield",\
"[2, 0, 4, 15, 8, 3]":"Steel Square Shield","[2, 0, 4, 15, 8, 4]":"Kingly Square Shield",\
"[2, 0, 4, 15, 8, 5]":"Elven Square Shield","[2, 0, 4, 15, 8, 6]":"Mithril Square Shield",\
"[2, 0, 4, 15, 8, 8]":"Aulean Square Shield"}

GoldNumenoreanShield = [10,0,7,100,1,1]
IronNumenoreanShield = [10,0,7,100,1,2]
SteelNumenoreanShield = [10,0,7,100,1,3]
KinglyNumenoreanShield = [10,0,8,100,1,4]
ElvenNumenoreanShield = [10,0,8,100,1,5]
MithrilNumenoreanShield = [10,0,9,100,1,6]
AuleanNumenoreanShield = [10,0,10,100,1,8]
NS = [GoldNumenoreanShield,IronNumenoreanShield,SteelNumenoreanShield,KinglyNumenoreanShield,ElvenNumenoreanShield,\
MithrilNumenoreanShield,AuleanNumenoreanShield]
NSdict = {"[10, 0, 7, 100, 1, 1]":"Gold Numenorean Shield","[10, 0, 7, 100, 1, 2]":"Iron Numenorean Shield",\
"[10, 0, 7, 100, 1, 3]":"Steel Numenorean Shield","[10, 0, 8, 100, 1, 4]":"Kingly Numenorean Shield",\
"[10, 0, 8, 100, 1, 5]":"Elven Numenorean Shield","[10, 0, 9, 100, 1, 6]":"Mithril Numenorean Shield",\
"[10, 0, 10, 100, 1, 8]":"Aulean Numenorean Shield"}

shields = [SquareS,RoundS,NS]
tools = [weapons,shields]
toolsdictlist = [SSdict,CSdict,Axedict,Clubdict,Knifedict,ThrowingAxedict,THSdict,THAdict,SquareSdict,RoundSdict,Bowdict,NSdict,Arrowdict, \
{"[0, 1, 0, 0, 0, 1]": "Bare Hands"}, {"[0, 2, 0, 0, 0, 1]": "Unlit Torch"}, {"[0, 10, 0, 0, 4, 1]": "Lit Torch"}]
def alltools(): # function instead of var because I would have to assign it first,which would be the one imported
    alltools = []
    for classes in tools: # goes to wep and shield
        for types in classes: # goes to subclasses
            for eachtool in types: # goes to each tool in subclasses
                alltools.append(eachtool) # alltools now has each one.
    return alltools
def toolsdict():
    toolsdict = {}
    for eachdict in toolsdictlist:
        toolsdict.update(eachdict)
    return toolsdict
toolsdict()
# attribute order: armor,attack,block,health,experience,found at and below,found at and above where,type
YoungBarrowWight = [0,2,1,5,10,1,15,1]
crazedHobbit = [30,20,2,100,20,10,25,2]
AdultBarrowWight = [50,40,2,150,100,20,35,3]
CrazedDwarf = [100,35,5,250,500,30,50,4]
OldBarrowWight = [100,70,3,500,2500,40,50,5]
KingBarrowWight= [600,100,4,1000,5000,50,50,7]
enemies = [YoungBarrowWight,crazedHobbit,AdultBarrowWight,CrazedDwarf,OldBarrowWight,KingBarrowWight]
EnemyDict = {"Y":YoungBarrowWight,"H":crazedHobbit,"A":AdultBarrowWight,"D":CrazedDwarf,\
"O": OldBarrowWight,"K":KingBarrowWight}
EnemyDictNames = {"Y":"Young Barrow Wight","H": "Crazed Hobbit","A":"Adult Barrow Wight",\
"D": "Crazed Dwarf","O": "Old Barrow Wight","K": "King Barrow Wight", "\\": "Leg of Ungoliant", \
"|": "Leg of Ungoliant", "/": "Leg of Ungoliant", "=": "Pincers of Ungoliant", "o": "Head of Ungoliant",\
"(": "Thorax of Ungoliant", ")":"Abdomen of Ungoliant", "}": "Stinger of Ungoliant"}
