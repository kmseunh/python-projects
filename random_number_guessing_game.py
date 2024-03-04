import random


def random_number_genrator(num1, num2):
    return random.randint(num1, num2)


def get_user_input():
    while True:
        try:
            user_input = int(input("정답: "))
            return user_input
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")


def main():
    print("랜덤 생성 숫자 범위를 지정해주세요")
    start = int(input("최소: "))
    end = int(input("최대: "))

    answer = random_number_genrator(start, end)
    print("생성 완료")

    for attempt in range(10):
        user_answer = get_user_input()
        if user_answer == answer:
            print("정답")
            break
        elif user_answer < answer:
            print("DOWN")
        elif user_answer > answer:
            print("UP")

    if attempt == 9:
        print("시도 횟수를 초과했습니다. 정답은", answer, "입니다.")


if __name__ == "__main__":
    main()
