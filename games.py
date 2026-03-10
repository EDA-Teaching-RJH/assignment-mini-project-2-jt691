import sys                                                  #allows python to read the arguments #python3 games.py jack (line to input into the terminal)


if len(sys.argv) < 2:
    print("Please enter your first name ")
elif len (sys.argv) > 2:
    print("please enter ONLY your first name ")               #using argument to ask username 
else:
    print("Welcome", sys.argv[1])

def minigames():
    print("Select a game you wish to play:")
    print("1. Head or Tails")
    print("2. Rock, Paper, Scissors")
    print("3. Blackjack")
    print("4. Score")
    print("5. Exit")