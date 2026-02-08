import random

num = 1
print("welcome to the number guessing game,we have a number that needs to be guessed,you have 1o chances")
print("the secret number is between 1 to 50")
secret_number = random.randint(1,50)                                 #secret_number = 21 optional
attemps  = 10
is_guess_correct = False


while num <= 10:
    print(f"you have {attemps} attempts left.")
    user_input = int(input("enter a number: "))
    if user_input == secret_number:
        print("congratulations you guessed correct the number")
        print("you won")
        is_guess_correct = True
        break
    else:
        if user_input < secret_number:
            higher_or_lower ="higher"
            print(f"your guess is wrong Try {higher_or_lower} number")
        else:
            higher_or_lower = "lower"
            print(f"your guess is wrong Try {higher_or_lower} number")

    attemps -= 1
    num += 1
if  not is_guess_correct:    #is_guess_correct == False (or)
    print("bad luck you lost,you have no more attempts left now")
    print(f"the secret number was {secret_number} GAMEOVER")






