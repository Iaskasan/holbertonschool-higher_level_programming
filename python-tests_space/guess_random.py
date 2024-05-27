from random import randrange
max_range = int(input("Choose the max number range: "))
number_to_guess = randrange(max_range + 1)
number_of_tries = 0
while 1:
    number_of_tries += 1
    user_number = int(input(f"Guess the number between 0 and {max_range}: "))
    if user_number < number_to_guess:
        print("Its more than that!")
    elif user_number > number_to_guess:
        print("LESS LESS!")
    else:
        print(f"GG, the number was indeed {number_to_guess}!")
        print(f"You guessed it in {number_of_tries} attemps")
        if number_of_tries == 1:
            print("Yeah that's just luck...")
        break
