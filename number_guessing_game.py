import random


def guess_user_number(x, y):
    random_number = random.randint(x, y)
    print("숫자가 생성되었습니다. 시작합니다!")
    for _ in range(7):
        guess = int(input(f"{x}와 {y} 사이의 숫자를 입력하세요: "))
        if guess < random_number:
            print("입력한 값이 너무 작습니다.")
        elif guess > random_number:
            print("입력한 값이 너무 큽니다.")
        else:
            print(f"축하합니다! 정답은 {random_number}입니다.")
            break
    else:
        print(f"안타깝지만 기회를 모두 사용했습니다. 정답은 {random_number}입니다.")


def guess_computer_number(x, y):
    low = x
    high = y
    random_number = random.randint(low, high)
    print(f"컴퓨터가 {low}과 {high} 사이의 숫자를 생각합니다...")
    attempts = 0
    while True:
        guess = random.randint(low, high)
        print(f"컴퓨터가 추측한 숫자는 {guess} 입니다.")
        attempts += 1

        if guess < random_number:
            print("컴퓨터가 너무 작은 숫자를 추측했습니다.")
            low = guess + 1
        elif guess > random_number:
            print("컴퓨터가 너무 큰 숫자를 추측했습니다.")
            high = guess - 1
        else:
            print(f"컴퓨터가 정답을 맞췄습니다! 정답은 {random_number}입니다.")
            print(f"컴퓨터가 시도한 횟수: {attempts}")
            break


def play_game():
    while True:
        mode = input(
            "게임 모드를 선택하세요 (사용자 숫자 맞추기: 1, 컴퓨터 숫자 맞추기: 2): "
        )
        if mode == "1":
            a, b = map(int, input("범위를 입력하세요 (시작 끝): ").split())
            guess_user_number(a, b)
        elif mode == "2":
            a, b = map(int, input("범위를 입력하세요 (시작 끝): ").split())
            guess_computer_number(a, b)
        else:
            print("올바른 모드를 선택하세요.")

        play_again = input("다시 플레이하시겠습니까? (yes/no): ")
        if play_again.lower() != "yes":
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    play_game()
