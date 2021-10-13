import time
#import pandas as pd

#-------------------------Classes----------------------#
class Leaderboard: #Handles the input to 
    name = ['Jesus A']
    ending = [True]
    score = ['30'] 

    def Stamp(Self, name, ending, score):
        Self.name.append(name)
        Self.ending.append(ending)
        Self.score.append(score)
        #leaderboard = pd.DataFrame({'Name': Leaderboard.name, 'Ending': Leaderboard.ending, 'Score': Leaderboard.score})
        leaderboard = [Self.name, Self.ending, Self.score]
        print(f'Leaderboard: \n \n {leaderboard}')


class Inventory: #Handles inventory management
    inventory = [None]

    def AddInventory(item):
        Inventory.inventory.append(item)
        print(f"\nYou place {item} in your inventory\n")

class Timer: #Handles matters of time
    time = 30
    
    def Ticking(self, tick):
        Timer.time = Timer.time - tick
        if Timer.time < 0:
            Timer.time = 0
            Timer.Passing()
            print(f"\nYou have {Timer.time} minutes left\n")
            Timer.Passing
            return(Timer.time) 

        elif Timer.time == 1:
            Timer.Passing()
            print(f"\nYou have {Timer.time} minute left\n")
            Timer.Passing
            return(Timer.time) 

        else:
            Timer.Passing()
            print(f"\nYou have {Timer.time} minutes left\n")
            Timer.Passing()
            return(Timer.time) 

    def Passing():
        time.sleep(3)

class Game: #Handles the game interactions and responses
    name = None
    ending = True
    score = Timer.time
    answer = None
    inventory = Inventory.inventory

    def Print(phrase):
        Timer.Passing()
        print(f'\n{phrase}\n')

    def Question(Self, question):
        Self.answer = input(f'\n{question}\n')
        return(Self.answer)

    def Over(Self):
        Timer.Ticking(Timer.time, 30)
        Self.Print("Your mind drifts away as the current washes your body away...")
        Self.Print("GAME OVER")
        Self.ending = False
        Leaderboard.Stamp(Self.name, Self.ending, Self.score)
    
    def BadAnswer(Self):
        Self.Print("\nYou can't seem to think straight... \n")
        seed = Self.Over()

    def Drown(Self):
        Self.Print("Water has filled out the room")
        Self.Print("In a futile effort to survive you cling to the last air pocket in the room")
        Self.Print("It is quickly filled out with water and so are your lungs")
        seed = Self.BadAnswer()

    def Win(Self):
        Self.Print("You crawl out of the hole you made in the wall...")
        Self.Print("Although you still don't know how you got there...")
        Self.Print("However, soon after reaching the surface...")
        Self.Print("You realize why you were there.")
        Self.Print("TO BE CONTINUED")
        Leaderboard.Stamp(Self.name, Self.ending, Self.score)


    def TimerCheck(Self):
        if Timer.time <= 0:
            Self.Drown()
        else:
            pass

    def Start(Self):
        Self.Print(f"Slowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...")
        Self.Question("Would you open your eyes? (yes/no)")
        if Self.answer == "yes":
            Self.Q1()
        elif Self.answer == "no":
            Self.Over()
        else:
            Self.BadAnswer()
        
    def Q1(Self):
        Timer.Ticking(Timer.time, 0)
        Self.Print("It's dark, however a small crack on the ceiling gives just enough light to make your sorroundings...")
        Self.Print("You are able to hear water rushing in from somewhere you cannot see...")
        Timer.Passing()
        Self.Question("What would you like to do? (Look around/Close eyes)")

        if Self.answer == "look around":
            Self.Q2a()

        elif Self.answer == "close eyes":
            Self.Over()

        else:
            Self.BadAnswer()
    
    def Q2a(Self):
        Self.TimerCheck()
        Timer.Ticking(Timer.time, 1)
        Self.Print("You can make out in the darkness a section of the wall that seems to have some loose rocks...")
        Self.Question("What would you do? (Get closer/Keep looking)")

        if Self.answer == "get closer":
            Self.Q3()

        elif Self.answer == "keep looking":
            if 'Macuahuitl' in Self.inventory:
                Self.Print("You don't see anything else that might be relevant")
                Self.Q2a()
    
            else:
                Self.Q2b()

        else:
            Self.BadAnswer()

    def Q2b(Self):
        Self.TimerCheck()
        Self.Print("You see a Macuahuitl lying on the floor...")
        Self.Question("What would you do? (Take/Go back)")

        if Self.answer == "take":
            Inventory.AddInventory('Macuahuitl')
            Self.Q2a()

        elif Self.answer == "go back":
            Self.Q2a()
        
        elif Self.answer == "what is a macuahuitl?":
            Self.Print("A macuahuitl is a weapon, a wooden club with several embedded obsidian blades. The name is derived from the Nahuatl language and means hand-wood. Its sides are embedded with prismatic blades traditionally made from obsidian. Obsidian is capable of producing an edge sharper than high quality steel razor blades. The macuahuitl was a standard close combat weapon.")
            Timer.Ticking(Timer.time, 30)

        else:
            Self.BadAnswer()
        
    def Q3(Self):
        Self.TimerCheck()
        Self.Print('You see that water trickles through this wall...')
        Self.Print('You think that if you hit the wall hard enough you can bring it down...')
        Self.Question('What would you do? (Hulk Smash/Keep Looking)')
        if Self.answer == "hulk smash":
            if 'Macuahuitl' in Self.inventory:
                Self.Print("You use the Macuahuitl to smash the wall in with all your might...")
                Self.Print("The wall gives away, revealing a passage to the outside...")
                Self.Win()
            else:
                Timer.Ticking(Timer.Ticking, 10)
                Self.Print("You try for a good while to hit the wall but it seems that your bare hands can't do much")
                Self.Q3()

        elif Self.answer == "keep looking":
            if 'Macuahuitl' in Self.inventory:
                Self.Print("You don't see anything else that might be relevant")
                Self.Q3()

            else:
                Self.Q2b()

        
#-------------------------GameInit----------------------#

game = Game
game.name = game.Question('What is your name?')
game.Start()
