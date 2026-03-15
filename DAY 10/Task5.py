secret_number = 7
guess = 0

print("--- Guess the Number (1 to 10) ---")

while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print("Correct! You found the secret number. ")
