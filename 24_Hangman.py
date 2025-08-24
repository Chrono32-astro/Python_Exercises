import random

from words_list import words 

#dictionaty containing a turple
hangman_art = {0 : (" " , " " ," ") ,
               1 : (" O " , "  " ," ") ,
               2 : (" O " , " | " ," ") ,
               3 : (" O " , "/| " ," ") ,
               4 : (" O " , "/|\\" ," ") ,
               5 : (" O " , "/|\\" ,"/ ") ,
               6 : (" O " , "/|\\" ,"/ \\")}



def display_hangman (wrong_guesses) :
    print ("********************")
    for i in hangman_art [wrong_guesses] :
        print (i)
    print ("********************")

def display_hint (hint) :
    line = " " .join (hint)
    print (line)

def display_answer (answer) :
    line = " " .join (answer)
    print (answer)


def main ( ) :
    answer = random.choice (words)
    hint = ["_"] * len (answer)
    wrong_guesses = 0
    guessed_letters = set ( )
    is_running =True

    while is_running :
        display_hangman (wrong_guesses)
        display_hint (hint)
        guess = input ("Guess a letter in the word : ").lower ( )


        if len (guess) != 1 or not guess.isalpha ( ) :
            print ("Not a valid input")
            continue

        if guess in guessed_letters :
            print (f"{guess} is already guessed")
            continue
        guessed_letters.add (guess)
        

        if guess in answer :
            for i in range ( len (answer) ) :
                if answer [i] == guess :
                    hint [i] = guess
                    
        else :
            wrong_guesses += 1 
        
        if "_" not in hint :
            display_hangman (wrong_guesses)
            display_answer (answer)
            print ("You win ")
            is_running = False
        
        
        elif wrong_guesses >= len (hangman_art) -1 :
            display_hangman (wrong_guesses)
            display_answer (answer)
            print ("Game over,you lose ")
            is_running = False


if __name__ =="__main__" :
    main ( )