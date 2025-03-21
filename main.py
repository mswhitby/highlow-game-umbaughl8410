import random

lower_bound = 1
upper_bound = 100

secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between {} and {}): ".format(lower_bound, upper_bound)))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
        return True
    return False

def play_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        attempts += 1
        guess = get_guess()
        if check_guess(guess, secret_number):
            print("You guessed it in {} attempts!".format(attempts))
            break
