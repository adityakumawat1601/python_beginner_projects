"""hangman.py is a word quiz game.
this game is made on 18-12-2022 . author - adityakumawat. adityakumawat@gmail.com.
this is practice coding project at grass ."""
import sys
import os
import random
def menu():
    """menu prints menu when game starts"""
    menu = """WELCOME TO HANGMAN GAME
    guide-
    you got three chance to fill each empty gap.
    press 0 to exit.
    
    1.start game
    2.exit    
    """
    hangman ="""   
                 ________
                |       +
                |     --^--
                |       |
                |   (save him)
                |      hangman  """


    hangman2 =  """

                 __________
                |         -                
                |      hangman
                |      is saved!
                |
                |       +<|---    \n\n"""
    

    return menu,hangman,hangman2
    
    
def random_words():
    """function random_words. generates random words from list of words . through choice function 
    in  random library."""
    words = ["pineapple","welcome","dolphin","orange","banana","pomegranete","sugarcane","papaya","google","intention",
                        "reality","response","classroom","fishing","airport","speaker","freedom","product","passenger","election","software"   ]
    rdm_word = random.choice(words)
    return rdm_word


if __name__ == "__main__":
    os.system("cls")
    MENU,HANGMAN, HANGMAN2 = menu()
    print(MENU)
    while True:
        print("\n\n")
        choice = input("enter your choice[1 or 2] :")
        if choice == "2":
            sys.exit(0)
        elif choice =="1":
            os.system("cls")
            break
        else:
            print("invalid input .enter 1 or 2")
            
    while True:
        r = random_words().upper()
        print(f"\t\t\t\t\t\t{r[:1]}_{r[2:3]}_{r[4:5]}_{r[6:]}".upper())
        for _ in range(3):
            place1 = input("enter answer place 1:").strip().upper()
            print(f"{r[:1]}{place1}{r[2:3]}_{r[4:5]}_{r[6:]}".upper())
            if place1!=r[1:2]:
                print("your answer is incorect\n")
                continue
            else:
                print("correct choice well done.\n")
                break

        for _ in range(3):
            place2 = input("enter your answer 2:").strip().upper()
            print(f"{r[:1]}{place1}{r[2:3]}{place2}{r[4:5]}_{r[6:]}".upper())
            if place2 != r[3:4]:
                print("your answer is incorrect.\n ")
                continue
            else:
                print("correct choice well done.\n")
                break

        for _ in range(3):
            place3 = input("enter your answer 3:").strip().upper()
            print(f"{r[:1]}{place1}{r[2:3]}{place2}{r[4:5]}{place3}{r[6:]}".upper())
            if place3 != r[5:6]:
                print("your answer is incorrect.\n ")
                continue
            else:
                print("correct choice well done.\n")
                break

        user = f"{r[:1]}{place1}{r[2:3]}{place2}{r[4:5]}{place3}{r[6:]}"
        if user==r:
            print(HANGMAN2)
            print("\t\tcorrect answer.",r.upper())
            print("\t\t\t\t\tcongrats! you won hangman game.".title())

        else:
            print("correct word is",r)
            print("you lose hangman better luck next time.".title())
            print("\t\t\tPLAY AGAIN - enter YES")
            print("\t\t\tEXIT - enter NO")
        play = input("enter [YES OR NO] :").strip().upper()
        if play == "YES":
            os.system("cls")
            continue
        elif play == "NO":
            sys.exit(0)
        else:
            print("invalid agruement type only yes or no")
            break

        
        




