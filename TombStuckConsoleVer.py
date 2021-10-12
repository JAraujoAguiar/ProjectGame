import time
import pandas as pd

#-------------------------Classes----------------------#
class Leaderboard: #Handles the input to 
    name = ['Jesus A']
    ending = [True]
    score = ['30'] 

    def Stamp(name, ending, score):
        Leaderboard.name.append(name)
        Leaderboard.ending.append(ending)
        Leaderboard.score.append(score)
        leaderboard = pd.DataFrame({'Name': Leaderboard.name, 'Ending': Leaderboard.ending, 'Score': Leaderboard.score})
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

    def Print(phrase):
        Timer.Passing()
        print(f'\n{phrase}\n')

    def Question(question):
        Game.answer = input(f'\n{question}\n')
        return(Game.answer)

    def Over():
        Timer.Ticking(Timer.time, 30)
        Game.Print("Your mind drifts away as the current washes your body away...")
        Game.Print("GAME OVER")
        Game.ending = False
        Leaderboard.Stamp(Game.name, Game.ending, Game.score)
    
    def BadAnswer():
        Game.Print("\nYou can't seem to think straight... \n")
        seed = Game.Over()

    def Drown():
        Game.Print("Water has filled out the room")
        Game.Print("In a futile effort to survive you cling to the last air pocket in the room")
        Game.Print("It is quickly filled out with water and so are your lungs")
        seed = Game.BadAnswer()

    def Win():
        Game.Print("You crawl out of the hole you made in the wall...")
        Game.Print("Although you still don't know how you got there...")
        Game.Print("However, soon after reaching the surface...")
        Game.Print("You realize why you were there.")
        Game.Print("TO BE CONTINUED")
        Leaderboard.Stamp(Game.name, Game.ending, Game.score)


    def TimerCheck():
        if Timer.time <= 0:
            Game.Drown()
        else:
            pass

    def Start():
        Game.Print(f"Slowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...")
        Game.Question("Would you open your eyes? (yes/no)")
        if Game.answer == "yes":
            Game.Q1()
        elif Game.answer == "no":
            Game.Over()
        else:
            Game.BadAnswer()
        
    def Q1():
        Timer.Ticking(Timer.time, 0)
        Game.Print("It's dark, however a small crack on the ceiling gives just enough light to make your sorroundings...")
        Game.Print("You are able to hear water rushing in from somewhere you cannot see...")
        Timer.Passing()
        Game.Question("What would you like to do? (Look around/Close eyes)")

        if Game.answer == "look around":
            Game.Q2a()

        elif Game.answer == "close eyes":
            Game.Over()

        else:
            Game.BadAnswer()
    
    def Q2a():
        Game.TimerCheck()
        Timer.Ticking(Timer.time, 1)
        Game.Print("You can make out in the darkness a section of the wall that seems to have some loose rocks...")
        Game.Question("What would you do? (Get closer/Keep looking)")

        if Game.answer == "get closer":
            Game.Q3()

        elif Game.answer == "keep looking":
            if 'Macuahuitl' in Inventory.inventory:
                Game.Print("You don't see anything else that might be relevant")
                Game.Q2a()
    
            else:
                Game.Q2b()

        else:
            Game.BadAnswer()

    def Q2b():
        Game.TimerCheck()
        Game.Print("You see a Macuahuitl lying on the floor...")
        Game.Question("What would you do? (Take/Go back)")

        if Game.answer == "take":
            Inventory.AddInventory('Macuahuitl')
            Game.Q2a()

        elif Game.answer == "go back":
            Game.Q2a()
        
        elif Game.answer == "what is a macuahuitl?":
            Game.Print("A macuahuitl is a weapon, a wooden club with several embedded obsidian blades. The name is derived from the Nahuatl language and means hand-wood. Its sides are embedded with prismatic blades traditionally made from obsidian. Obsidian is capable of producing an edge sharper than high quality steel razor blades. The macuahuitl was a standard close combat weapon.")
            Timer.Ticking(Timer.time, 30)

        else:
            Game.BadAnswer()
        
    def Q3():
        Game.TimerCheck()
        Game.Print('You see that water trickles through this wall...')
        Game.Print('You think that if you hit the wall hard enough you can bring it down...')
        Game.Question('What would you do? (Hulk Smash/Keep Looking)')
        if Game.answer == "hulk smash":
            if 'Macuahuitl' in Inventory.inventory:
                Game.Print("You use the Macuahuitl to smash the wall in with all your might...")
                Game.Print("The wall gives away, revealing a passage to the outside...")
                Game.Win()
            else:
                Timer.Ticking(Timer.Ticking, 10)
                Game.Print("You try for a good while to hit the wall but it seems that your bare hands can't do much")
                Game.Q3()

        elif Game.answer == "keep looking":
            if 'Macuahuitl' in Inventory.inventory:
                Game.Print("You don't see anything else that might be relevant")
                Game.Q3()

            else:
                Game.Q2b()

        
#-------------------------GameInit----------------------#

game = Game
game.name = game.Question('What is your name?')
game.Start()
