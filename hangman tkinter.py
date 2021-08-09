import pycountry
import random


def Handler(event):
    hangman()

def randomWord():
    li = []
    li1 = []
    
    c1.create_line(300, 35, 300, 200)
    c1.create_line(200,35,300,35)
    global no_of_guesses, word_to_guess,word_to_lower, display, incorrect_guesses, correct_guesses
    no_of_guesses = 8
    correct_guesses = []
    incorrect_guesses = []
    won = False
    for i in range(len(pycountry.countries)):
        li1 = (list(pycountry.countries)[i].name).split()
       
        if len(li1) == 1:
             li.append(list(pycountry.countries)[i].name)
    
    word_to_guess = random.choice(li)
    word_to_lower = word_to_guess.lower()
    result.configure(text = "")
    lblincorrect.configure(text = '[]')
    lblguesses.configure(text = "You have {} guesses left.".format(no_of_guesses))
    display = '?' * len(word_to_lower)
    lbldisplay.configure(text = display)
    
    
def hangman():
    global no_of_guesses,  word_to_guess,word_to_lower,display, incorrect_guesses,correct_guesses
    letter = inputletter.get()
    entletter.delete(0,END)
    
    if letter.isalpha() and len(letter) == 1:
        if letter in word_to_lower and letter not in correct_guesses:
            result.configure(text = "The letter guessed was correct.")
            correct_guesses.append(letter)
            displaylist = list(display)
            index = [i for i,letter1 in enumerate(word_to_lower) if letter==letter1]
            
            for ind in index:
                displaylist[ind] = letter
         
            display = "".join(displaylist)
            lbldisplay.configure(text = display)

            if word_to_lower == display.lower():
                guessed = True
                result.configure(text = "You WON! CONGRATULATIONS! You have guessed the word")
                res = messagebox.askyesno("Notification", "Do you want to play again?")
                if res == True:
                    c1.delete("all")
                    randomWord()
                else:
                    c1.delete("all")
                    window.destroy()
    
        
        elif letter in correct_guesses or letter in incorrect_guesses:
            result.configure(text = "You have already guessed this letter before.")
        else:
            no_of_guesses -= 1
            lblguesses.configure(text = "You have {} guesses left.".format(no_of_guesses))
            incorrect_guesses.append(letter)
            lblincorrect.configure(text = incorrect_guesses)
            result.configure(text = "The letter guessed was incorrect.")
           
            if no_of_guesses == 0:
                result.configure(text = "Sorry, the correct word was {}".format(word_to_lower))
                c1.configure(hanged(0))
                res = messagebox.askyesno("Notification", "Do you want to play again?")
                if res == True:
                    c1.delete("all")
                    randomWord()
                else:
                    c1.delete("all")
                    window.destroy()
            
    elif len(letter) == len(word_to_lower):     
        if letter == word_to_lower:
            lbldisplay.configure(text = word_to_lower)
            result.configure(text = "You WON! CONGRATULATIONS! You have guessed the word")
            res = messagebox.askyesno("Notification", "Do you want to play again?")
            if res == True:
                c1.delete("all")
                randomWord()
            else:
                c1.delete("all")
                window.destroy()
        else:
            no_of_guesses -= 1
            lblguesses.configure(text = "You have {} guesses left.".format(no_of_guesses))
            result.configure(text = "Sorry the word you guessed is incorrect")
           
        
    else:
        result.configure(text = "Please enter a valid letter as a guess")

    c1.configure(hanged(no_of_guesses))

    
import tkinter as tk
from tkinter import *
import pycountry
from tkinter import messagebox
import random

window = tk.Tk()
f = tk.Frame(window)
c1 = tk.Canvas(f)
f.pack(side = "right")
c1.pack()

c1.create_line(300, 35, 300, 200)
c1.create_line(200,35,300,35)

window.configure(bg = 'pale turquoise')
window.title("LET'S PLAY HANGMAN")
T = tk.Text(window, height=100, width=200, font = ("Times New Roman" , 16, 'bold'), bg='pale turquoise')
T.pack()
quote = '''WELCOME TO HANGMAN
RULES: 
---> The user is required to guess the name of the country within 8 guesses.
---> The user must enter a word or letter.
---> If the letter guessed is incorrect that is, it does not exist in the word to be guessed, then the number of guesses decreases.
---> Otherwise, if the letter guessed is correct then the position of the correct letter in the word to be guessed is displayed.
---> Once the number of guesses are over, the game ends.'''
        
T.insert(tk.END, quote)

window.bind("<Return>", Handler)

inputletter = StringVar()
entletter = Entry(window, bd = 6, justify = 'center', relief = 'groove', font= ("Helvetica" , 16), textvariable = inputletter)
entletter.place(x = 500, y = 300)
entletter.focus_set()

lbl=Label(window, text="Enter a letter in lowercase and press enter ", fg='green',  font=("Helvetica", 16))
lbl.place(x=50, y=300)

result = Label(window, text = "" ,  bg = 'pale turquoise', font = ("Helvetica", 16))
result.place(x = 100 , y = 500)

lblword = Label(window, text = "The word is" , fg = 'green', font = ("Helvetica", 16))
lblword.place(x = 50 , y = 350)

lbldisplay = Label(window, text = "", font = ("Helvetica", 16), fg = 'green')
lbldisplay.place(x = 350 , y = 350)

lblguesses = Label(window,text = "" , font= ("Helvetica", 15))          
lblguesses.place(x = 50, y = 400)

incorr = Label(window, text = "The incorrect guesses are: ", font = ("Helvetica",15))
incorr.place(x = 50, y = 450)
lblincorrect = Label(window, text = "[]", font =("Helvetica",15))
lblincorrect.place(x = 500, y = 450)
    
 
def hanged(no_of_guesses):
    if no_of_guesses == 7:
        c1.create_line(200,35,200,70)
    if no_of_guesses == 6:
        c1.create_oval(185,70,215,100)
        c1.create_line(192,80,192,85)
        c1.create_line(207,80,207,85)
        c1.create_line((192, 90,200,95, 207, 90), width = 2, smooth = 1, tags= 'smiley')
    if no_of_guesses == 5:
        c1.create_line(200,100,200,150)
    if no_of_guesses == 4:
        c1.create_line(170,100,200,120)
    if no_of_guesses == 3:
        c1.create_line(230,100,200,120)
    if no_of_guesses == 2:
        c1.create_line(170,170,200,150)
    if no_of_guesses == 1:
        c1.create_line(230,170,200,150)
    if no_of_guesses == 0:
        c1.delete('smiley')
        c1.create_line((192, 90,200,85, 207, 90), width = 2, smooth = 1)


randomWord()
tk.mainloop()


