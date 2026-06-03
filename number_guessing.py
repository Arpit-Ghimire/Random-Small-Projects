import random

number = random.randint(0,100)

guess = int(input("Enter your guess : "))
guesses = 0

while(guess != number):
    guesses += 1

    if(guess > number):
        print("Your guess is higher.")
        guess = int(input("Enter your guess : "))

    elif(guess < number):
        print("Your guess is lower.")
        guess = int(input("Enter your guess : "))
    
    else:
        break

print(f"Congratulations you guess the correct number i.e {number} in {guesses} guesses.")