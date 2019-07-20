import random

def RollDice():
    rolled = random.randint(1,6)
    print("You got: " + str(rolled))
    return rolled