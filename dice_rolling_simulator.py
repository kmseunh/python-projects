import random


def roll_dice():
    """주사위를 굴리고 결과를 반환합니다."""
    return random.randint(1, 6)


def main():
    print("주사위 굴리기 시뮬레이터에 오신 것을 환영합니다.")

    while True:
        start_game = input("주사위를 굴리시겠습니까? ('y' or 'n'): ").lower()

        if start_game == "y":
            dice_result = roll_dice()
            print(f"주사위를 굴려서 {dice_result}이 나왔습니다.")
        elif start_game == "n":
            print("주사위 굴리기 시뮬레이터를 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")


if __name__ == "__main__":
    main()
