from time import sleep
#from tkinter.constants import NO
import pandas as pd
import sqlite3

conn = sqlite3.connect('leaderboard.db')
c = conn.cursor()

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
question0 = "Would you open your eyes? (yes/no)"
script1 = ["It's dark, however a small crack on the ceiling gives just enough light to make your sorroundings...", "You are able to hear water rushing in from somewhere you cannot see..."]
question1 = "What would you like to do? (Look around/Close eyes)"
script2a = ["You can make out in the darkness a section of the wall that seems to have some loose rocks..."]
question2a = "What would you do? (Get closer/Keep looking)"
script2b = ["You see a Macuahuitl lying on the floor..."]
question2b = "What would you do? (Take/Go Back/What is a Macuahuitl?)"
script3a = ["You see that water trickles through this wall...", "You think that if you hit the wall hard enough you can bring it down..."]
question3a = "What would you do? (Hulk Smash/Keep Looking)"
script3b = ["You use the Macuahuitl to smash the wall in with all your might...", "The wall gives away, revealing a passage to the outside..."]

answer = None
#-------------------------Classes----------------------#
class Leaderboard: #Stores and appends to the leaderboard
    '''
    name = ['Jesus A']
    ending = [True]
    score = ['30'] 
    '''
    def Stamp(name, ending, score):
        c.execute(f"INSERT INTO leaderboard VALUES ('{name}','{ending}','{score}')")
        query = c.execute("SELECT * From leaderboard")
        cols = [column[0] for column in query.description]
        results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
        print(f'Leaderboard: \n \n {results}')
        #print(f'Leaderboard: \n \n {leaderboard}')
        '''
        Leaderboard.name.append(name)
        Leaderboard.ending.append(ending)
        Leaderboard.score.append(score)
        leaderboard = pd.DataFrame({'Name': Leaderboard.name, 'Ending': Leaderboard.ending, 'Score': Leaderboard.score})
        '''

        print(f'Leaderboard: \n \n {Leaderboard.name}{Leaderboard.ending}{Leaderboard.score}')


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
        sleep(3)

class Game: #Handles the game interactions and responses
     
    name = None
    ending = True
    score = Timer.time
    inventory = Inventory.inventory
    
    def __init__(self):
        self.name = Game.name
        self.ending = Game.ending
        self.score = Game.score
        self.inventory = Game.inventory
        self.scriptOver = scriptOver
        self.scriptBadAnswer = scriptBadAnswer
        self.scriptDrown = scriptDrown
        self.scriptWin = scriptWin
        self.scriptGen0 = scriptGen0
        self.scriptGen1 = scriptGen1
        self.scriptGen2 = scriptGen2
        self.scriptGen3 = scriptGen3
    
    def PrintEX(self, script):
        Timer.Passing()
        for phrase in script:
            print(f'\n{phrase}\n')
            Timer.Passing()

    def QuestionEX(self, question):
        global answer
        answer = input(f'\n{question}\n')
        return(answer)

    def Over(self):
        Timer.Ticking(Timer.time, 30)
        self.PrintEX(self.scriptOver)
        self.ending = False
        self.score = Timer.time
        Leaderboard.Stamp(self.name, self.ending, self.score)

    def BadAnswer(self):
        self.PrintEX(self.scriptBadAnswer)
        next = self.Over()

    def Drown(self):
        self.PrintEX(self.scriptDrown)
        next = self.Over()
    
    def Win(self):
        self.score = Timer.time
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
        if answer == "yes":
            self.Q1(script1, question1)
        elif answer == "no":
            self.Over()
        else:
            self.BadAnswer()

    def Q1(self, script, question):
        Timer.Ticking(Timer.time, 0)
        self.PrintEX(script)
        Timer.Passing()
        self.QuestionEX(question)
        if answer == "look around":
            self.Q2a(script2a, question2a)

        elif answer == "close eyes":
            self.Over()

        else:
            self.BadAnswer()

    def Q2a(self, script, question):
        self.TimerCheck()
        Timer.Ticking(Timer.time, 1)
        self.PrintEX(script)
        self.QuestionEX(question)
        if answer == "get closer":
            self.Q3(script3a, question3a)

        elif answer == "keep looking":
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
        self.PrintEX(script2b)
        self.QuestionEX(question2b)

        if answer == "take":
            Inventory.AddInventory('Macuahuitl')
            self.Q2a(script2a, question2a)

        elif answer == "go back":
            self.Q2a(script2a, question2a)
        
        elif answer == "what is a macuahuitl?":
            self.PrintEX(self.scriptGen2)
            Timer.Ticking(Timer.time, 30)

        else:
            self.BadAnswer()
    
    def Q3(self, script, question):
        self.TimerCheck()
        self.PrintEX(script)
        self.QuestionEX(question)
        if answer == "hulk smash":
            if 'Macuahuitl' in self.inventory:
                self.PrintEX(script3b)
                self.Win()
            else:
                Timer.Ticking(Timer.Ticking, 10)
                self.PrintEX(self.scriptGen3)
                self.Q3(script3a, question3a)

        elif answer == "keep looking":
            if 'Macuahuitl' in self.inventory:
                self.PrintEX(self.scriptGen0)
                self.Q3(script3a, question3a)

            else:
                self.Q2b(script2b, question2b)

        
#-------------------------GameInit----------------------#

game = Game()
game.name = game.QuestionEX("What is your name?")
game.Start(script0, question0)
