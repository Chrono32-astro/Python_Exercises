
import random
import time

def spin_row ():
    symbols = ['🍋', '🍉', '🔔', '🐉', '🫧', '🍒']
    return [random.choice (symbols) for x in range (3)]

def print_row (row):
    print ("***************")
    print (" | " .join (row))
    print ("***************")

def get_payout (row, bet ):
    if row[0] == row[1] == row[2] :
        return bet * 100
    elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2] :
        return bet * 25
    else :
        return 0
        print (f"you lost ${bet}")
        
def main ( ) :
    
    balance = 100
    print ("          Welcome to pyslots          ")
    print ("symbols 🍋 🍉 🔔 🐉 🫧 🍒")
    print (f"Your balance is ${balance}")
    
    while balance > 0 :
        print (f"Curent balance ${balance}")
        bet = input ("How much would you like bet ? : $")
        if not bet.isdigit ( ) :
            print ("Enter a valid input, which can only be a number ")
            continue
        bet = float (bet)
        if bet > balance :
            print ("You can't bet more than your balance")
            continue
        if bet <= 0 :
            print ("Your bet can't bet zero or negative")
            continue
        balance -= bet
        row = spin_row ( )
        print ("Spining...")
        time.sleep (3)

        print_row (row)
        payout = get_payout (row, bet)
        if payout > 0 :
            print (f"You won ${payout}")
        else :
            print ("Sorry you lost this round")

        balance += payout
        play = input ("Do you want to spin again? ( Y/N ) : ").upper ( )
        if play != "Y" :
            break
    print (f"Game over ! \nYour final balance is ${balance}")

if __name__ == "__main__" :
    main ( )