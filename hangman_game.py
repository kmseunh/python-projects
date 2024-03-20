import random


class Hangman:
    def __init__(self):
        # Hangman 게임에 사용될 단어 리스트
        self.words = [
            "python",
            "javascript",
            "typescript",
            "sveltekit",
            "springboot",
            "fastapi",
        ]
        # 랜덤으로 선택된 단어를 저장할 변수
        self.word_to_guess = random.choice(self.words)
        # 사용자가 추측한 글자들을 저장할 리스트
        self.guessed_letters = []
        # 남은 시도 횟수를 저장할 변수
        self.attempts_left = 10

    # 현재 게임 상태에서 단어를 표시하는 메서드
    def display_word(self):
        return "".join(
            [
                letter if letter in self.guessed_letters else "_"
                for letter in self.word_to_guess
            ]
        )

    # 사용자 입력이 유효한 글자인지 확인하는 메서드
    def is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    # 사용자에게 글자를 입력받는 메서드
    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if self.is_valid_guess(guess):
                return guess
            else:
                print("Please enter a single letter.")

    # Hangman 게임을 실행하는 메서드
    def play(self):
        print("Welcome to Hangman!")

        while self.attempts_left > 0:
            print("\nAttempts left:", self.attempts_left)
            print("Word:", self.display_word())

            guess = self.get_guess()

            # 이미 추측한 글자인지 확인
            if guess in self.guessed_letters:
                print("You've already guessed that letter.")
                continue

            # 추측한 글자를 리스트에 추가
            self.guessed_letters.append(guess)

            # 추측한 글자가 정답에 포함되어 있는지 확인
            if guess in self.word_to_guess:
                print("Good guess!")
                # 모든 단어가 추측된 경우 게임 종료
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


# Hangman 객체를 생성하고 게임을 실행
game = Hangman()
game.play()
