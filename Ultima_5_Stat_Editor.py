#filepath at C:/Ultima_5/SAVED.GAM where stats/items/characters are located
filePath = "/Ultima_5/SAVED.GAM"

# CHARACTER OFFSETS
charactersOffset = {"PLAYER" : int('0x02', 16),
                    "SHAMINO": int('0x22', 16),
                    "IOLO" : int('0x42', 16),
                    "MARIAH": int('0x62', 16),
                    "GEOFFREY": int('0x82', 16),
                    "JAANA": int('0xA2', 16),
                    "JULIA": int('0xC2', 16),
                    "DUPRE": int('0xE2', 16),
                    "KATRINA": int('0x102', 16),
                    "SENTRI": int('0x122', 16),
                    "GWENNO": int('0x142', 16),
                    "JOHNE": int('0x162', 16),
                    "GORN": int('0x182', 16),
                    "MAXWELL": int('0x1A2', 16),
                    "TOSHI": int('0x1C2', 16),
                    "SADUJ": int('0x1E2', 16)
                }

# STAT OFFSETS
# STAT LOCATIONS
# STRENGTH: 0XE(14) but offset is 0x0c(12) because player is at 0x02(2)
# Dexterity: 0XF(15) but offset is 0x0d(13) because player is at 0x02(2)
# ETC...
# STR/DEX/INT/MAGIC = Max(255) bc (2^8 -1) only represented in one offset
# HP/MAXHP/EXP = Max(65535) bc (2^16) -1 represented in two offset
# EX: HP = 0x12/0x13
statOffset = {"STRENGTH": int('0x0C', 16),
              "DEXTERITY": int('0x0D', 16),
              "INTELLIGENCE": int('0x0E', 16),
              "MAGIC": int('0x0F', 16),
              "HP": int('0x10', 16),
              "MAXHP": int('0x12', 16),
              "EXPERIENCE": int('0x14', 16)
             }

# ITEM OFFSETS
# items are shared between all characters so items are located in the corresponding offsets
# GOLD = MAX(65535) because its represented in two offsets
# KEYS/GEMS/MAGIC CARPET/SKULL KEYS/BLACK BADGE/MAGIC AXE= MAX(255) bc its represented in one offset
itemOffset = {"GOLD": int('0X204',16),
              "KEYS": int('0X206',16),
              "GEMS": int('0X207',16),
              "MAGIC CARPET": int('0X20A',16),
              "SKULL KEYS": int('0X20B',16),
              "BLACK BADGE": int('0X218',16),
              "MAGIC AXE": int('0X240',16),
              }


# open the file where ULTIMA/SAVED.GAM is at
def readData():
    with open(filePath, "rb") as save:
        #read and return as a byte array
        dataBytes = list(bytearray(save.read()))
        save.close()
        return dataBytes


# write the new data into ULTIMA/SAVED.GAM
def writeData(data):
    with open(filePath, "wb") as save:
        save.write(bytearray(data))
        save.close()


# get the max stat
# numbers are correlated to the options given to the user
def getMaxStat(choice):
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        return 255
    if choice == 5 or choice == 6 or choice == 7:
        return 65535


# return the stat name that they chose
def getStat(statChoice):
    return{
        1: "STRENGTH",
        2: "DEXTERITY",
        3: "INTELLIGENCE",
        4: "MAGIC",
        5: "HP",
        6: "MAXHP",
        7: "EXPERIENCE"
    }[statChoice]


# get the max quantity of an item
# numbers correlated to the option given to the user
def getMaxItems(itemChoice):
    if itemChoice == 1:
        return 65535
    else:
        return 255


# get the string of the item that the user selected
def getItem(itemChoice):
    return {
        1: "GOLD",
        2: "KEYS",
        3: "GEMS",
        4: "MAGIC CARPET",
        5: "SKULL KEYS",
        6: "BLACK BADGE",
        7: "MAGIC AXE",
    }[itemChoice]


# returns the character that they chose based on the int
def getCharacter(characterChoice):
    return {
        1: "PLAYER",
        2: "SHAMINO",
        3: "IOLO",
        4: "MARIAH",
        5: "GEOFFREY",
        6: "JAANA",
        7: "JULIA",
        8: "DUPRE",
        9: "KATRINA",
        10: "SENTRI",
        11: "GWENNO",
        12: "JOHNE",
        13: "GORN",
        14: "MAXWELL",
        15: "TOSHI",
        16: "SADUJ"
    }[characterChoice]


# get the byte array to change the code in the program
def getByteArray(maxValue,valueToEdit):
    # return the array of value of the bytes in terms of little endian
    # if max is 255, then it only affects 1 offset
    if maxValue == 255:
        return list(bytearray(valueToEdit.to_bytes(1, byteorder="little")))
    # if max is 65535, then it affects 2 offsets
    if maxValue == 65535:
        return list(bytearray(valueToEdit.to_bytes(2, byteorder="little")))


# function to change the stats of the characters
# first we want to ask for what character's stat they want to change
# after that get the maxValue of the stat
# ask the user to input the stat
def statEdit(data):
    # ask the user to select character he wishes to edit
    print("Stat Edit: Please select from the following stats you wish to edit."
          "\n1. PLAYER \n2. SHAMINO \n3. IOLO"
          "\n4. MARIAH \n5. GEOFFREY \n6. JAANA"
          "\n7. JULIA  \n8. DUPRE \n9. KATRINA"
          "\n10. SENTRI \n11. GWENNO \n12. JOHNE"
          "\n13. GORN  \n14. MAXWELL \n15. TOSHI"
          "\n16. SADUJ\n")
    # make sure it is an integer
    while (True):
        try:
            characterChoice = int(input())
        except ValueError:
            print("Please enter 1-16: ")
            continue
        # make sure it is between 1 and 16
        if characterChoice < 1 or characterChoice > 16:
            print("Please enter 1-16")
            continue
        else:
            break

    # get the string of the character selected
    characterSelected = getCharacter(characterChoice)
    print("Character selected is", characterSelected)

    # ask the user to select stat he wishes to edit
    print("Stat Edit: Please select from the following stats you wish to edit."
          "\n1. STRENGTH \n2. DEXTERITY \n3. INTELLIGENCE"
          "\n4. MAGIC \n5. HP \n6. MAXHP\n7. EXPERIENCE\n")

    # make sure it is an integer
    while (True):
        try:
            statChoice = int(input())
        except ValueError:
            print("Please enter 1-7: ")
            continue
        # make sure it is from 1 - 7
        if (statChoice < 1 or statChoice > 7):
            print("Please enter 1-7")
            continue
        else:
            break
    # get the string of the stat he wishes to edit
    statSelected = getStat(statChoice)
    print("State selected is", statSelected)

    # get the index of where the stat is located for the character
    index = charactersOffset[characterSelected] + statOffset[statSelected]

    # get the max value of the stat that the character can edit
    maxStatValue = getMaxStat(statChoice)
    # tell the user what the max value for the choice is
    print("Max value for " + statSelected + " is: ", maxStatValue)

    # ask for desire state value
    print("What value do you want to change this to? : ")
    # make sure it is an integer
    while (True):
        try:
            desiredStatValue = int(input())
        except ValueError:
            print("Please enter 1-",maxStatValue)
            continue
        if desiredStatValue < 1 or desiredStatValue > maxStatValue:
            print("Please enter 1-",maxStatValue)
            continue
        else:
            break

    # get the byte to change the value to
    byteArray = getByteArray(maxStatValue,desiredStatValue)

    counter = 0
    # will change only 1 value if only one offset is changed EX: DEX,INT,STR
    # will change 2 values if HP, MAXHP, EXP
    # loop through the array and change the binary in the offsets
    for n in byteArray:
        data[index + counter] = n
        counter += 1
    #inform that the stat is changed
    print(statSelected + " is updated to " ,desiredStatValue)
    # write to the data
    writeData(data)

def itemEdit(data):
    # ask the user to select character he wishes to edit
    print("Item Edit: Please select from the following items you wish to edit."
          "\n1. GOLD \n2. KEYS \n3. GEMS"
          "\n4. MAGIC CARPET \n5. SKULL KEYS \n6. BLACK BADGE"
          "\n7. MAGIC AXE")
    # make sure it is an integer
    while (True):
        try:
            itemChoice = int(input())
        except ValueError:
            print("Please enter 1-7: ")
            continue
        # make sure it is between 1 and 7
        if itemChoice < 1 or itemChoice > 7:
            print("Please enter 1-7")
            continue
        else:
            break

    #get the item that is selected based on the int
    itemSelected = getItem(itemChoice)
    print("Character selected is", itemSelected)

    # get the index of where the item is located in the file
    index = itemOffset[itemSelected]

    # get the max value of the stat that the character can edit
    maxItemValue = getMaxItems(itemChoice)

    # tell the user what the max value for the choice is
    print("Max value for " + itemSelected + " is: ", maxItemValue)

    # ask for desire state value
    print("What value do you want to change this to? : ")
    # make sure it is an integer
    while (True):
        try:
            desiredItemValue = int(input())
        except ValueError:
            print("Please enter 1-",maxItemValue)
            continue
        if desiredItemValue < 1 or desiredItemValue > maxItemValue:
            print("Please enter 1-",maxItemValue)
            continue
        else:
            break

    # get the byte to change the value to
    byteArray = getByteArray(maxItemValue,desiredItemValue)

    counter = 0
    # will change only 1 value if only one offset is changed, every item besides gold
    # will change 2 values if GOLD
    # loop through the array and change the binary in the offsets
    for n in byteArray:
        data[index + counter] = n
        counter += 1
    # inform that the stat is changed
    print(itemSelected + " is updated to " , desiredItemValue)
    # write to the data
    writeData(data)

def mainMenu():
    # open the file and read the data
    data = readData()
    choice = 0;

    # allow the program to run multiple times
    while choice != 3:
        print("Welcome cheater: Please select from the Following menu."
              "\n1. Edit Charcter Stats. \n2. Edit Item Quantities \n3. Save and End")
        # make sure it is an integer
        while True :
            try:
                choice = int(input())
            except ValueError:
                print("Please enter 1, 2 or 3 : ")
                continue
            if choice < 1 or choice > 3:
                print("Please enter 1, 2 or 3")
                continue
            else:
                break

        # inform the user of the choice they selected
        print("You selected", choice)

        #based on choice, call specific functions
        if choice == 1:
            statEdit(data)
        if choice == 2:
            itemEdit(data)

mainMenu()