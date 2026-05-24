import random

words = ["python", "coding", "apple", "laptop", "gaming"]

chosen_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

display_word = ["_"] * len(chosen_word)

print("🎮 Welcome to Hangman Game!")

while incorrect_guesses < max_incorrect and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:

        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display_word[index] = guess

        print("Correct guess!")

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in display_word:
    print("\n🎉 You Won!")
    print("The word was:", chosen_word)

else:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)