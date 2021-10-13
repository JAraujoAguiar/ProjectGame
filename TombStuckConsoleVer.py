import time
import pandas as pd

#-------------------------Script------------------------#
scriptOver = ["Your mind drifts away as the current washes your body away...", "GAME OVER"]
scriptBadAnswer = ["You can't seem to think straight..."]
scriptDrown = ["Water has filled out the room...", 'In a futile effort to survive you cling to the last air pocket in the room...', 'The space is quickly filled out with water and so are your lungs...']    
scriptWin = ["You crawl out of the hole you made in the wall...", "Although you still don't know how you got there...", "Soon after reaching the surface...", "You realize why you were there.", "TO BE CONTINUED"]
scriptGen0 = ["You don't see anything else that might be relevant"]
scriptGen1 = ["You see a Macuahuitl lying on the floor..."]
scriptGen2 = ["A macuahuitl is a weapon, a wooden club with several embedded obsidian blades. The name is derived from the Nahuatl language and means hand-wood. Its sides are embedded with prismatic blades traditionally made from obsidian. Obsidian is capable of producing an edge sharper than high quality steel razor blades. The macuahuitl was a standard close combat weapon."]
scriptGen3 = ["You try for a good while to hit the wall but it seems that your bare hands can't do much"]
script0 = ["Slowly, you come back to...", "Your head is throbbing, your body aches and your eyes are heavy..."]
question0 = ["Would you open your eyes? (yes/no)"]
script1 = ["It's dark, however a small crack on the ceiling gives just enough light to make your sorroundings...", "You are able to hear water rushing in from somewhere you cannot see..."]
question1 = ["What would you like to do? (Look around/Close eyes)"]
script2a = ["You can make out in the darkness a section of the wall that seems to have some loose rocks..."]
question2a = ["What would you like to do? (Look around/Close eyes)"]
script2b = ["You see a Macuahuitl lying on the floor..."]
question2b = ["What would you do? (Take/Go back)"]
script3a = ["You see that water trickles through this wall...", "You think that if you hit the wall hard enough you can bring it down..."]
question3a = ["What would you do? (Hulk Smash/Keep Looking)"]
script3b = ["You use the Macuahuitl to smash the wall in with all your might...", "The wall gives away, revealing a passage to the outside..."]

#-------------------------Classes----------------------#
class Leaderboard: #Stores and appends to the leaderboard
    name = ['Jesus A']
    ending = [True]
    score = ['30'] 

    def Stamp(Self, name, ending, score):
        Self.name.append(name)
        Self.ending.append(ending)
        Self.score.append(score)
        leaderboard = pd.DataFrame({'Name': Leaderboard.name, 'Ending': Leaderboard.ending, 'Score': Leaderboard.score})
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
    
    def __init__(self):
        self.name = Game.name
        self.ending = Game.ending
        self.score = Game.score
        self.answer = Game.answer
        self.inventory = Game.inventory
        self.scriptOver = scriptOver
        self.scriptBadAnswer = scriptBadAnswer
        self.scriptDrown = scriptDrown
        self.scriptWin = scriptWin
        self.scriptGen0 = scriptGen0
        self.scriptGen1 = scriptGen1
        self.scriptGen2 = scriptGen2
        self.scriptGen3 = scriptGen3
    
    def PrintEX(self):
        Timer.Passing()
        for phrase in self.script:
            print(f'\n{phrase}\n')
            Timer.Passing()

    def QuestionEX(self):
        self.answer = input(f'\n{self.question}\n').lower.strip
        return(self.answer)

    def Over(self):
        Timer.Ticking(Timer.time, 30)
        self.PrintEX(self.script.Over)
        self.ending = False
        Leaderboard.Stamp(self.name, self.ending, self.score)

    def BadAnswer(self):
        self.PrintEX(self.scriptBadAnswer)
        next = self.Over()

    def Drown(self):
        self.PrintEX(self.scriptDrown)
        next = self.Over()
    
    def Win(self):
        self.PrintEX(self.scriptWin)
        Leaderboard.Stamp(self.name, self.ending, self.score)
   
    def TimerCheck(self):
        if self.score <= 0:
            self.Drown()
        else:
            pass
    
    def Start(self, script, question):
        self.PrintEX(script)
        self.QuestionEX(question)
        if self.answer == "yes":
            pass
        elif self.answer == "no":
            self.Over()
        else:
            self.BadAnswer()

    def Q1(self, script, question):
        Timer.Ticking(Timer.time, 0)
        self.PrintEX(script)
        Timer.Passing()
        self.QuestionEX(question)
        if self.answer == "look around":
            pass

        elif self.answer == "close eyes":
            self.Over()

        else:
            self.BadAnswer()

    def Q2a(self, script, question):
        self.TimerCheck()
        Timer.Ticking(Timer.time, 1)
        self.PrintEX(script)
        self.QuestionEX(question)

        if self.answer == "get closer":
            pass

        elif self.answer == "keep looking":
            if 'Macuahuitl' in self.inventory:
                self.PrintEX(self.scriptGen0)
                self.Q2a(script2a, question2a)
    
            else:
                self.Q2b(script2b, question2b)

        else:
            self.BadAnswer()       
    
    def Q2b(self, script, question):
        self.TimerCheck()
        Timer.Ticking(Timer.time, 1)
        self.PrintEX(self.script2b)
        self.QuestionEX(self.question2b)

        if self.answer == "take":
            Inventory.AddInventory('Macuahuitl')
            self.Q2a()

        elif self.answer == "go back":
            self.Q2a()
        
        elif self.answer == "what is a macuahuitl?":
            self.PrintEX(self.scriptGen2)
            Timer.Ticking(Timer.time, 30)

        else:
            self.BadAnswer()
    
    def Q3(self, script, question):
        self.TimerCheck()
        self.PrintEX(script)
        self.QuestionEX(question)
        if self.answer == "hulk smash":
            if 'Macuahuitl' in self.inventory:
                self.PrintEX(script3b)
                self.Win()
            else:
                Timer.Ticking(Timer.Ticking, 10)
                self.PrintEX(self.scriptGen3)
                self.Q3(script3a, question3a)

        elif self.answer == "keep looking":
            if 'Macuahuitl' in self.inventory:
                self.PrintEX(self.scriptGen0)
                self.Q3(script3a, question3a)

            else:
                self.Q2b()

        
#-------------------------GameInit----------------------#

game = Game
game.Start(script0, question0)
game.Q1(script1, question1)
game.Q2a(script2a, question2a)
game.Q3(script3a, question3a)

