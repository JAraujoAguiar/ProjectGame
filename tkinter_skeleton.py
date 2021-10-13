from tkinter import *
from threading import Timer

feedback_text = ""
names = ["Jesus"]
root = Tk()
root.title("TombStuck")
# function_name --- reference
# function_name() --- call the function and run its body

def rebuild_new_layout():
    q = Label(root, text="New Layout Label")
    u = Entry(root)
    ok = Button(root, text="Ok", command=set_answer)
    f = Label(root, text="")
    q.pack()
    u.pack()
    ok.pack()
    f.pack()

def print_question():
    feedback_text['text'] = ''
    question['text'] = "How are you today?"
    user_input.delete(0, END)
    question.destroy()
    feedback_text.destroy()
    ok_btn.destroy()
    timer2 = Timer(5, rebuild_new_layout)
    timer2.start()

def set_answer():
    global feedback_text
    user_input_var = user_input.get()
    names.append(user_input_var)
    feedback_text['text'] = user_input_var
    timer = Timer(3, print_question)
    timer.start()


question_text: str = "What is your name"
question = Label(root, text=question_text)
user_input = Entry(root, width=10)
ok_btn = Button(root, text="Ok", width=5, command=set_answer)
feedback_text = Label(root, text="")


# style of the window
question.pack()
user_input.pack()
ok_btn.pack()
feedback_text.pack()


root.mainloop()
