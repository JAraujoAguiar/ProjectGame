import time
#import tkFont
import pandas as pd
from tkinter import *
from tkinter import messagebox


window = Tk()

#window.geometry('500*250')
#font = tkFont.Font ()

'''
def enter():
    answer = Game.answer.get()
    return(answer)
'''
#-------------------------Classes----------------------#
class Leaderboard: #Handles the input to 
    name = ['Jesus A']
    ending = [True]
    score = ['30'] 

    def Stamp(self, name, ending, score):
        self.name.append(name)
        self.ending.append(ending)
        self.score.append(score)
        leaderboard = pd.DataFrame({'Name': self.name, 'Ending': self.ending, 'Score': self.score})
        #leaderboard = leaderboard.sort([score], ascending=[1])
        Game.Print(f'Leaderboard: \n \n {leaderboard}')
        print(f'Leaderboard: \n \n {leaderboard}')


class Inventory: #Handles inventory management
    inventory = [None]
    
    def AddInventory(self, item):
        self.inventory.append(item)
        print(f"\nYou place {item} in your inventory\n")
        return(self.inventory)

class Timer: #Handles matters of time
    time = 30
    
    def Ticking(tick):
        Timer.time = Timer.time - tick
        if Timer.time < 0:
            Timer.time = 0
            Timer.Passing
            Label(window, text=f"\nYou have {Timer.time} minutes left\n", bg='black', fg="white", font="none 12 bold").grid(row=Game.row, column=0, sticky=W)
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
        time.sleep(3)

class Game(Tk): #Handles the game interactions and responses
    name = None
    ending = True
    score = Timer.time
    answer = None
    input = None
    row = 0
    
    def MainLoop(self):
       super().mainloop()
       self.Start() 


    def Print(self, phrase):
        Timer.Passing()
        Label (self, text=f'\n{phrase}\n\n', bg='black', fg="white", font="none 12 bold").grid(row=Game.row, column=0, sticky=W)
        self.row = self.row + 1
        return(self.row)

    def Question(self, question):
        self.Print(question)
        self.input = Entry(bg='black', fg="white", font="none 12 bold")
        self.input.grid(row=self.row, column=0, sticky=W)
        self.input.bind('<Return>', enter)
        print(self.input)
        self.answer = self.input


    def Over(self):
        Timer.Ticking(Timer.time, 30)
        self.Print("Your mind drifts away as the current washes your body away...")
        self.Print("GAME OVER")
        self.ending = False
        Leaderboard.Stamp(self.name, self.ending, self.score)
    
    def BadAnswer(self):
        self.Print("\nYou can't seem to think straight... \n")
        seed = self.Over()

    def Drown(self):
        self.Print("Water has filled out the room")
        self.Print("In a futile effort to survive you cling to the last air pocket in the room")
        self.Print("It is quickly filled out with water and so are your lungs")
        seed = self.BadAnswer()

    def Win(self):
        self.Print("You crawl out of the hole you made in the wall...")
        self.Print("Although you still don't know how you got there...")
        self.Print("However, soon after reaching the surface...")
        self.Print("You realize why you were there.")
        self.Print("TO BE CONTINUED")
        Leaderboard.Stamp(self.name, self.ending, self.score)


    def TimerCheck(self):
        if Timer.time <= 0:
            self.Drown()
        else:
            pass

    def Start(self):
        self.Print(f"Slowly you come back to. Your head is throbbing, your body aches and your eyes are heavy...")
        self.Question("Would you open your eyes? (yes/no)")
        if self.answer == "yes":
            self.Q1()
        elif self.answer == "no":
            self.Over()
        else:
            self.BadAnswer()
        
    def Q1(self):
        Timer.Ticking(Timer.time, 0)
        self.Print("It's dark, however a small crack on the ceiling gives just enough light to make your sorroundings...")
        self.Print("You are able to hear water rushing in from somewhere you cannot see...")
        Timer.Passing()
        self.Question("What would you like to do? (Look around/Close eyes)")

        if self.answer == "look around":
            self.Q2a()

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
            for item in Inventory.inventory:
                if item == 'Macuahuitl':
                    Game.Print("You don't see anything else that might be relevant")
                    Game.Q2a()
    
                else:
                    Game.Q2b()
                
                break

        else:
            Game.BadAnswer()

    def Q2b():
        Game.TimerCheck()
        Game.Print("You see a Macuahuitl lying on the floor...")
        Game.Question("What would you do? (Take/Go back)")

        if Game.answer == "take":
            Inventory.AddInventory(Inventory.inventory, 'Macuahuitl')
            Game.Q2a()

        elif Game.answer == "go back":
            Game.Q2a()
        
        elif Game.answer == "what is a macuahuitl?":
            Game.Print("A macuahuitl is a weapon, a wooden club with several embedded obsidian blades. \nThe name is derived from the Nahuatl language and means hand-wood. \nIts sides are embedded with prismatic blades traditionally made from obsidian. \nObsidian is capable of producing an edge sharper than high quality steel razor blades. \nThe macuahuitl was a standard close combat weapon.")
            Timer.Ticking(Timer.time, 30)

        else:
            Game.BadAnswer()
        
    def Q3():
        Game.TimerCheck()
        Game.Print('You see that water trickles through this wall...')
        Game.Print('You think that if you hit the wall hard enough you can bring it down...')
        Game.Question('What would you do? (Hulk Smash/Keep Looking)')
        if Game.answer == "hulk smash":
            for item in Inventory.inventory:
                if item == 'Macuahuitl':
                    Game.Print("You use the Macuahuitl to smash the wall in with all your might...")
                    Game.Print("The wall gives away, revealing a passage to the outside...")
                    Game.Q2a()
                else:
                    Timer.Ticking(Timer.Ticking, 10)
                    Game.Print("You try for a good while to hit the wall but it seems that your bare hands can't do much")
                    Game.Q3()
                break

        elif Game.answer == "keep looking":
            for item in Inventory.inventory:
                if item == 'Macuahuitl':
                    Game.Print("You don't see anything else that might be relevant")
                    Game.Q3()

                else:
                    Game.Q2b()
                
                break

        
#-------------------------GameInit----------------------#

game = Game()
game.title("Tomb Stuck")
game.configure(background="black")
game.name = game.Question('What is your name?')
game.Start()
game.mainloop()