def save_score(name,points):                 # Files I/O files, saves score to file 
    with open("scores.txt", "a") as file:
        file.write(name + ": " + str(points) + "\n")     

def test_hand_value():                     #testing - verify that the hand values is working correctly by asserting values of different hands 
    assert hand_value(["10, J"]) == 20
    assert hand_value(["A, 9"]) == 20
    assert hand_value(["A, A, 9"]) == 21
    assert hand_value(["A, A, 9, 2"]) == 12
    print("Blackjack hand value tests passed")  

import re  

def score():                 #Regex to only allow valid names ie only letters(letters from A-Z and a-z)
    global points
    print("Your current score is:", points)
    name = input("enter your name to save your score:")
    if not re.match("^[A-Za-z]+$", name):  
        print("Invalid name. Please only use letters.")
        return
    save_score(name, points)        

if not re.match ("^(heads|tails)$", x):         #regex only allows heads or tails 

if not re.match("^(hit|stand)$", choice):            # only allows hit or stand as valid inputs 
            print("please select hit or stand only")