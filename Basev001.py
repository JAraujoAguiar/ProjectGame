import time
import turtle

#-------------------------Classes----------------------#
class Inventory: #Handles inventory management
    inventory = ["space", "item"]
    
    def AddInventory(self, item):
        Inventory.inventory.append(item)
        print(f"\nYou place {item} in your inventory\n")
        return(Inventory.inventory)

class Timer: #Handles matters of time
    time = 30
    
    def Ticking(self, tick):
        Timer.time = Timer.time - tick
        if Timer.time < 0:
            Timer.time = 0
            Timer.Passing
            print(f"\nYou have {Timer.time} minutes left\n")
            Timer.Passing
            return(Timer.time) 

        elif Timer.time == 1:
            Timer.Passing
            print(f"\nYou have {Timer.time} minute left\n")
            Timer.Passing
            return(Timer.time) 

        else:
            Timer.Passing
            print(f"\nYou have {Timer.time} minutes left\n")
            Timer.Passing
            return(Timer.time) 
               

    def Passing():
        time.sleep(2)

class Game: #Handles the game interactions and responses

    def Over():
        print("\nYour mind drifts away as the current washes your body away... \n")
        Timer.Ticking(Timer.time, 30)
        print("GAME OVER")
    
    def BadAnswer():
        print("\nYou can't seem to think straight... \n")
        seed = Game.Over()

    def Drown():
        Timer.Passing()
        print("\nWater has filled out the room\n")
        Timer.Passing()
        print("\nIn a futile effort to survive you cling to the last air pocket in the room\n")
        Timer.Passing()
        print("\nIt is quickly filled out with water and so are your lungs\n")
        Timer.Passing()
        seed = Game.BadAnswer()


    def Start():
        print(f"\nSlowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...\n")
        Timer.Passing()
        answer = input("Would you open your eyes? (yes/no) \n \n").lower().strip()
        if answer == "yes":
            game.Q1()
        elif answer == "no":
            game.Over()
        else:
            game.BadAnswer()
        
    def Q1():
        Timer.Ticking(Timer.time, 0)
        print("\nIt's dark, however a small crack on the ceiling gives just enough light to make your sorroundings... \n")
        Timer.Passing()
        print("\nYou are able to hear water rushing in from somewhere you cannot see...\n")
        Timer.Passing()
        answer = input("\n What would you like to do? (Look around/Close eyes)\n\n").lower().strip()

        if answer == "look around":
            game.Q2a()

        elif answer == "close eyes":
            game.Over()

        else:
            game.BadAnswer()
    
    def Q2a():
        Timer.Ticking(Timer.time, 1)
        print("\nYou can make out in the darkness a section of the wall that seems to have some loose rocks...\n")
        Timer.Passing()
        answer = input("What would you do? (Get closer/Keep looking)\n").lower().strip()

        if answer == "get closer":
            answer = None
            game.Q3

        elif answer == "keep looking":
            answer = None
            for item in Inventory.inventory:
                if item == 'Macuahuitl':
                    print("\nYou don't see anything else that might be relevant")
                    game.Q2a()
            
                else:
                    Timer.Passing()
                    game.Q2b()

        else:
            game.BadAnswer()

    def Q2b():
        Timer.Passing()
        print("You see a Macuahuitl lying on the floor...")
        Timer.Passing()
        answer = input("What would you do? (Take/Go back)").lower().strip()

        if answer == "take":
            answer = None
            Inventory.AddInventory(Inventory.inventory, "Macuahuitl")
            game.Q2a()

        elif answer == "go back":
            answer = None
            game.Q2a()
        
        elif answer == "what is a macuahuitl?":
            print("A macuahuitl is a weapon, a wooden club with several embedded obsidian blades. The name is derived from the Nahuatl language and means hand-wood. Its sides are embedded with prismatic blades traditionally made from obsidian. Obsidian is capable of producing an edge sharper than high quality steel razor blades. The macuahuitl was a standard close combat weapon.")
            Timer.Ticking(Timer.time, 30)

        else:
            game.BadAnswer()
        
    def Q3():
        print("To be continued...")
        
#-------------------------GameInit----------------------#

game = Game
game.Start()


