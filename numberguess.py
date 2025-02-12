import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congrats! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_number()
