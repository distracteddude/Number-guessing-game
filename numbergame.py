import random

def rand():
    return random.randrange(1, 100)

random_num = rand()
def main():
    print("Welcome to number guessing game, you've a total of 5 turns to guess a number")
    
    total_turns = 5

    while True:
        
        guess = int(input("Guess any number between 1 to 100: "))

        if 0 <= guess <= 100:

            if guess == random_num:
                print("Congrats you guessed the right number!")
                break

            elif 0 <= guess <= random_num:
                
                print("Too low! Please try again.")
                total_turns -= 1
                print("Total turns left = ", total_turns)
            
                if total_turns == 0:
                    print("Sorry you lost the game.")
                    print("The number was", random_num)
                    break


            elif 100 >= guess >= random_num:

                print("Too high! Please try again.")
                total_turns -= 1
                print("Total turns left = ", total_turns)

                if total_turns == 0:
                    print("Sorry you lost the game.")
                    print("The number was", random_num)
                    break

        else:
            print("Invalid input! Please enter any INTEGER between 1 to 100")            

main()