#!\usr\bin\env python
# investigate equip/unequip/drop and pyGame
import random
import time
import sys
import os
import shop
import copy
######################
#    Variables
######################
toolsdict = shop.toolsdict()
options = ["y", "n"]
commands = ["a","s","d","w","h","i","D","e","u","S","U","/exit","/save","/load"]
wasdStringDict = {9:"(origPos - findobj) % 81 < 72",-9:"(origPos - findobj) % 81 > 8",1:"(origPos - findobj) % 9 != 8",\
-1:"(origPos - findobj) % 9 != 0"} # for using in movement and throwing
bottommsg = ""
area = []
terrain = []
level = 0
CharLevel = 1
Experience = 0
health = 10
turn = 1
viewterrain = []
terrainnumbers = []
dropdictionary = {}
EnemyPlaceDict = {}
UserName = raw_input("What is your name? ").strip().title()
inventory = []
equipped = [shop.barehands,shop.barehands]
level = 0
row = 0
useok = False
bodyparts = ["\\", "|", "|", "/", "=", "o", "(", ")", "}", "/", "|", "|", "\\"] # Ungoliant body
##############################
#
#
#      Save Functions
#
##############################
def bottomprint(string):
    global bottommsg
    bottommsg += "\n" + string
def savegame():
    global health, level, CharLevel, Experience
    statlist = [health,level,CharLevel,Experience]
    savefile = open("BarrowDownsSaveFile.txt", "a") # this creates the file if it doesn't exist.
    savefile.close
    savefile = open("BarrowDownsSaveFile.txt", "r")
    FindInSaveFile = savefile.read()
    savefile.close 
    savefile = open("BarrowDownsSaveFile.txt", "w") # w immediately deletes the whole thing.
    if len(inventory) == 0:
        inventory.append(shop.barehands)
    if UserName+"\n" in FindInSaveFile:
        while True:
            choice = raw_input("Are you sure you want to overwrite your previous save?").lower().strip()[:1]
            if choice == "y":
                StartSaveIndex = FindInSaveFile.find(UserName+"\n")
                IntermediateSaveIndex =FindInSaveFile.find("}", StartSaveIndex)
                IntermediateSaveIndex2 =FindInSaveFile.find("}", IntermediateSaveIndex+1)
                EndSaveIndex =FindInSaveFile.find("]", IntermediateSaveIndex2)
                FindInSaveFile = FindInSaveFile[:StartSaveIndex] + FindInSaveFile[EndSaveIndex+1:] # this cuts out the old save. [:] is the only way. del doesn't work.
                savefile.writelines([FindInSaveFile,"\n", UserName,"\n", str(terrain),"\n", str(terrainnumbers),"\n", str(inventory),\
"\n", str(equipped),"\n", str(EnemyPlaceDict), "\n", str(dropdictionary),"\n", str(statlist)])
                savefile.close()
                bottomprint("saved")
                break
            elif choice == "n":
                savefile.writelines([FindInSaveFile])
                bottomprint("not saved")
                break
            else:
                print "The options are (yes) and (n)o."
    else:
        savefile.writelines([FindInSaveFile,"\n", "WARNING!!! Editing this file will break the game.","\n", UserName,"\n", str(terrain),\
"\n", str(terrainnumbers),"\n", str(inventory),"\n", str(equipped),"\n", str(EnemyPlaceDict), "\n", str(dropdictionary),"\n", str(statlist)])
        savefile.close()
        bottomprint("saved")
def exitgame():
    while True:
        SaveOrNot = raw_input("Would you like to save your program? If so, you can open it again using the same character name. ").strip().lower() [:1]
        if SaveOrNot == "y":
            savegame()
            sys.exit()
        elif SaveOrNot =="n":
            sys.exit()
        else:
            print "The options are (yes) and (n)o."
def opensavedfile(character):
    global terrain, terrainnumbers, inventory, EnemyPlaceDict, dropdictionary, equipped, health, Experience, CharLevel, level
    try:
        savedfile = open("BarrowDownsSaveFile.txt", "r")
        savedfileinfo = savedfile.read()
    except:
        savedfileinfo = ""
    if character+"\n" not in savedfileinfo: #The +"\n" is to make sure it doesn't find Matt in Matthew
        landscaper() # if not savedd, makes the level
    if character+"\n" in savedfileinfo: # if saved, finds the explored area, terrain, and character stats and inventory.
        StartOfTerrainListIndex = savedfileinfo.find("[", savedfileinfo.find(character+"\n")) # it finds the username and then finds the index of the immediate next list.
        EndOfTerrainListIndex = savedfileinfo.find("]", StartOfTerrainListIndex)
        terrain = eval(savedfileinfo[StartOfTerrainListIndex:EndOfTerrainListIndex+1]) # +1 because it will cut off before the number, and the eval finds the list within the string, instead of giving a list of each character of the string.
        
        StartOfTerrainnumbersListIndex = savedfileinfo.find("[", EndOfTerrainListIndex) 
        EndOfTerrainnumbersListIndex = savedfileinfo.find("]", StartOfTerrainnumbersListIndex)
        terrainnumbers = eval(savedfileinfo[StartOfTerrainnumbersListIndex:EndOfTerrainnumbersListIndex+1])
        
        StartOfInventoryListIndex = savedfileinfo.find("[", EndOfTerrainnumbersListIndex) 
        EndOfInventoryListIndex = savedfileinfo.find("]]", StartOfInventoryListIndex)
        inventory = eval(savedfileinfo[StartOfInventoryListIndex:EndOfInventoryListIndex+2]) # +2 because it has to get by 2 ]s
        
        StartOfEquipListIndex = savedfileinfo.find("[", EndOfInventoryListIndex) 
        EndOfEquipListIndex = savedfileinfo.find("]]", StartOfEquipListIndex)
        equipped = eval(savedfileinfo[StartOfEquipListIndex:EndOfEquipListIndex+2])
        
        StartOfEnemyPlaceDictIndex = savedfileinfo.find("{", EndOfEquipListIndex) 
        EndOfEnemyPlaceDictIndex = savedfileinfo.find("}", StartOfEnemyPlaceDictIndex)
        EnemyPlaceDict = eval(savedfileinfo[StartOfEnemyPlaceDictIndex:EndOfEnemyPlaceDictIndex+1])
        
        StartOfDropDictIndex = savedfileinfo.find("{", EndOfEnemyPlaceDictIndex) 
        EndOfDropDictIndex = savedfileinfo.find("}", StartOfDropDictIndex)
        dropdictionary = eval(savedfileinfo[StartOfDropDictIndex:EndOfDropDictIndex+1])
        
        StartOfStatListIndex = savedfileinfo.find("[", EndOfDropDictIndex) 
        EndOfStatListIndex = savedfileinfo.find("]", StartOfStatListIndex)
        statlist = eval(savedfileinfo[StartOfStatListIndex:EndOfStatListIndex+1])
        health = statlist[0];level = statlist[1];CharLevel = statlist[2];Experience = statlist[3]
def load():
    while True:
        sureness = raw_input("Are you sure you want to exit your current game: ").lower().strip()[:1]
        if sureness in options:
            break
        else:
            print "The options are (yes) and (n)o."
    if sureness == "y":
        while True:
            save = raw_input("Would you like to save your current game: ").lower().strip()[:1]
            if save in options:
                break
            else:
                print "The options are (yes) and (n)o."
        if save == "y": # no n is needed because y and n are the only options.
            savegame()
        savedfile = open("BarrowDownsSaveFile.txt", "r")
        savedfileinfo = savedfile.read()
        if savedfileinfo.strip() == "":
            bottomprint("there are no saved characters.") 
        else:
            while True:  
                whoload = raw_input("What character do you want to load: ").lower().strip().capitalize()
                if whoload + "\n" not in savedfileinfo:
                    print "That's not a saved character. Try again."
                else:
                    break
            clearscreen()
            opensavedfile(whoload)    
##############################
#
#
#     Regular Functions
#
##############################
def printInventory():
    global inventory
    while True:
        try:
            del inventory[inventory.index(shop.barehands)] # deletes any Bare Hands in inventory
        except:
            break
    loop = 1
    clearscreen()
    print "Inventory:"
    for each in inventory:
        armorInvenWeapon = each[0]*each[5]
        attackInvenWeapon = each[1]*each[5]
        blockInvenWeapon = each[2]
        
        attackChangeRightHand = attackInvenWeapon - (equipped[0][1]*equipped[0][5])
        blockChangeRightHand = blockInvenWeapon - equipped[0][2]
        
        armorChangeLeftHand = armorInvenWeapon - (equipped[1][0]*equipped[1][5]) # no armor for right hand because shields are always left
        attackChangeLeftHand = attackInvenWeapon - (equipped[1][1]*equipped[1][5])
        blockChangeLeftHand = blockInvenWeapon - equipped[1][2]
        
        print loop, "  ", toolsdict[str(each)],"  Armor: %s (%s)  Attack: %s RH (%s) LH (%s)  Block: %s RH (%s) LH (%s)" % (armorInvenWeapon, \
armorChangeLeftHand, attackInvenWeapon, attackChangeRightHand, attackChangeLeftHand, blockInvenWeapon, blockChangeRightHand, \
blockChangeLeftHand)
        loop +=1
    loop = 1
    print "Equipped:"
    for eachequip in equipped:
        print loop, "  ", toolsdict[str(eachequip)],"  Armor: %d  Attack: %d  Block: %d" % (eachequip[0]*eachequip[5],eachequip[1]*eachequip[5],eachequip[2])
        loop += 1
def throwWeapon(origPos, num, choice):
    global CharLevel
    global Experience
    findobj = num
    while True:  
        if toolsdict[str(inventory[choice])].find("Arrow") != -1:        
            sureness = raw_input("Are you sure you want to shoot this? It will not be retrievable.").lower().strip()[:1]
        elif toolsdict[str(inventory[choice])].find("Arrow") == -1:        
            sureness = raw_input("Are you sure you want to throw this? It will not be retrievable.").lower().strip()[:1]
        if sureness in options:
            break
        else:
            print "The options are (yes) and (n)o."
    if sureness == "y":
        while True: # this loop is to let the knife traverse multiple squares.
            if terrain[origPos - findobj] == "-" or not eval(wasdStringDict[num]): # if impassable terrain
                bottomprint("The %s hits a wall and breaks." % (toolsdict[str(inventory[choice])]))
                break
            try:
                shop.EnemyDictNames.keys().index(terrain[origPos - findobj])
                good = True # this finds out if the terrain is an enemy or not
            except:
                good = False
            if good == True: # if enemy
                if toolsdict[str(inventory[choice])].find("Round Shield") != -1: # MARVELLL!!!
                    dmg = (inventory[choice][5]*inventory[choice][5]*2*CharLevel)-EnemyPlaceDict[origPos - findobj][0] 
                else:
                    dmg = (inventory[choice][1]*inventory[choice][5]*2*CharLevel)-EnemyPlaceDict[origPos - findobj][0] # damage doubled when knife is thrown and armor subtracted
                EHealth = (EnemyPlaceDict[origPos - findobj][3]) 
                EHealth -= dmg
                if EHealth <= 0: # if he is dead
                    bottomprint("You killed the %s" % shop.EnemyDictNames[terrain[origPos - findobj]])
                    enemydrop = drop(EnemyPlaceDict[origPos - findobj])
                    Experience += EnemyPlaceDict[origPos - findobj][4]
                    currentlevel = CharLevel
                    if CharLevel == 0:
                        CharLevel = 1 
                    if Experience >= 1.46**(CharLevel+1) + 60*(CharLevel): # if experience >= than requirement, level up.
                        CharLevel +=1
                    if currentlevel < CharLevel: #level up!
                        bottomprint("Congratulations, you've leveled up!")
                        health = 10*CharLevel # increase my health by level
                    dropdictionary[origPos - findobj] = enemydrop
                    terrain[origPos - findobj] = '!' # removes his char from map
                    del EnemyPlaceDict[origPos - findobj]
                    break
                else:
                    bottomprint("You hit the %s" % shop.EnemyDictNames[terrain[origPos - findobj]])
                    EnemyPlaceDict[origPos - findobj][3] = EHealth
                    break
            else: # not enemy and not impassable, thus continue
                findobj += num
    if sureness == "n": #deleted after, so reinserted here
        inventory.insert(choice, inventory[choice])
def throwtorch(origPos,num):
    findobj = num
    while True: # this loop is to let the torch traverse multiple squares.
        if terrain[origPos - findobj] == "-" or not eval(wasdStringDict[num]):
            bottomprint("The torch hits a wall.")
            dropdictionary[origPos-findobj+num] = shop.Offtorch
            if terrain[origPos - findobj+num] == ".":
                terrain[origPos - findobj+num] = "!"
            break
        try:
            shop.EnemyDictNames.keys().index(terrain[origPos - findobj])
            good = True # this finds out if the terrain is an enemy or not
        except:
            good = False
        if good == True:
            bottomprint("You torched the %s! His ash blows away." % shop.EnemyDictNames[terrain[origPos - findobj]])
            enemydrop = drop(EnemyPlaceDict[origPos - findobj])
            dropdictionary[origPos - findobj] = enemydrop
            terrain[origPos - findobj] = '!' 
            del EnemyPlaceDict[origPos - findobj]
            WhichSpacesToView(origPos - findobj)
            Retaliation()
            break
        else:
            WhichSpacesToView(origPos - findobj)
        findobj += num
def throwing(invenitem):
    item = toolsdict[str(inventory[invenitem])]
    levelprint(9,level)
    while True:
        compassPts = ["w","a","s","d"]
        if item.find("Arrow") == -1:
            direction = raw_input("What direction would you like to throw in? (w/a/s/d) ")
        elif item.find("Arrow") != -1:
            direction = raw_input("What direction would you like to shoot in? (w/a/s/d) ") #shoot instead of throw
        if direction not in compassPts:
            print "which direction was it?"
            continue
        wpnposition = terrain.index("I") # % 81 to put in on the level only.
        if direction == "w":
            num = 9
        if direction == "d":
            num = -1
        if direction == "s":
            num = -9
        if direction == "a":
            num = 1
        break
    if item.find("Torch") == -1:
        throwWeapon(wpnposition, num, invenitem)
        Retaliation()
    elif item.find("Torch") != -1:
        throwtorch(wpnposition, num)
        Retaliation()
def lighttorch(invenidx):
    if shop.Offtorch in inventory:
        for each in inventory:
            if each == shop.Offtorch:
                inventory[inventory.index(each)] = shop.Ontorch
    printInventory()
def inventoryfunc(command):
    global inventory
    if command == "D":
        while True:
            printInventory()
            choice = raw_input("Which inventory item would you like to drop? (#) ")
            if choice == "": # hitting enter exits
                break
            if choice == "#":
                print "Ha ha ha. I meant a number."
            try:
                choice = int(choice)-1
            except:
                print "That's not an option.\n"
                continue
            if choice in range(0,len(inventory)):
                if inventory[choice] == shop.barehands:
                    bottomprint("You can't drop your hands!")
                    break
                del inventory[choice]
                printInventory()
                raw_input("--Continue--")
                clearscreen()
                break
            else: 
                print "That number is not in your inventory."
    if command == "e":
        global health
        while True:
            printInventory()
            choice = raw_input("Which item would you like to equip? (#) ")
            if choice == "":
                break
            if choice == "#":
                print "Ha ha ha. I meant a number."
            try:
                choice = int(choice)-1
            except:
                print "That's not an option.\n"
                continue
            if choice in range(0,len(inventory)): # inventory[choice] is the list of attributes of tool 
                if CharLevel >= (inventory[choice][5]-1) * 5: 
                    if True: # this allows me to have an else statement wherever I want.
                        if toolsdict[str(inventory[choice])].find("Shield") != -1: # the tool is a shield
                            inventory.append(equipped[1])
                            equipped[1] = inventory[choice][:]
                            if toolsdict[str(equipped[0])].find("Two Handed") != -1 or toolsdict[str(equipped[0])].find("Bow") != -1:
                                equipped[0] = shop.barehands # this holds it open so shield isn't 0
                        elif toolsdict[str(inventory[choice])].find("Two Handed") != -1 or toolsdict[str(inventory[choice])].find("Bow") != -1:
                            if (toolsdict[str(equipped[1])].find("Two Handed") != -1 and toolsdict[str(equipped[0])].find("Two Handed") != -1) or \
                            (toolsdict[str(equipped[1])].find("Bow") != -1 and toolsdict[str(equipped[0])].find("Bow") != -1):
                                inventory.append(equipped[0])
                                equipped[0] = inventory[choice][:]
                                equipped[1] = inventory[choice][:]
                            else: # if equipping two handed weapons, prevents double weapons in inventory
                                inventory.append(equipped[0])
                                inventory.append(equipped[1])
                                equipped[0] = inventory[choice][:]
                                equipped[1] = inventory[choice][:]
                        elif toolsdict[str(inventory[choice])].find("Arrow") != -1:
                            bottomprint("Arrows cannot be equipped, only Bows. To fire, use the arrows")
                            break
                        else: # any other tools besides Shield or Two Handed weapon
                            while True:
                                handchoice = raw_input("Would you like to wield it right or left handed? (1|2) ").lower().strip()[:1]
                                if handchoice != "1" and handchoice != "2":
                                    print "That's not an option."
                                    continue
                                if handchoice == "2":
                                    inventory.append(equipped[1])
                                    equipped[1] = inventory[choice][:]
                                if handchoice == "1":
                                    inventory.append(equipped[0])
                                    equipped[0] = inventory[choice][:]                        
                                if toolsdict[str(equipped[1])].find("Two Handed") != -1 or toolsdict[str(equipped[1])].find("Bow") != -1:
                                    equipped[1] = shop.barehands
                                if toolsdict[str(equipped[0])].find("Two Handed") != -1 or toolsdict[str(equipped[0])].find("Bow") != -1:
                                    equipped[0] = shop.barehands
                                break
                    del inventory[choice]
                    printInventory()
                    raw_input("--Continue--")
                    clearscreen()
                    break            
                elif CharLevel < (inventory[choice][5]-1) * 5:
                    bottomprint("You need to be level %d to equip that." % ((inventory[choice][5]-1) * 5))
                    break          
            else: 
                print "That number is not in your inventory."
    if command == "u":
        while True:
            printInventory()
            choice = raw_input("Which item would you like to unequip? (#) ")
            if choice == "":
                break
            if choice == "#":
                print "Ha ha ha. I meant a number."
            try:
                choice = int(choice)-1
            except:
                print "That's not an option. Choose either 1 or 2.\n"
                continue
            if choice in range(0,len(equipped)):
                inventory.append(equipped[choice])
                equipped[choice] = shop.barehands
                for slot in range(0,len(equipped)):
                    if toolsdict[str(equipped[slot])].find("Two Handed") != -1 or toolsdict[str(equipped[slot])].find("Bow") != -1:
                        equipped[slot] = shop.barehands
                printInventory()
                raw_input("--Continue--")
                clearscreen()
                break
            else: 
                print "That number is not in your equipped inventory."
    if command == "U":
        while True:
            printInventory()
            invenitem = raw_input("Which inventory item would you like to use? (#) ")
            if invenitem == "":
                break
            if invenitem == "#":
                print "Ha ha ha. I meant a number."
            try:
                invenitem = int(invenitem)-1
            except:
                print "That's not an option.\n"
                continue
            if invenitem in range(0,len(inventory)):
                if toolsdict[str(inventory[invenitem])].find("Arrow") != -1:
                    if toolsdict[str(equipped[0])].find("Bow") != -1: 
                        throwing(invenitem)
                    else:
                        bottomprint("A bow must be equipped")
                        break
                elif toolsdict[str(inventory[invenitem])].find("Lit Torch") != -1:
                    while True:
                        uses = raw_input("Would you like to throw it or light another torch? (throw/light) ").strip().lower()[:1]
                        if uses == "t":
                            throwing(invenitem)
                            del inventory[invenitem]
                            break
                        elif uses == "l":
                            lighttorch(invenitem)
                            raw_input("--Continue--")
                            break
                        else:
                            print "what was that?"
                    break
                elif toolsdict[str(inventory[invenitem])].find("Unlit Torch") != -1:
                    bottomprint("It needs to be lit first.")
                    break
                elif toolsdict[str(inventory[invenitem])].find("Aulean Numenorean Shield") != -1:
                    if useok == True:
                        while True:  
                            sureness = raw_input("Are you sure you want to battle Ungoliant now?").lower().strip()[:1]
                            if sureness in options:
                                break
                            else:
                                print "The options are (yes) and (n)o."
                        if sureness == "y":
                            inventory.append(equipped[1]) # next few lines copied from equip code, shield guaranteed
                            equipped[1] = inventory[invenitem][:]
                            if toolsdict[str(equipped[0])].find("Two Handed") != -1 or toolsdict[str(equipped[0])].find("Bow") != -1:
                                equipped[0] = shop.barehands # this holds it open so shield isn't 0
                            del inventory[invenitem]
                            savegame()
                            print "You smash the ground with your shield and a crack opens. You jump in."
                            time.sleep(2)
                            clearscreen()
                            animation()
                            bossmap()
                            break
                        else:
                            break
                    else:
                        inventory.append(inventory[invenitem])
                elif len(inventory[invenitem]) == 7: # throwable items have an extra characteristic
                    throwing(invenitem)
                elif len(inventory[invenitem]) != 7:
                    bottomprint("This item has no use beyond equipping")
                del inventory[invenitem]
                break                
            else: 
                print "That number is not in your inventory."
def raritycalc(tool):
    rarity = (tool[4])*(9-tool[5])# the 9 switches material rarity so the high rarity have 
    return rarity                 # a low number. this is so when appended, most rare are the least common.
def drop(enemy):
    alltools = shop.alltools()
    collection = []
    for eachtool in alltools:
        if eachtool[5] >= enemy[7] and eachtool[5]-1 <= enemy[7]: # this keeps the materials near to enemy levels
            rare = raritycalc(eachtool)
            for each in range(0,rare): 
                collection.append(eachtool)
    for each in range(4*(9-enemy[7])): # out here so that all enemies may drop it.
        collection.append(shop.Ontorch)
    drop = random.choice(collection)
    return drop
def Combat(enemyname,enemyplace):
    global Experience
    global CharLevel    
    global health
    MyAttack = 0
    EHealth = EnemyPlaceDict[enemyplace][3] 
    loop = 0
    for each in equipped:
        if toolsdict[str(each)].find("Two Handed") != -1 and loop == 0:
            loop +=1
            continue
        MyAttack+=each[1]*each[5] # 5 is the material type 
        loop += 1 # sole purpose is for the Two Handed weapons.
    MyAttack = (MyAttack*CharLevel)-EnemyPlaceDict[enemyplace][0] # armor is 0
    if MyAttack < 0:
        MyAttack = 0 # my attack*charlevel - his armor = my attack
    HisBlock = EnemyPlaceDict[enemyplace][2]
    ChanceOfHit = random.randint(0,10)
    if ChanceOfHit > HisBlock: # makes a chance of hitting. 2 is the block index
        EHealth -=  MyAttack #drop his health, the 3 index
        if EHealth <= 0:
            if bosslevel == False:
                print "You killed the %s!" % (enemyname) # not a bottom print because there are inputs afterwards 
            if bosslevel == True:
                bottomprint("You killed the %s!" % (enemyname)) # there aren't inputs afterwards about picking up something.            
            enemydrop = drop(EnemyPlaceDict[enemyplace])
            movement = terrain.index("I")-enemyplace
            Experience += EnemyPlaceDict[enemyplace][4]
            currentlevel = CharLevel
            #CharLevel = int(math.log(Experience)/math.log(1.46)) # Increases levels by 1.385^level = exp bar
            if CharLevel == 0:
                CharLevel = 1
            if Experience >= 1.46**(CharLevel+1) + 60*(CharLevel): # if experience >= than requirement, level up.
                CharLevel +=1
            if currentlevel < CharLevel: #level up!
                print "Congratulations, you've leveled up!"
                health = 10*CharLevel # increase my health by level
            if bosslevel == True: 
                slot = bodyparts.index(terrain[enemyplace])
                del bodyparts[slot] # deletes one part of Ungoliant.
            while True and bosslevel == False:
                armorInvenWeapon = enemydrop[0]*enemydrop[5]
                attackInvenWeapon = enemydrop[1]*enemydrop[5]
                blockInvenWeapon = enemydrop[2]
                
                attackChangeRightHand = attackInvenWeapon - (equipped[0][1]*equipped[0][5])
                blockChangeRightHand = blockInvenWeapon - equipped[0][2]
                
                armorChangeLeftHand = armorInvenWeapon - (equipped[1][0]*equipped[1][5]) # no armor for right hand because shields are always left
                attackChangeLeftHand = attackInvenWeapon - (equipped[1][1]*equipped[1][5])
                blockChangeLeftHand = blockInvenWeapon - equipped[1][2]            
                pickup = raw_input("Would you like to pick up: %s?\n(Armor: %s (%s)  Attack: %s RH (%s) LH (%s)  Block: %s RH (%s) LH (%s))" \
% ((toolsdict[str(enemydrop)]), armorInvenWeapon, armorChangeLeftHand, attackInvenWeapon, attackChangeRightHand, attackChangeLeftHand,\
blockInvenWeapon, blockChangeRightHand, blockChangeLeftHand)).strip()[:1]
                if pickup == "y":
                    arrowCount = 0
                    for each in inventory:
                        if toolsdict[str(each)].find("Arrow") != -1:
                            arrowCount += 1
                    if (len(inventory) - arrowCount) >= 10: # Carry unlimited arrows
                        bottomprint("You cannot carry anything else. Come back after you've dropped something.")
                        dropdictionary[enemyplace] = enemydrop
                        terrain[enemyplace] = '!' # removes his char from map once implemented
                        break
                    elif toolsdict[str(enemydrop)].find("Arrow") != -1: # if not too much space and drop is arrow.
                        for each in range(0,4): # appends 4x, 5 including last append.
                            inventory.append(enemydrop)
                    inventory.append(enemydrop)
                    break
                elif pickup == "n": 
                    break
                else:
                    print "The options are (yes) and (n)o."
            leaveperiod(enemyplace, movement)
            Retaliation()
            del EnemyPlaceDict[enemyplace]
        else:
            if toolsdict[str(equipped[0])].find("Lit Torch") != -1 or toolsdict[str(equipped[1])].find("Lit Torch") != -1:
                bottomprint("The torch's flames singe the %s" % (enemyname))
                EnemyPlaceDict[enemyplace][3] = EHealth
            else:
                bottomprint("You hit the %s" % (enemyname))
                EnemyPlaceDict[enemyplace][3] = EHealth
    if ChanceOfHit <= HisBlock: # these are all bottomprints because there aren't inputs after
        bottomprint("The %s blocked your attack." % (enemyname))
    Retaliation()
        
def Retaliation():
    global Experience
    global CharLevel
    global health
    idx = terrain.index("I")
    idxlist = []
    if idx % 81 > 8:        
        idxlist.append(idx - 9) #Top
    if idx % 81 < 80 and idx % 9 !=8:
        idxlist.append(idx + 1)#right
    if idx % 81 < 72:
        idxlist.append(idx + 9)#bottom
    if idx % 81 > 0 and idx % 9 != 0:
        idxlist.append(idx - 1)#left only these four because diagonals can't be moved in or attacked
    for position in idxlist:
        if position in EnemyPlaceDict.keys():  
            MyBlock = 0
            MyArmor = 0
            loop = 0
            enemyname = shop.EnemyDictNames[terrain[position]]
            for each in equipped:
                if toolsdict[str(each)].find("Two Handed") != -1 and loop == 0:
                    loop +=1
                    continue
                MyArmor+=each[0]*each[5]
                MyBlock+=each[2]    # block stays constant with shields, armor increases.
                loop += 1 # sole purpose is for the Two Handed weapons.
            HisAttack = EnemyPlaceDict[position][1]-MyArmor # his attack - my armor
            if HisAttack < 0:
                HisAttack = 0        
            ChanceOfHit = random.randint(0,10)
            if ChanceOfHit > MyBlock: # makes a chance of hitting. 
                health -= HisAttack #drop my health
                if health <= 0:
                    print "You were slain by the %s in the service of Middle Earth." % (enemyname)
                    raw_input("--End Game--")
                    sys.exit()
                bottomprint("The %s hit you!" % (enemyname))
            elif ChanceOfHit <= MyBlock:
                choice = random.randint(1,4)
                if choice == 1:
                    bottomprint("You dodged the %s's attack!" % (enemyname))
                else:
                    bottomprint("You blocked the %s's attack!" % (enemyname)) # far more common to block with weapons
                    
def EnemyLandscaping():
    global level
    global terrain
    PossEnemies = []
    for each in shop.enemies:
        if level >= 50:
            if each[6] == 50:
                PossEnemies.append(each)
        if level + 1 >= each[5] and level + 1 <= each[6]: # this finds which enemies can be found on the level. 
            PossEnemies.append(each)
    # Now the map has all types of possible enemies for the enemy and must chose which one.
    enemy = copy.deepcopy(random.choice(PossEnemies))
    # without deepcopy, the dictionary of enemies all reference the lists in shop, and a change to one changes the one in shop, thus them all. 
    # with deepcopy, all the enemies are actually individuals. This is why classes would be useful. 
    enemyAbbrDict = {1:"Y", 2:"H", 3:"A", 4:"D", 5:"O", 7:"K"}
    terrain.append(enemyAbbrDict[enemy[7]])
    EnemyPlaceDict[len(terrain)-1] = enemy
    
def WhichSpacesToView(idx): # this function prints the spaces around the I character. 
    numberlist = []
    numberlist.append(idx)
    if idx % 81 > 8:        
        numberlist.append(idx - 9) #Top
    if idx % 81 > 8 and idx % 9 != 8: # if not on top row or right column
        numberlist.append(idx - 8)#Top right
    if idx % 9 != 8:
        numberlist.append(idx + 1)#right
    if idx % 81 < 72 and idx % 9 !=8:
        numberlist.append(idx + 10)#bottom right
    if idx % 81 < 72:
        numberlist.append(idx + 9)#bottom
    if idx % 81 < 72 and idx % 9 != 0: # if not on bottom row or left column
        numberlist.append(idx + 8)#bottom left
    if idx % 9 != 0:
        numberlist.append(idx - 1)#left
    if idx % 81 > 8 and idx % 9 != 0:
        numberlist.append(idx - 10)#top left
    """
0  1  2  3  4  5  6  7  8
9  10 11 12 13 14 15 16 17
18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35
36 37 38 39 40 41 42 43 44
45 46 47 48 49 50 51 52 53
54 55 56 57 58 59 60 61 62
63 64 65 66 67 68 69 70 71
72 73 74 75 76 77 78 79 80"""
    for each in equipped:
        if toolsdict[str(each)].find("Lit Torch") != -1: #if torch is carried, see farther.
            if idx % 81 > 17 and terrain[idx - 9] != "-": #N and checks for wall       
                numberlist.append(idx - 18) 
            if idx % 81 > 17 and idx % 9 != 8 and not (terrain[idx-9] == "-" and terrain[idx-8] == "-"): #NNE checks for both as walls
                numberlist.append(idx - 17)
            if idx % 81 > 17 and idx % 9 < 7 and terrain[idx - 8] != "-": #NE
                numberlist.append(idx - 16)
            if idx % 81 > 6 and idx % 9 < 7 and not (terrain[idx-8] == "-" and terrain[idx+1] == "-"): #ENE
                numberlist.append(idx - 7)
            if idx % 9 < 7 and terrain[idx + 1] != "-": #E
                numberlist.append(idx + 2)
            if idx % 81 < 72 and idx % 9 < 7 and not (terrain[idx+1] == "-" and terrain[idx+10] == "-"): #ESE
                numberlist.append(idx + 11)
            if idx % 81 < 63 and idx % 9 < 7 and terrain[idx + 10] != "-": #SE
                numberlist.append(idx + 20)            
            if idx % 81 < 63 and idx % 9 != 8 and not (terrain[idx+9] == "-" and terrain[idx+10] == "-"): #SSE
                numberlist.append(idx + 19)
            if idx % 81 < 63 and terrain[idx + 9] != "-": #S
                numberlist.append(idx + 18)
            if idx % 81 < 63 and idx % 9 != 0 and not (terrain[idx+9] == "-" and terrain[idx+8] == "-"): #SSW
                numberlist.append(idx + 17)
            if idx % 81 < 63 and idx % 9 > 1 and terrain[idx+8] != "-": #SW
                numberlist.append(idx + 16)
            if idx % 81 < 72 and idx % 9 > 1 and not (terrain[idx-1] == "-" and terrain[idx+8] == "-"): #WSW
                numberlist.append(idx + 7)
            if idx % 9 > 1 and terrain[idx-1] != "-": #W
                numberlist.append(idx - 2)
            if idx % 81 > 10 and idx % 9 > 1 and not (terrain[idx-1] == "-" and terrain[idx-10] == "-"): #WNW
                numberlist.append(idx - 11)
            if idx % 81 > 19 and idx % 9 > 1 and terrain[idx-10] != "-": #NW
                numberlist.append(idx - 20)
            if idx % 81 > 18 and idx % 9 != 0 and not (terrain[idx-9] == "-" and terrain[idx-10] == "-"): #NNW
                numberlist.append(idx - 19)
    for each in numberlist:
        if each not in terrainnumbers:
            terrainnumbers.append(each)
def changeview():
    global terrainnumbers
    global viewterrain
    del viewterrain[:]
    loop = 0
    while loop < len(terrain):
        viewterrain.append(" ") # this makes viewterrain as long as terrain, so copying index to index works.
        loop+=1
    for each in terrainnumbers:
        viewterrain[each] = terrain[each] # terrainnumbers is the list of explored spaces. This function eliminates fog of exploration
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear') # Ternary operator!!! a if b else c    
# do a if b true otherwise do c! the nt is windows, and this won't work in Eclipse console.
def printhelp():
    clearscreen()
    print """
-COMMANDS-                 
w    move up             
a    move left          
s    move down           
d    move right          
h    print help          
D    drop item           
e    equip item 
u    unequip item
U    use item
i    view inventory
S    view your stats"""      
    raw_input("--Continue--")
    clearscreen()
    print """
--ADVANCED COMMANDS--
/exit    exit program with save opportunity given
/save    save program
/load    load another character"""
    raw_input("--Continue--")
    clearscreen()
    print """
--TERRAIN--
- or |  wall
.       open space
t       trap
/       stairs
!       equipment drop
I       You, the player %s""" % UserName
    raw_input("--Continue--")
    clearscreen()
    print """-ENEMIES-
Y    Young Barrow Wight
A    Adult Barrow Wight
O    Old Barrow Wight
K    King Barrow Wight
H    Crazed Hobbit
D    Crazed Dwarf"""           
    raw_input("--Continue--")
    clearscreen()
def printstats():
    global Experience
    global CharLevel
    global health
    loop = 0
    MyAttack = 0
    MyBlock = 0
    MyArmor = 0
    for each in equipped:
        if toolsdict[str(each)].find("Two Handed") != -1 or toolsdict[str(each)].find("Bow") != -1:
            if loop == 0:
                loop +=1
                continue
        MyArmor+=each[0]*each[5]
        MyAttack+=each[1]*each[5] # 5 is the material type
        MyBlock+=each[2]    # block stays constant with shields, armor increases.
        loop += 1 # sole purpose is for the Two Handed weapons.
    MyAttack = (MyAttack*CharLevel)
    MyBlock *= 10
    if MyBlock > 100:
        MyBlock = 100
    bottomprint("Health: %d    Attack: %d    Armor: %d    Block:%d%% percent chance    XP:%d    Character Level:%d" % (health,MyAttack,MyArmor,MyBlock,Experience,CharLevel))
def levelprint (NumberOfRows,level): # num is how big of square it reads. must be same as landscaper num.
    clearscreen()
    global bottommsg
    changeview()
    for currentRow in range(-1,NumberOfRows+1): # for each row. -1 and +1 for TopBottomWalls
        if currentRow == NumberOfRows  or currentRow == -1: #      |
            TopBottomWalls = ""                             #      |
            for currentRow in range(0,NumberOfRows):        #      |
                TopBottomWalls +="--"                       #      |
            TopBottomWalls +="-"                            #      |
            print TopBottomWalls                            #      V
        elif NumberOfRows > currentRow > -1:        # prints the different rows
            row = "|"                               # each row starts with a |
            for therownum in range(0,NumberOfRows): # makes the necessary number of %s for row. 2nd var is NumOfRows to make a square
                row+="%s "
            row = row[:len(row)-1] + "|"            # prints the row ending with another |
            print row % (viewterrain[(81*level) + (9*currentRow)],viewterrain[(81*level) + (9*currentRow)+1],viewterrain[(81*level) + (9*currentRow)+2],viewterrain[(81*level) + (9*currentRow)+3],viewterrain[(81*level) + (9*currentRow)+4],viewterrain[(81*level) + (9*currentRow)+5],viewterrain[(81*level) + (9*currentRow)+6],viewterrain[(81*level) + (9*currentRow)+7],viewterrain[(81*level) + (9*currentRow)+8])
    print "Character:" + UserName, " Depth:" + str(level + 1), "Health:" + str(health)
    print "Character Level:" + str(CharLevel), "Experience:" + str(Experience)
    if bottommsg != "":
        print bottommsg
    bottommsg = ""
def landscaper():
    del area[:]
    for each in range(1,81): # not 82 because 41 appends twice
        if each == 41: # not 40 because of the 1 starting range
            area.append(0) #starts you in center
            area.append(1) #starts stairs to your right
        else:
            area.append(random.randint(2,20))
    count = 0
    while count < len(area):
        symbol = area[count]
        count+=1
        if symbol == 0:
            terrain.append("I")
        elif symbol == 1:
            terrain.append("/")
        elif symbol in range(2,3): # this only counts the 2, not 2,3
            terrain.append("t")
        elif symbol in range(3,6):
            terrain.append("-")
        elif symbol in range(6,7) and level <= 50:
            EnemyLandscaping()
        elif symbol in range(6,11) and level > 50: # this quadruples the number of enemies past level 50.
            EnemyLandscaping()
        else:
            terrain.append(".")
def levelmove(oldpos):
    global level
    global terrain
    levelprint(9,level)
    while True:
        choice = raw_input("Would you like to vanquish another level of the Barrow-Downs?").lower().strip()[:1]
        index = terrain.index("I")
        if choice not in options:
            print "What was that? (yes/no)"
            continue
        elif choice == "y":
            if level == 0:
                landscaper()
                level = 1
                terrain[index] = "."
                terrain[40+level*81] = "I"         
            else: 
                nextchoice = raw_input("Would you like to go down, or up to the previous level? ").lower().strip()[:1]
                while nextchoice != "u" and nextchoice != "d":
                    nextchoice = raw_input("What was that? The options are up and down.").lower().strip()[:1]
                if nextchoice == "d":
                    level += 1           
                    landscaper()
                    terrain[index] = "."
                    terrain[40+level*81] = "I"
                    if level == 50:
                        clearscreen()
                        print "Prepare for high levels of combat!!!"
                        time.sleep(2)
                if nextchoice == "u":
                    level -= 1  
                    terrain[index] = "."
                    terrain[40+level*81] = "I"   # Up and down can be both (+) because level has already changed. 
# I don't use index because it won't put you on the left of the stairs
        elif choice == "n":
            terrain[index] = "."
            terrain[index-oldpos] = "I"
        break
def trap():
    global health
    traptype = random.randint(1,50)
    eventText = ""
    if traptype > 45:
        eventText = "You dodged a cave in!"
    elif traptype <= 10:
        eventText = "You are hit by an arrow from out of sight!"
        health-= (CharLevel*3) # 30% of max health
    elif 25 > traptype > 10:
        health-= (CharLevel*2) # 20% of max health
        if health <= 0:
            print "Cave in! You die beneath the ground, never to guard the Shire again."
            time.sleep(4)
            sys.exit()
        time.sleep(1)
        eventText = "Cave in! You wake up a little later with a severe headache."        
    elif 45 >= traptype >= 25:
        eventText = "You are bitten by a spider dropping from the ceiling"
        health-= CharLevel # 10% of max health
    if health <= 0:
        print eventText
        print "You are dead. The Dunedain will miss you."
        time.sleep(4)
        sys.exit()
    else:
        bottomprint(eventText)
#############################################
#
#
#            MOVE FUNCTIONS
#
#
#############################################
def leaveperiod(newpos,oldpos):
    global terrain
    terrain[newpos+oldpos] = "."
    terrain[newpos] = "I"
    if (newpos+oldpos) % 81 == 41 and bosslevel == False:        
        terrain[newpos+oldpos] = "/" # removes I from the stair
def move(number,newposition): # number is  same as the index number addition
    currentTerrain = terrain[newposition]
    if newposition in dropdictionary.keys():
        while True:
            arrowCount = 0
            for each in inventory:
                if toolsdict[str(each)].find("Arrow") != -1:
                    arrowCount += 1                    
            if (len(inventory) - arrowCount) >= 10: # Carry unlimited arrows            
                bottomprint("There's a %s here, but you're carrying too much." % toolsdict[str(dropdictionary[newposition])]) 
                break
            choice = raw_input("Would you like to pick up: %s? (Armor: %d  Attack: %d  Block: %d)" % (toolsdict[str(dropdictionary[newposition])],dropdictionary[newposition][0]*dropdictionary[newposition][5],dropdictionary[newposition][1]*dropdictionary[newposition][5],dropdictionary[newposition][2]))[:1] 
            if choice == "y":
                if toolsdict[str(dropdictionary[newposition])].find("Arrow") != -1: # if drop is arrow
                        for each in range(0,4): # appends 4x, 5 including last append.
                            inventory.append(dropdictionary[newposition])
                inventory.append(dropdictionary[newposition])
                del dropdictionary[newposition]
                leaveperiod(newposition, -number)
                break
            elif choice == "n": 
                leaveperiod(newposition, -number)
                del dropdictionary[newposition]
                break
            else:
                print "The options are (yes) and (n)o."
    if currentTerrain == "/" and bosslevel == False:
        levelmove(-number)
    elif currentTerrain == "t":
        trap()
        leaveperiod(newposition, -number)    
    elif currentTerrain == "." or currentTerrain == "!":
        leaveperiod(newposition, -number)  
    else:
        if currentTerrain in shop.EnemyDict:
            Combat(shop.EnemyDictNames[currentTerrain],newposition)
        if bosslevel == True:
            if newposition in EnemyPlaceDict:
                name = shop.EnemyDictNames[currentTerrain]
                Combat(name, newposition)
# no else because it includes killing enemies.
def moveright():
    newposition = terrain.index("I") +1 
    if newposition/9.0 == newposition/9: # already at right side of map
        bottomprint("You can't move through a wall!")
    elif terrain[newposition] != "-":
        move(1,newposition)
    elif terrain[newposition] == "-": 
        bottomprint("You can't move through a wall!") 
def moveleft():
    newposition = terrain.index("I")-1
    if (newposition+1)/9.0 == (newposition+1)/9: # already at left side of map
        bottomprint("You can't move through a wall!")
    elif terrain[newposition] != "-":
        move(-1,newposition)
    elif terrain[newposition] == "-": 
        bottomprint("You can't move through a wall!") 
def moveup():
    newposition = terrain.index("I")-9
    if (newposition+9)%81 < 9: # already at top side of map
        bottomprint("You can't move through a wall!")
    elif terrain[newposition] != "-":
        move(-9,newposition)
    elif terrain[newposition] == "-": 
        bottomprint("You can't move through a wall!") 
def movedown():
    newposition = terrain.index("I")+9
    if (newposition-9)%81 > 71: # already at top side of map
        bottomprint("You can't move through a wall!")
    elif terrain[newposition] != "-":
        move(9,newposition)
    elif terrain[newposition] == "-": 
        bottomprint("You can't move through a wall!") 
###############################
#
#
#        BOSS BATTLE
#
###############################
    
def animation():
    anime = """
    |
    |
    \\
     \\
      \\______,
             /
            /
      .____/
      \\
       \\
        \\
        |
        |
        |
       / \\\n"""
    idx = 1
    while True:
        idx = anime.find("\n", idx+1)
        idx2 = anime.find("\n",idx+1)
        print anime[idx:idx2],
        time.sleep(.2)
        if idx2-idx < 5:
            break
def bossmap():
    global intobosslevel
    global terrainnumbers
    global level
    intobosslevel = True
    bmap = """
. . . . . . . . . 
. . . . . . . . . 
. . . . . . . . . 
. . . . \ | | / . 
. . I = o ( ) } . 
. . . . / | | \ . 
. . . . . . . . . 
. . . . . . . . . 
. . . . . . . . . """
    for each in bmap:
        if each != " ":
            terrain.append(each)
    for each in terrain:
        if each == "\n":
            del terrain[terrain.index(each)]
    for each in range(len(terrain)-81,len(terrain)):
        terrainnumbers.append(each)
    level += 1
    terrain[terrain.index("I")] = "." # replaces the old I with a period.
    place = len(terrain)-81
    for each in bodyparts: 
        indx = terrain.index(each,place) # index of the body part in terrain.
        place = indx + 1
        EnemyPlaceDict[terrain.index(each,indx)] = [500,100,5,500,100,50,50,1] # adds the body part to enemies
def checker():
    global decision
    global bosslevel
    correct = 0
    bosslevel = False
    levelmap = []
    if intobosslevel == False: # Checks for me being at boss, if not and I can, puts me there.
        if equipped[1] == shop.AuleanNumenoreanShield:
            while decision == False: 
                droptoUngol = raw_input("Will you brave a fight with Ungoliant now? ").lower().strip()[:1]
                if droptoUngol == "y":
                    savegame()
                    print "You smash the ground with your shield and a crack opens. You jump in."
                    time.sleep(2)
                    clearscreen()
                    animation()
                    bossmap()
                    break
                elif droptoUngol == "n": 
                    bottomprint("When you want to fight her, use your Aulean Numenorean Shield.")
                    global useok 
                    useok = True
                    break
                else:
                    print "The options are (y)es and (n)o"
            decision = True
    for each in range(len(terrain)-81,len(terrain)): #puts the current map in levelmap and checks it for boss level
        levelmap.append(terrain[each])
    for each in bodyparts:
        if each in levelmap:
            correct += 1
    if correct == len(bodyparts): # if Ungoliant is in the map
        bosslevel = True
    if bosslevel == True and bodyparts == []:
        for each in range(len(terrain)-81,len(terrain)):
            if terrain[each] != "I": # if no body parts are left
                terrain[each] = "."
        clearscreen()
        print """Congratulations! You defeated the horrible Ungoliant! 
The Shire is safe from this terrible threat!"""
        raw_input("--End Game--")
        sys.exit()
###############################
#
#
#            MAIN BODY
#
###############################
decision = False
intobosslevel = False
opensavedfile(UserName)
idx = terrain.index("I")
WhichSpacesToView(idx)
print """%s, you are a ranger entering the Barrow-Downs to keep the Shire safe.
If you fail, the Shire will fall. May Aule go with you.""" % UserName
raw_input("--Continue--")
clearscreen()
for each in dropdictionary.keys():
        if terrain[each] == ".":
            terrain[each] = "!"
while True:
    for each in dropdictionary.keys():
        if terrain[each] == ".":
            terrain[each] = "!"
    if turn % 10 == 0 and health < CharLevel*10:
        health += (CharLevel/4) + 1
    if health > CharLevel*10:
        health = CharLevel*10
    idx = terrain.index("I")
    WhichSpacesToView(idx)
    checker()
    levelprint(9,level) # prints level and character stats.
    if bosslevel == True:
        if len(bodyparts) != 0:
            MyBlock = 0
            for each in equipped:
                MyBlock += each[2]
            if MyBlock > 10:
                MyBlock = 10
            ChanceOfHit = random.randint(0,13) # Ungoliant can even get by a Numenorean Shield with 50 damage
            if ChanceOfHit > MyBlock: # makes a chance of hitting. 
                bottomprint("Ungoliant hit you with a ranged attack!")
                health -= 50 
                if health <= 0:
                    clearscreen()
                    print """\
You died fighting the Shire's most dire foe, Ungoliant.
She leaves her cave and wreaks havoc on Middle Earth."""
                    raw_input("--End Game--")
                    sys.exit()
            if ChanceOfHit <= MyBlock:
                bottomprint("Ungoliant's ranged attack missed you.")
    action = raw_input().strip()
    if action == "": # they hit enter
        continue # this can't be a cheat to restore health!
    if action[:1] != "/":
        action = action[:1]
    while action not in commands:
        action = raw_input("That wasn't a valid command. Try again: ").strip()
        if action[:1] != "/":
            action = action[:1]
    if action[:1] == "/":
        if action == "/exit":
            exitgame()
        elif action == "/save":
            savegame()
            turn -= 1 # stops turn advancement of save
        elif action == "/load":
            load()
    elif action == "h":
        printhelp()
    elif action == "i":
        clearscreen()
        printInventory()
        raw_input("--Continue--")
        clearscreen()
    elif action == "D" or action == "e" or action == "u" or action == "U":
        inventoryfunc(action)
    elif action == "S":
        printstats()      
    turn+=1 #same line,two things,turn+=1
    if action == "d":
        moveright()
    elif action == "a":
        moveleft()
    elif action == "w":
        moveup()
    elif action == "s":
        movedown()
     
    