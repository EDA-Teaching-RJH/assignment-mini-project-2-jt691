import sys                                                  #allows python to read the arguments #python3 games.py jack (line to input into the terminal)


if len(sys.argv) < 2:
    print("Please enter your first name ")
elif len (sys.argv) > 2:
    print("please enter ONLY your first name ")               #using argument to ask username 
else:
    print("Welcome", sys.argv[1])

