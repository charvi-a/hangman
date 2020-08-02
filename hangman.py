import pycountry
import random


def hangman():
    li = []
    li1 = []
    won = False
    for i in range(len(pycountry.countries)):
        li1 = (list(pycountry.countries)[i].name).split()
        if len(li1) == 1:
             li.append(list(pycountry.countries)[i].name)

    word_to_guess = random.choice(li)
    word_to_lower = word_to_guess.lower()
    no_of_guesses = 8
    count = 0
    display = "?" * len(word_to_lower)
    guessed = False
    correct_guesses = []
    incorrect_guesses = []
    
    print("WELCOME TO HANGMAN")
    print("RULES: ")
    print("---> The user is required to guess the name of the country within 8 guesses.")
    print("---> The user must enter a letter.")
    print("---> If the letter guessed is incorrect that is, it does not exist in the word to be guessed, then the number of guesses decreases.")
    print("---> Otherwise, if the letter guessed is correct then the position of the correct letter in the word to be guessed is displayed.")
    print("---> Once the number of guesses are over, the game ends.")
    print("********************************************************************")
    print("The word is: "+ display)

    while no_of_guesses > 0 and not guessed:
        guessed = False
        print("You have "+ str(no_of_guesses)+ " guesses left")
        if count > 0:
              print('***********************************************************')
        letter = input("Enter a letter in lowercase: ")
        if letter.isalpha() and letter.islower() and len(letter) == 1:
            if letter in word_to_lower and letter not in correct_guesses:
                print("The letter guessed was correct.")
                correct_guesses.append(letter)
                displaylist = list(display)
                index = [i for i,letter1 in enumerate(word_to_lower) if letter==letter1]
                for ind in index:
                    displaylist[ind] = letter
                display = "".join(displaylist)
                print(display)
                count += 1
                
                if no_of_guesses < 8:
                    print(hanged(no_of_guesses))
                
                if word_to_lower == display.lower():
                    guessed = True
                    break
                continue
            
            elif letter in correct_guesses or letter in incorrect_guesses:
                print("You have already guessed this letter before.")
            else:
                no_of_guesses -= 1
                incorrect_guesses.append(letter)
                if no_of_guesses == 0:
                    break
                
        elif len(letter) == len(word_to_lower):     
            if letter == word_to_lower:
                guessed = True
                break
            else:
                print("Sorry the word you guessed is incorrect")
                no_of_guesses -= 1
            
        else:
            print("Please enter a valid letter as a guess")

        count += 1
        if no_of_guesses != 8:
            print(hanged(no_of_guesses))
        print(display)
        print("The incorrect guesses are:" + str(incorrect_guesses))
      
    if guessed:
        print("You WON! CONGRATULATIONS! You have guessed the word")
        play()
    else:
        print(hanged(0))
        print("You have "+ str(no_of_guesses)+ " guesses left")
        print("Sorry, the correct word was " + word_to_lower)
        play()
   
  
def hanged(no_of_guesses1):
    hang_string = [
    """
    ------                  
    |    |
    |    0
    |   \\|/
    |    |
    |   / \\
    -
    """,

    """                 
    ------                  
    |    |
    |    0
    |   \\|/
    |    |
    |   /
    -
    """,

    """
    ------                  
    |    |
    |    0
    |   \\|/
    |    |
    |    
    -
    """,
    """
    ------                  
    |    |
    |    0
    |   \\|
    |    |
    |   
    -
    """,
    """
    ------                  
    |    |
    |    0
    |    |
    |    |
    |   
    -
    """ ,
    """
    ------                  
    |    |
    |    0
    |    |
    |    
    |   
    -
    """,
    """
    ------                  
    |    |
    |    0
    |       
    |   
    -
    """,
    """
    ------                  
    |    |
    |    
    |   
    |    
    |   
    -
    """

    ]
        
    return hang_string[no_of_guesses1]


def play():
    play_again = False
    let = input("Enter Y to play again and N to exit ")
    if let == 'Y' or let == 'y':
       print('***********************************************************')
       hangman()
    else:
        exit()


