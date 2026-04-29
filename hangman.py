import random

word = random.choice(['apple', 'orange', 'banana', 'mango'])
guesses = ''
turns = 5

print("Guess the fruit name!")

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou Win!")
        break

    guess = input("\n\nEnter a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print(f"Wrong! {turns} turns left.")

if turns == 0:
    print("\nYou Lose! The word was:", word)