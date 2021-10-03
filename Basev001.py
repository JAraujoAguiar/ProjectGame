import time
import turtle

#-------------------------Classes----------------------#
class Inventory:
    inventory = [None]

    def AddInventory(self, item):
        Inventory.inventory.append(item)
        print("\nYou place {item} in your inventory\n")
        return(Inventory.inventory)

class Timer:
    time = 30
    
    def Ticking(self, tick):
        Timer.time = Timer.time - tick
        print("\nYou have {time} minutes left\n")
        return(Timer.time)      

class Game:

    def Over(self):
        print("\nYour mind drifts away as the current washes your body away... \n")
        time.sleep(3)
        print("GAME OVER")
    
    def BadAnswer(self):
        print("\n You can't seem to think straight... \n")
        time.sleep(3)
        seed = Game.Over(None)

    def Q1(self):
        print(f"\nSlowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...\n")
        time.sleep(3)
        answer = input("Would you open your eyes? (yes/no) \n \n")
        return(answer)

    def Q2(answer):
        pass
        
#-------------------------GameInit----------------------#

tick = Timer.Ticking
game = Game

#Darken the font
tick(0,0)
#-------------------------------------------Q1--------------------------------------------#
game.Q1(None)
game.Q2(game.Q1.answer)

#print(f"\nSlowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...\n")
#time.sleep(3)
#answer = input("Would you open your eyes? (yes/no) \n \n")

#-------------------------------------------Q2--------------------------------------------#

if answer.lower().strip() == "yes":
    #Brigten the font
    tick(0,0)
    print("\nIt's dark, however a small crack on the ceiling gives just enough light to make your sorroundings... \n")
    time.sleep(3)
    #Play rushing_water.mp3
    print("\nYou are able to hear water rushing in from somewhere you cannot see...")
    time.sleep(1)
    print("\n What would you like to do?\n\n")

    answer = input("Look around/Close your eyes and drift away")

    if answer.lower().strip() == "lookaround":
        print("\n You can make out in the darkness a door with a dial that covers the middle section...\n")
        tick(1)
        answer = input("What would you do? (Get Closer/Keep Looking)")

        if answer.lower().strip() == "getcloser":
            print()

    #elif answer.lower().strip() == "closeyoureyesanddriftaway","closeyoureyes","driftaway":
        #print()

    else:
        game.BadAnswer(None)

#-------------------------------------------Q2--------------------------------------------#

elif answer.lower().strip() == "no":
    game.Over(None)

else:
    game.BadAnswer(None)
#-------------------------------------------Q1--------------------------------------------#


        
