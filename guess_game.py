import os
import random


os.system("cls")
# linux cls --> clear

print("\n\n")
print("Welcome to Guess Game".center(100))
print("\n\n")

guess = random.randint(1, 50)
chances = 5

while chances>0:
    print("__"*50)
    print(f"\n\nyou have left {chances} chances to win this game!\n\n")
    user = int(input("your guess[1-50]: "))
    if user<1 or user>50:
        print("\nWarning! Guess only between 1 and 50!")
        continue
        
    if user==guess:
        print("\nWhoo! you such a master! you have won the game!")
        break
    elif user>guess:
        print("\nHint: your guess is high.")
    else:
        print("\nHint: your guess is low.")
    chances -= 1
else:
    print("Ohh!You such a looser!")
