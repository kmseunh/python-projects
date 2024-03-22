import random


class NumberBaseballGame:
    def __init__(self):
        self.secret_number = self.generate_random_number()
        self.attempts = 0

    @staticmethod
    def generate_random_number():
        """
        컴퓨터가 무작위로 생성한 3자리의 숫자를 반환
        """
        digits = [str(i) for i in range(10)]  # 0부터 9까지의 숫자 리스트
        random.shuffle(digits)
        return "".join(digits[:3])

    def get_user_guess(self):
        """
        사용자로부터 3자리의 숫자를 입력받아 반환
        """
        while True:
            user_input = input("3자리의 숫자를 입력하세요: ")
            if user_input.isdigit() and len(user_input) == 3:
                return user_input
            else:
                print("올바른 형식의 숫자를 입력하세요.")

    def compare_numbers(self, user_guess):
        """
        사용자가 입력한 숫자와 컴퓨터가 생성한 숫자를 비교하여 스트라이크와 볼의 개수를 반환
        """
        strikes = 0
        balls = 0
        for i in range(3):
            if user_guess[i] == self.secret_number[i]:
                strikes += 1
            elif user_guess[i] in self.secret_number:
                balls += 1
        return strikes, balls

    def play_game(self):
        """
        숫자야구 게임 실행
        """
        print("숫자야구 게임을 시작합니다!")
        while True:
            user_guess = self.get_user_guess()
            self.attempts += 1
            strikes, balls = self.compare_numbers(user_guess)
            print(f"{strikes} 스트라이크, {balls} 볼")
            if strikes == 3:
                print(f"축하합니다! {self.attempts}번 만에 숫자를 맞추셨습니다.")
                break


if __name__ == "__main__":
    game = NumberBaseballGame()
    game.play_game()
