import random


class Hangman:
    def __init__(self):
        self.words = [
            "python",
            "javascript",
            "typescript",
            "sveltekit",
            "springboot",
            "fastapi",
        ]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = 10

    def display_word(self):
        return "".join(
            [
                letter if letter in self.guessed_letters else "_"
                for letter in self.word_to_guess
            ]
        )

    def is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if self.is_valid_guess(guess):
                return guess
            else:
                print("Please enter a single letter.")

    def play(self):
        print("Welcome to Hangman!")

        while self.attempts_left > 0:
            print("\nAttempts left:", self.attempts_left)
            print("Word:", self.display_word())

            guess = self.get_guess()

            if guess in self.guessed_letters:
                print("You've already guessed that letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word_to_guess:
                print("Good guess!")
                if all(letter in self.guessed_letters for letter in self.word_to_guess):
                    print(
                        "Congratulations! You've guessed the word:", self.word_to_guess
                    )
                    break
            else:
                print("Sorry, that letter is not in the word.")
                self.attempts_left -= 1

        else:
            print("You've run out of attempts! The word was:", self.word_to_guess)


game = Hangman()
game.play()
