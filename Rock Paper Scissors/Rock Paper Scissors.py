import tkinter as tk
from tkinter import PhotoImage
import random, time

UserScore=0
ComputerScore=0
Font="Courier New"
BlankImage=tk.PhotoImage(file="Rock Paper Scissors/Blank Image.png")
RockImage=tk.PhotoImage(file="Rock Paper Scissors/Rock.png")
PaperImage=tk.PhotoImage(file="Rock Paper Scissors/Paper.png")
ScissorsImage=tk.PhotoImage(file="Rock Paper Scissors/Scissors.png")
Rock2Image=tk.PhotoImage(file="Rock Paper Scissors/Rock2.png")
Paper2Image=tk.PhotoImage(file="Rock Paper Scissors/Paper2.png")
Scissors2Image=tk.PhotoImage(file="Rock Paper Scissors/Scissors2.png")

def SetUserChoice(option):
    global ComputerChoice
    UserChoiceImageLabel.config(image=BlankImage)
    ComputerChoiceImageLabel.config(image=BlankImage)
    time.sleep(1)
    GameLabel.config(text="3")
    Window.update()
    time.sleep(1)
    GameLabel.config(text="2")
    Window.update()
    time.sleep(1)
    GameLabel.config(text="1")
    Window.update()
    time.sleep(1)
    SetUserChoiceLabel(option)
    SetComputerChoiceLabel()
    CalulateResult(option, ComputerChoice)

def SetUserChoiceLabel(choice):
    if choice == 1:
        UserChoiceImageLabel.config(image=RockImage)
    elif choice == 2:
        UserChoiceImageLabel.config(image=PaperImage)
    else:
        UserChoiceImageLabel.config(image=ScissorsImage)

def SetComputerChoiceLabel():
    global ComputerChoice
    ComputerChoice=random.randint(1,3)
    if ComputerChoice == 1:
        ComputerChoiceImageLabel.config(image=Rock2Image)
    elif ComputerChoice == 2:
        ComputerChoiceImageLabel.config(image=Paper2Image)
    else:
        ComputerChoiceImageLabel.config(image=Scissors2Image)

def CalulateResult(user, computer):
    global ComputerScore, UserScore
    if user == 1 and computer == 2:
        GameLabel.config(text="You lost! Try again.")
        ComputerScore+=1
        ComputerScoreLabel.config(text=f"Bot: {ComputerScore}")
    elif user == 1 and computer == 3:
        GameLabel.config(text="You Won! Next round.")
        UserScore+=1
        UserScoreLabel.config(text=f"You: {UserScore}")
    elif user == 2 and computer == 3:
        GameLabel.config(text="You lost! Try again.")
        ComputerScore+=1
        ComputerScoreLabel.config(text=f"Bot: {ComputerScore}")
    elif user == 2 and computer == 1:
        GameLabel.config(text="You Won! Next round.")
        UserScore+=1
        UserScoreLabel.config(text=f"You: {UserScore}")
    elif user == 3 and computer == 1:
        GameLabel.config(text="You lost! Try again.")
        ComputerScore+=1
        ComputerScoreLabel.config(text=f"Bot: {ComputerScore}")
    elif user == 3 and computer == 2:
        GameLabel.config(text="You Won! Next round.")
        UserScore+=1
        UserScoreLabel.config(text=f"You: {UserScore}")
    else:
        GameLabel.config(text="It's a draw! Again.")

Window=tk.Tk()
Window.geometry("500x200")
Window.title("Rock Paper Scissors")

WelcomeLabel=tk.Label(Window, text="Rock, Paper, Scissors", font=(f"{Font}", 15, "bold"))
WelcomeLabel.grid(row=1, column=2)

UserScoreLabel=tk.Label(Window, text=f"You: {UserScore}", font=(f"{Font}", 12, "bold"))
UserScoreLabel.grid(row=1, column=1)

UserChoiceImageLabel=tk.Label(Window, image=BlankImage)
UserChoiceImageLabel.grid(row=2, column=1)

ComputerScoreLabel=tk.Label(Window, text=f"Bot: {ComputerScore}", font=(f"{Font}", 12, "bold"))
ComputerScoreLabel.grid(row=1, column=3)

ComputerChoiceImageLabel=tk.Label(Window, image=BlankImage)
ComputerChoiceImageLabel.grid(row=2, column=3)

GameLabel=tk.Label(Window, text="Choose Your Option!", font=(f"{Font}", 12, "bold"))
GameLabel.grid(row=2, column=2)

ButtonRock=tk.Button(text="Rock", font=(f"{Font}", 10, "bold"), command=lambda: SetUserChoice(1))
ButtonPaper=tk.Button(text="Paper", font=(f"{Font}", 10, "bold"), command=lambda: SetUserChoice(2))
ButtonScissors=tk.Button(text="Scissors", font=(f"{Font}", 10, "bold"), command=lambda: SetUserChoice(3))

ButtonRock.grid(row=3, column=1)
ButtonPaper.grid(row=3, column=2)
ButtonScissors.grid(row=3, column=3)

Window.mainloop()