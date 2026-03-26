import sys                                                  #allows python to read the arguments #python3 games.py jack (line to input into the terminal)
import random                                               #allows for rock paper scissors and coin flip to be random and blackjack

def minigames():                                                 #list of games and options to pick from 
    print("Select a game you wish to play:")                   
    print("1. Head or Tails")
    print("2. Rock, Paper, Scissors")
    print("3. Blackjack")
    print("4. Score")
    print("5. Exit")
                        
def main():                              # Moved argument to main function to make more readable and added sys. exit() to end unless a name is given
    if len(sys.argv) < 2:                                                 # directs user input to the variable seleted calling the function to run
        print("Please enter your first name ")                               #using argument to ask username 
        sys.exit()
    if len (sys.argv) > 2:
        print("please enter ONLY your first name ")               
        sys.exit()
    print("Welcome", sys.argv[1])
    
    while True:
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
    coin = ["heads", "tails"]
    while True:    
        x = input("Pick heads or tails: ").lower()
        if x not in coin:
            print("Please selct heads or tails only")                  
        else:
            flip = random.choice(coin)
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

def blackjack():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",  #standard deck of cards 
             "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
             "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
             "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]
    def hand_value(hand):
        total = 0                                                  # created two variables, total is overlall value of hand whilst ace will be used later to change the value to 1 or 11
        aces = 0
        
        for card in hand:                                          #assings J,Q,K as 10 and A as 11 but if the total goes over 21 the value of the ace will change to 1 
            if card in ["J", "Q", "K"]:
                total += 10
            elif card == "A":
                aces += 1
                total += 11
            else:
                total += int(card)

    while total > 21 and aces > 0:                  # whilst a ace is in hand the value of total will change from 11 to 1 to prevent the player going over 21 
        total -= 10
        aces -= 1    
    return total 
    
    
    player = []
    dealer = []

    player.append(random.choice(cards))              #deals two starting cards to the player and the dealer 
    cards.remove(player[-1])
    player.append(random.choice(cards))
    cards.remove(player[-1])
    
    dealer.append(random.choice(cards))
    cards.remove(dealer[-1])
    dealer.append(random.choice(cards))
    cards.remove(dealer[-1])



if __name__ == "__main__":
    main()              

