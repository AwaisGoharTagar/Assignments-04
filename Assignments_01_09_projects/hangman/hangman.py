import random
import string

# List of words to choose from
words = [
    'python', 'programming', 'computer', 'algorithm', 'database',
    'network', 'software', 'hardware', 'internet', 'developer',
    'coding', 'debugging', 'testing', 'deployment', 'version',
    'control', 'repository', 'function', 'variable', 'class'
]

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)          # Unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()              # What the user has guessed

    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show the user what they've used
        print("\nYou have", lives, "lives left. Used letters:", ' '.join(used_letters))

        # Display current word status
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))

        # Ask for user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✔️ Correct!")
            else:
                lives -= 1
                print("❌ Wrong!")
        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("⛔ Invalid character. Please enter a letter.")

    # Game result
    if lives == 0:
        print("\n😢 You died. The word was:", word)
    else:
        print("\n🎉 You guessed the word:", word, "!!")

# Run the game
hangman()
