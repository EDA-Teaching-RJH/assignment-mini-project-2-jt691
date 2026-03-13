import sys                                                  #allows python to read the arguments #python3 games.py jack (line to input into the terminal)
import random                                               #allows for rock paper scissors and coin flip to be random and blackjack

if len(sys.argv) < 2:
    print("Please enter your first name ")
elif len (sys.argv) > 2:
    print("please enter ONLY your first name ")               #using argument to ask username 
else:
    print("Welcome", sys.argv[1])

def minigames():                                                 #list of games and options to pick from 
    print("Select a game you wish to play:")                   
    print("1. Head or Tails")
    print("2. Rock, Paper, Scissors")
    print("3. Blackjack")
    print("4. Score")
    print("5. Exit")
                        
def main():                                                                # directs user input to the variable seleted calling the function to run
    while true:
        minigames()
        select = input("Enter the number for the corresponding game")
        if select == "1":
            heads_or_tails()
        elif select == "2":
            rock_paper_scissors()
        elif select == "3":
            blackjack()
        elif select == "4":
            score()
        elif select == "5":
            print("shutting down ")
            break

def heads_or_tails():                                             #standard coin flip using flip to make it random
    Coin = ["heads", "tails"]
    while True:    
        x = input("Pick heads or tails: ").lower()
        if x not in Coin:
            print("Please selct heads or tails only")                  
        else:
            flip = random.choice(Coin)
            if x == flip:
                print("you win, the coin landed on",flip)
            else:
                print("you lose, the coin landed on",flip)

def rock_paper_scissors():                                                     #standard game of rock, paper, scissor
    options = ["rock", "paper", "scissors"]
    while True:
        x = input("Pick rock, paper or scissors:").lower()
        if x not in options:
            print("please select valid option")
        else:
            opponent = random.choice(options)
            if x == opponent:
                print("tie, opponent also picked", opponent)
            elif (x == "rock" and opponent == "scissors") or (x== "paper" and opponent == "rock") or (x == "scissors" and opponent == "paper"):
                print("you win opponent picked" , opponent)
            else:
                print("you lose opponent picked", opponent)

               

main()