import random
print("\tWELCOME TO \"GUESS THE NUMBER\" GAME!")
print("\nRULES:")
print("1. Computer Will Generate A Random Number Between [1 to 100].")
print("2. You Can Choose Between Different Levels [Easy, Medium, Hard].")
print("3. Easy -> 7 Attempts; \t Medium -> 5 Attemts; \t Hard -> 3 Attempts.")
print("\n\t\tALL THE BEST!\n")

# ------------------------------ MAIN FUNCTIONS -----------------------------

def guess_number(random_number, max_attempts):
    count = 0
    while(count <= max_attempts):
        try:
            user_input = int(input("Enter Your Guessed Number: "))
            count += 1
            if(user_input == random_number):
                print("Wow you guessed the number!")
                print(f"You Took {count} Attempts To Guess!")
                print("Thanks For PLaying The Game :) !\n")
                return
            else:
                print("Oops your guess is wrong!")
                if(user_input > random_number):
                    print("Hint -> \"Your Guess Is Too HIGH!\"\n") 
                else:
                    print("Hint -> \"Your Guess Is Too LOW!\"\n") 
        except ValueError:
            print("Invalid Value!")
    print("GAME OVER!")
    print(f"The Number is {random_number}.\n")
def continue_game():
    while(True):
        choice = input("Do you want to play again? ['y' or 'n']: ").lower()
        if(choice == 'y'):
            return True
        elif(choice == 'n'):
            print("Thanks For PLaying The Game :) !\n")
            return False
        else:
            print("Invalid Input! Please Enter 'y' or 'n'.")

# ------------------------------ GAME LOOP -----------------------------

attempts = {"Easy" : 7, "Medium" : 5, "Hard" : 3}
while(True):
    level = input("Choose your level [Easy, Medium, Hard]: ").capitalize().strip()
    if level in attempts:
        max_attempts = attempts[level]
        random_number = random.randint(1,100)
        print(f"\nYou've choosen {level} level -> You have {max_attempts} attempts.\n")
        guess_number(random_number, max_attempts)
    else:
        print("Invalid Input! Please Enter Correct Input.\n")
        continue
    if not continue_game():
        break