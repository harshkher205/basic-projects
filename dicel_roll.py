import random
print("welcome to the Game of rolling the Dice.")
while True:
    choice = input("press 'Enter' to roll the dice or 'q' to quit. ")
    choice = choice.strip()
    if choice == "q" or choice == 'Q':
        print("thanks for playing the game")
        break
    elif choice=="":
        number = random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("invalid input")
print("game over")





