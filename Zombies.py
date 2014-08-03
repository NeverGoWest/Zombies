import random
import sys

tilenames = ["Ruin", "Street", "House", "Gun Store", "Super Market", "Park", "Police Station", "Fire Station"]
tilechars = ["##", "--", "[]", "GS", "SM", "PP", "PS", "FS"]
#tileloot = [[junk, pammo,

class Item:
    def __init__(self):
        self.name = "Error"
        self.desc = "You found a bug, holy shit!"
        self.weight = 0
        self.dmg = 0
        self.tohit = 0
        self.drop = 1
    def Use(self):
        pass

o_knife = Item()
o_knife.name = "Knife"
o_knife.desc = "A sharp blade"
o_knife.weight = 1
o_knife.dmg = 3
o_knife.tohit = 3

o_trash = Item()
o_trash.name = "Trash"
o_trash.desc = "Useless piece of trash"

o_pipe = Item()
o_pipe.name = "Pipe"
o_pipe.desc = "A sturdy iron pipe."
o_pipe.dmg = 2
o_pipe.tohit = 2

o_fist = Item()
o_fist.name = "Fists."
o_fist.desc = "Your fists, dont drop theese, that is bad!"
o_fist.dmg = 1
o_fist.tohit = 2
o_fist.drop = 0

class Enemy:
    def __init__(self):
        self.name = "Raider"
        self.tohit = 3
        self.dmg = 3
        self.health = 5
    def hit(self):
        hit = random.randint(0, 6)

        if hit >= player.tohit:
            player.health -= self.dmg
            print("You were hit for ", self.dmg, " damage!")

e_zombie = Enemy()
e_zombie.name = "Zombie"
e_zombie.tohit = 4
e_zombie.dmg = 2

class MapTile:
    def Display(self):
        print(self.name)
        print("")
        print(self.desc)
    def __init__(self):
        self.name = tilenames[random.randint(0, 6)]
        self.type = random.randint(0, 7) # 0 street 1 house 2 gun store 3 general store 4 park 5 police station 6 fire station
        self.loot = [o_trash, o_knife, o_pipe]
        self.contents = [o_trash]
        self.monster = [e_zombie]
    def killmonster(self, monster):
        print(monster.name, " dies!")
        self.monster.pop(index(monster))
        




class PClass:
    def __init__(self):
        self.str = random.randint(1, 6)
        self.int = random.randint(1, 6)
        self.per = random.randint(1, 6)
        self.dex = random.randint(1, 6)

        self.hp = 10

        self.x = 2
        self.y = 2
        self.inv = [o_trash, o_knife]
        self.wielded = o_fist

        self.dir = ["n", "s", "w", "e"]

        self.tohit = 3
    def scavenge(self):
        lootx = random.randint(0, len(gmap[player.x][player.y].loot))
        self.inv.append(gmap[player.x][player.y].loot[lootx]) #random.randint(0, len(gmap[player.x][player.y].loot))]
    def listinv(self):
        print("INV:")
        slot = 0
        for item in self.inv:
            print(slot, item.name)
            slot += 1
    def wield(self, item):
        #self.wielded = item
        #self.inv.pop(self.inv.index(item))
        for 
    def unwield(self):
        self.inv.append(self.wielded)
        self.wielded = o_fist
    def move(self, direction):
        if direction == "n" and y >= 0:
            self.y = self.x - 1
            print("You walk north.")
            return
        elif direction == "s" and y <= 10:
            self.y = self.x + 1
            print("You walk south.")
            return
        elif direction == "e" and x <= 10:
            self.x = self.x + 1
            print("You walk east.")
            return
        elif direction == "w" and x >= 0:
            self.x = self.x - 1
            print("You walk west.")
            return
        else:
            print("You cannot walk that direction!")
            return
        
            
        
gmap = [[MapTile() for _ in range(10)] for _a in range(10)]
player = PClass()


        
        



def gett(typ):
    return tilechars[typ]

def dispmap():
    print(gett(gmap[player.x - 1][player.y - 1].type), gett(gmap[player.x][player.y - 1].type), gett(gmap[player.x + 1][player.y - 1].type))
    print(gett(gmap[player.x - 1][player.y].type), gett(gmap[player.x][player.y].type), gett(gmap[player.x + 1][player.y].type))
    print(gett(gmap[player.x - 1][player.y + 1].type), gett(gmap[player.x][player.y + 1].type), gett(gmap[player.x + 1][player.y + 1].type))

monsters = [e_zombie, e_zombie, Enemy]

def encounter():
    montype = random.randint(0, len(monsters))
    monster = monsters[montype]
    
#def listinv():
#    print("INV:")
#    for item in player.inv:
#        print(item.name)
def GameLoop():
    com = ""
    while com != "quit":
        com = input("> ") # input to string
        com = com.lower()
        # print(com)
        comargs = com.split() # split up the string to take arguments
        

        if comargs[0] == "move":
            pass
        

GameLoop()



