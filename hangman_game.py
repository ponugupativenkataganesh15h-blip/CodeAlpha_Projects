import random

# Predefined list of words
words = ["apple", "tiger", "chair", "robot", "green"]

# Select a random word
word = random.choice(words)

# Create empty display
guessed_word = ["_"] * len(word)

# Track attempts and guessed letters
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
