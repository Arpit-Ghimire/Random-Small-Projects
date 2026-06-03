import random

words = [
    {"word": "chair", "hint": "You sit on it", "difficulty": "easy"},
    {"word": "apple", "hint": "A red or green fruit", "difficulty": "easy"},
    {"word": "bread", "hint": "Baked food made from flour", "difficulty": "easy"},
    {"word": "house", "hint": "People live in it", "difficulty": "easy"},
    {"word": "water", "hint": "You drink it", "difficulty": "easy"},
    {"word": "clock", "hint": "Shows the time", "difficulty": "easy"},
    {"word": "smile", "hint": "You do this when happy", "difficulty": "easy"},

    {"word": "plant", "hint": "A green living thing", "difficulty": "medium"},
    {"word": "river", "hint": "A long flowing water body", "difficulty": "medium"},
    {"word": "light", "hint": "Opposite of dark", "difficulty": "medium"},
    {"word": "beach", "hint": "Sandy place near the sea", "difficulty": "medium"},
    {"word": "sound", "hint": "You hear it", "difficulty": "medium"},
    {"word": "train", "hint": "Runs on tracks", "difficulty": "medium"},
    {"word": "music", "hint": "You listen to it", "difficulty": "medium"},

    {"word": "brave", "hint": "Shows no fear", "difficulty": "hard"},
    {"word": "sharp", "hint": "Can cut easily", "difficulty": "hard"},
    {"word": "quiet", "hint": "Very little noise", "difficulty": "hard"},
    {"word": "truth", "hint": "Not a lie", "difficulty": "hard"},
    {"word": "focus", "hint": "Pay close attention", "difficulty": "hard"},
    {"word": "proud", "hint": "Feeling good about yourself", "difficulty": "hard"}
]

chances = 5
curr_chances = 0

selection = random.choice(words)
word = selection["word"]
hint = selection["hint"]
diff = selection["difficulty"]

print(f"\nHint : {hint}")
print(f"Difficulty : {diff}")

while (curr_chances < chances):

    guess_temp = input("Enter your guess for 5 lettered word : ")
    guess = guess_temp.lower()

    if len(guess) != 5:
        print("Please enter a 5-letter word only.")
        continue

    
    curr_chances += 1

    if(word == guess):
        print(f"\nCongratulations! You guessed the correct word in {curr_chances} attempts.")
        break
    else:
        print("\nIncorrect!")
        print(f"{chances - curr_chances} chances left.")
    
else:
    print("\n\nMaximum attempts finished.\nYou lost the game.")
    print(f"The correct word was: {word}")

